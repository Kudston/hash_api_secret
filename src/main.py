from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi import Query

import hmac
import hashlib
import uuid

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"]
)

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts = "*"    
)

@app.get("/")
async def home():
    return {"detail":"welcome"}

@app.get("/hash_string")
async def hash_text(
    payload: str=Query(
    "", description="Enter the plain text you would love to hash."),
    secret_key: str = Query(
        "", description="Enter the Secret value you would love to use.")
    ):
    """Currently it only hashes to a 32 bit length, if need be it can be extended later."""
    hash = hmac.new(bytes(secret_key, "utf-8"), payload.encode("utf-8"), hashlib.sha256)

    signature = hash.hexdigest()
    return {"detail":signature}
