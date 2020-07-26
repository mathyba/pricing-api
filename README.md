# pricing-api
This pricing API provides the current price for a given financial instrument

## Set-up
`git clone https://github.com/mathyba/pricing-api.git`

in `api.py`, replace the example Yahoo Finance API Key with your own.

### --> with Docker

I am assuming you have Docker installed. If not, you can find instructions for your system in the official documentation: https://docs.docker.com/engine/install/

- Build the docker image: `sudo docker build . -t pricing-api`
- Run the container: `sudo docker run --name "pricing-api" -v $(pwd):/api -p 5000:5000 -t pricing-api`

Side notes: 
- Anything running on the container's 5000 port will be available on localhost 5000 port
- Any changes you make to the code will be available in the container, which will lead the API to restart
- For access to the server logs: `docker logs pricing-api -f`
- For direct access within the container, most likely for debugging purposes: `docker exec -ti pricing-api /bin/sh `

### --> with a virtual environment

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

### --> in your container
run `docker exec -t pricing-api python3 -m pytest`

### --> in a virtual env
run `pytest`

In case of issues with imports, make sure the API's path is in your PYTHONPATH!
`export PYTHONPATH+=":/path/to/the/git/repo"`
