from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from requests.exceptions import HTTPError

from cryptocurrency import CryptoAPI

app = FastAPI(docs_url=None, redoc_url=None)
templates = Jinja2Templates(directory="templates")


class CustomException(Exception):
    def __init__(self, error_message: str):
        self.error_message = error_message


@app.exception_handler(CustomException)
async def exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        status_code=429,
        content={"status_code": 429, "message": exc.error_message},
    )


@app.get("/")
async def root(request: Request, timeframe: int = 30):
    try:
        api = CryptoAPI(days=timeframe)
    except HTTPError as e:
        raise CustomException(error_message="Too many requests, please wait a minute")

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
