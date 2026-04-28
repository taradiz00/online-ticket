from fastapi import FastAPI, Depends, Response, status
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarlettHttpexception 
from fastapi.exceptions import RequestValidationError
from app.routers.users import route_airports, route_users, route_flights, route_reservations, route_ticket, route_passengers, route_forget_passw
from app.auth.token_auth import get_authenticated_user
from contextlib import asynccontextmanager

tags_metadata = [
    {
        "name": "flights",
        "description": "Operations related to flights",
        "externalDocs": {
            "description": "More about flights",
            "url": "https://example.com/docs/flights"
        }
    }
]



@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application startup")
    yield
    print("Application shutdown")

app = FastAPI(title="Airport API", version="0.128.0", lifespan=lifespan, openapi_tags=tags_metadata)

app.include_router(route_airports.router)
app.include_router(route_users.router)
app.include_router(route_flights.router)
app.include_router(route_reservations.router)
app.include_router(route_ticket.router)
app.include_router(route_passengers.router)
app.include_router(route_forget_passw.router)





@app.get("/private")
def private_root(user = Depends(get_authenticated_user)):
    print(user)
    return {"message": "This is a private route"}


@app.get("/set-coockie")
def set_cookie(response:Response):
    response.set_cookie(key="test", value="something")
    return {"message": "cookie has been set successfully"}


@app.exception_handler(StarlettHttpexception)
async def http_exception_handler(request, exc):
    print(exc.__dict__)
    error_response = {
        "error": True,
        "status_code": exc.status_code,
        "detai": str(exc.detail)
    }
    return JSONResponse(status_code=exc.status_code, content=error_response)


@app.exception_handler(RequestValidationError)
async def http_validation_exception_handler(request, exc):
    print(exc.__dict__)
    error_response = {
        "error": True,
        "status_code": status.HTTP_422_UNPROCESSABLE_CONTENT,
        "detai": "There was a problem with your form request",
        "content": exc.errors()
    }
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, content=error_response)


