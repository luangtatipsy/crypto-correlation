import collections

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from .api.cryptocurrency import CryptoAPI

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")


@app.get("/")
async def root(request: Request, timeframe: int = 30):
    api = CryptoAPI(days=timeframe)
    symbols = ",".join(api.coin_df["symbol"])
    n_rows, n_cols = api.correlation.shape
    data_points = []

    for col in range(n_cols):
        for row in range(n_rows):
            data_points.append([col, row, api.correlation.iloc[row, col]])

    return templates.TemplateResponse(
        "index.html",
        context={
            "request": request,
            "symbols": symbols,
            "tf": timeframe,
            "data_points": data_points,
        },
    )
