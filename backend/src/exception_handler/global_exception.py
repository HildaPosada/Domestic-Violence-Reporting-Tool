from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


class NotFoundException(Exception):
    def __init__(self, status_code: int, message: str):
        self.message = message
        self.status_code = status_code


async def global_exception_handler(request: Request, ex: Exception):
    if isinstance(ex, NotFoundException):
        return JSONResponse(
            status_code=ex.status_code,
            content={
                "error": True,
                "message": ex.message
            }
        )
    
   
    return JSONResponse(
        status_code=500,
        content={
            "error": True,
            "message": "An unexpected error occured, our team is on it."
        }
    )