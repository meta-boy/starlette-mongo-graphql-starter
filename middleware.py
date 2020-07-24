from starlette.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware
import pymongo
import ssl


class DatabaseMiddleware(BaseHTTPMiddleware):
     async def dispatch(self, request, call_next):
         client = pymongo.MongoClient('mongodb://localhost:27017', ssl_cert_reqs=ssl.CERT_NONE)
         db = client['test']
         request.state.db = db
         response = await call_next(request)
         return response


middleware = [
  Middleware(DatabaseMiddleware)
]

