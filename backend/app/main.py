from fastapi import FastAPI
from app.api import routes

app = FastAPI()

# Include your API routes
app.include_router(routes.router)

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # frontend dev port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Agent Patches Backend is Live!"}
