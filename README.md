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
  4.2. Run via Docker
  ```sh
  docker build -t crypto-correlation .
  docker run -p 8000:80 crypto-correlation
  ```

5. Visit http://localhost:8000


## Deploying 
1. Install the Heroku CLI if not yet installed. Information about installtion can get [here](https://devcenter.heroku.com/articles/heroku-cli).
2. Perform login with the `heroku login` command
3. Create an Heroku app named `cryptocorr` and a remote for the repository.
```sh
heroku git:remote -a crptocorr
```
4. Push source code to a remote
```sh
git push heroku main
```
5. Logout from Heroku CLI (optional)
```sh
heroku logout
```


## License
This repository is distributed under [MIT License](https://github.com/luangtatipsy/crypto-correlation/blob/master/LICENSE)