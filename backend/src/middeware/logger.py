from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

class LogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        print(f"Incoming request: {request.method} {request.url}")
        response = await call_next(request)
        print(f"Response headers: {response.headers}")
        return response