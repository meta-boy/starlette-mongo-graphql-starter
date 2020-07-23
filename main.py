from starlette.applications import Starlette
from starlette.routing import Route
from starlette.graphql import GraphQLApp
import graphene


class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))
    bye = graphene.String(name = graphene.String(default_value = "stranger"))

    def resolve_hello(self, info, name):
        return "Hello " + name

    def resolve_bye(self, info, name):
        return "Bye "+ name

routes = [
    Route('/graphql', GraphQLApp(schema=graphene.Schema(query=Query)))
]
app = Starlette(routes=routes)
