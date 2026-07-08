# Take Home

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



Built using Python 3.14