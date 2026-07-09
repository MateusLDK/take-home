# Take Home

## Requirements

Python version: 3.12+
Pip: 26.0+

## Installation

Install the service dependencies by running:

```
pip install -r requirements.txt
```

If you want to run tests for this project, you should also install the dev dependencies by running:

```
pip install -r requirements-dev.txt
```


## Running locally

Execute the following command:

```
uvicorn src.app:app --reload
```

By default, uvicorn runs on port 8000. if you want to use a different port, add --port xxxx to the command above.


## Running tests

After installing the tests dependencies you can run pytest directly in the project root folder:

```
pytest
```

Unit tests cover the business logic (service and domain layers). The HTTP layer is validated end-to-end by the automated test suite.

## Design decisions

- In-memory storage using dict since durability was explicitly out of scope.
- Business logic is isolated from the HTTP layer; the service returns domain objects and the HTTP layer builds the responses.
- POST /event routes by "type" via dispatch table.
- Domain exceptions are translated to HTTP responses via fastAPI exception handler.

## Testing with curl

```bash
# Get balance
curl "http://localhost:8000/balance?account_id=100"

# Deposit
curl -X POST http://localhost:8000/event \
  -H "Content-Type: application/json" \
  -d '{"type":"deposit","destination":"100","amount":10}'

# Withdraw
curl -X POST http://localhost:8000/event \
  -H "Content-Type: application/json" \
  -d '{"type":"withdraw","origin":"100","amount":5}'
```

Interactive API docs available at `/docs` while the server is running.