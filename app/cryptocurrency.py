import time
from typing import Dict, List, Optional

import pandas as pd
from pycoingecko import CoinGeckoAPI


class CryptoAPI:
    def __init__(self, days: int = 30):
        self.days = days
        self.client = CoinGeckoAPI()
        self.coin_df = self.create_coin_df()
        self.correlation = self.correlate()

    def _list_top_coins(
        self,
        vs_currency: str = "usd",
        order: str = "volume_desc",
        top_n: int = 50,
        category: Optional[str] = None,
    ) -> List[Dict]:
        if category:
            response = self.client.get_coins_markets(
                vs_currency=vs_currency, order=order, per_page=top_n, category=category
            )
        else:
            response = self.client.get_coins_markets(
                vs_currency=vs_currency, order=order, per_page=top_n
            )

        return [
            {"id": coin["id"], "symbol": coin["symbol"].upper()} for coin in response
        ]

    def _list_price_by_coin(
        self,
        coin_id: str,
        days: int = 30,
        vs_currency: str = "usd",
        interval: str = "daily",
    ):
        response = self.client.get_coin_market_chart_by_id(
            coin_id, vs_currency=vs_currency, days=days, interval=interval
        )

        return [prices[1] for prices in response["prices"]]

    def create_coin_df(self):
        stable_coins = self._list_top_coins(top_n=50, category="stablecoins")
        top_coins = self._list_top_coins(top_n=50, order="market_cap_desc")
        coin_df = pd.DataFrame(top_coins)
        mask = coin_df["id"].isin([coin["id"] for coin in stable_coins[1:]])

        return coin_df[~mask]

    def correlate(self):
        price_matrix_df = pd.DataFrame()

        for coin in self.coin_df["id"].values:
            try:
                prices = self._list_price_by_coin(coin_id=coin, days=self.days)

                if len(prices) < self.days:
                    continue

                price_matrix_df[coin] = prices
            except Exception as e:
                print(e)
                print("History data are not enough")

            if len(price_matrix_df.columns) == 30:
                break

        return price_matrix_df.corr().round(2)
