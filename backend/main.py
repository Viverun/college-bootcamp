from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()  # This MUST be named 'app' for your command to work

# Add this now so your React frontend can talk to it later
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # We'll narrow this down to http://localhost:5173 later
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "FastAPI is officially running!"}