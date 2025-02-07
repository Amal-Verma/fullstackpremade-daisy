from fastapi import FastAPI
from routes import userRoute
from auth import jwt_encode,jwt_decode
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict,List
app=FastAPI()

allowed_origin=["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origin,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(userRoute.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
