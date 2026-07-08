from fastapi import (
    FastAPI,
)
from fastapi.responses import JSONResponse

from src.services.account_service import AccountService

app = FastAPI(title="Take Home Assignment", description="Ebanx Take Home Assignment")
service = AccountService()


def _account_response_json(account):
    return {
        "id": account.account_id,
        "balance": account.balance,
    }


def deposit_event(event):
    account = service.deposit(event["destination"], event["amount"])
    return {"destination": _account_response_json(account)}


def withdraw_event(event):
    account = service.withdraw(event["origin"], event["amount"])
    return {"origin": _account_response_json(account)}


def transfer_event(event):
    from_account, to_account = service.transfer(
        event["origin"], event["destination"], event["amount"]
    )
    return {
        "origin": _account_response_json(from_account),
        "destination": _account_response_json(to_account),
    }


EVENT_HANDLERS = {
    "deposit": deposit_event,
    "withdraw": withdraw_event,
    "transfer": transfer_event,
}


@app.get("/balance")
async def get_balance(account_id: str):
    account = service.get_balance(account_id)
    if account is None:
        return JSONResponse(status_code=404, content=0)
    return account.balance


@app.post("/event")
async def event_handler(event: dict):
    handler = EVENT_HANDLERS[event["type"]]
    if handler is None:
        return JSONResponse(status_code=404, content=0)
    return JSONResponse(status_code=201, content=handler(event))
