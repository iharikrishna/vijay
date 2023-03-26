from fastapi import FastAPI, Request, Response, status
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Create the FastAPI app
app = FastAPI(
    title="Vijay Appliance API",

    version="0.0.1",
    openapi_url="/api/v0.1/vijay.json",
    docs_url="/docs",

)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/hello/", status_code=201)
def helloWorld(request: Request, response: Response):
    return {"message": "Hello World from the Application"}


@app.get("/", status_code=201)
def helloWorld(request: Request, response: Response):
    return {"message": "Hello World from the Application root"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")