from fastapi import FastAPI

app = FastAPI()

# Import routes
from app.routes import payment_routes, fare_routes

app.include_router(payment_routes.router)
app.include_router(fare_routes.router)

@app.get("/")
def read_root():
    return {"message": "Payment Service API"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "payment-service"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
