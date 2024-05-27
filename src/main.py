from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

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
