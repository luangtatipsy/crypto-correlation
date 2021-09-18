# Cryptocurrency Price Correlation
A single page website for display correlation chart of top 30 cryptocurrencies ranked by Market Cap.

URL: https://cryptocorr.herokuapp.com/

## Prerequisites
- Git
- Python >= 3.8

## Setup
0. Clone the repository
```sh
git clone https://github.com/luangtatipsy/crypto-correlation.git
cd crypto-correlation
```
1. Create and activate a virtual environment for Python _(recommended)_. If you do not prefer using a virtual environment, skip to step 4.
```sh
python -m venv env
source env/bin/activate
```
2. Update pip to latest version
```sh
python -m pip install --upgrade pip
```
3. Install requirements
```sh
python -m pip install -r requirements.txt
```
4. Run the website
  4.1. Run via `uvicorn`
  ```sh
  cd app
  uvicorn main:app --reload
  ```
  4.1. Run via Docker
  ```sh
  docker build -t crypto-correlation .
  docker run -p 8000:80 crypto-correlation
  ```

5. Visit http://localhost:8000

## License
This repository is distributed under [MIT License](https://github.com/luangtatipsy/crypto-correlation/blob/master/LICENSE)