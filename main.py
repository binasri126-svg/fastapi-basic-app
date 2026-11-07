from fastapi import FastAPI

# Create the FastAPI app
app = FastAPI()


# Home page
@app.get("/")
def home():
    return {"message": "Hello, FastAPI"}


# Greet a person using their name
@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}