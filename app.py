from graphql.execution.executors.asyncio import AsyncioExecutor
from starlette.responses import JSONResponse
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.graphql import GraphQLApp
import graphene
from middleware import middleware
from queries import Query
from mutations import Mutations

routes = [
    Route('/', JSONResponse({'hello': 'world'})),
    Route('/graphql', GraphQLApp(
        schema=graphene.Schema(query=Query, mutation=Mutations),
        executor_class=AsyncioExecutor
    ))
]
app = Starlette(routes=routes, middleware=middleware)
