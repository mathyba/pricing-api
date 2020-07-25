# pricing-api
This pricing API provides the current price for a given financial instrument

## Setup
`git clone https://github.com/mathyba/pricing-api.git`

in `api.py`, replace the example Yahoo Finance API Key with your own.

Then, in the virtual environment shell, run `python pricing_app.py`


# Via a virtual environment

Before running the app, you should set up a virtual environment in the git repository, and use the requirements.txt to install the dependencies.

If you need to set up a virtual environment, here is a suggested course of action using Pipenv: 
- If necessary, install Pipenv: `pip install --user pipenv`
- Create virtual environment with dependencies: `pipenv install -r requirements.txt`
- Launch the virtual environment shell: `pipenv shell`
- Run the API: `python api.py`

Then, in the virtual environment shell, run `python api.py`


## Usage

### Required parameters

- "symbol": the stock symbol (ex: "CAT" for Caterpillear Inc)
Unkown stock symbols will yield a response with 404 request status and error message


### Making a call to the API

As the API currently supports only the GET method, parameter key and value must be included in the URL
Any other argument than required parameter(s) listed above will be ignored.

Example of a valid request:
`curl -i -H "Content-Type: application/json" "http://localhost:5000/?symbol=IBM"`

A valid request with a known instrument symbol will return a json with symbol, price and currency.
- If the symbol argument is not in the URL, response will include an error message.
- If the symbol is present but unknown, response will be an empty dict.


## Testing

A test suite is available to test the API: run `pytest` either in your virtual environment or docker container

In case of issues with imports, make sure the API's path is in your PYTHONPATH!
`export PYTHONPATH+=":/path/to/the/git/repo"`
