from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from app.word import Word

app = FastAPI()

audit_log = []

security = HTTPBasic()


@app.post("/jumble")
def jumble_word(word: Word):
    return {"jumble_word": word.jumble()}


@app.middleware("http")
async def log_calls(request: Request, call_next):
    response = await call_next(request)
    audit_log.append({"url": request.url, "method": request.method})
    return response


@app.get("/audit")
async def get_last_calls(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != "admin" or credentials.password != "secret":
        raise HTTPException(status_code=401, detail="Incorrect login credentials")
    return {"audit_log": audit_log[-10:]}
