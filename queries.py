import graphene
from models import Person

class Query(graphene.ObjectType):
    people = graphene.List(Person)

    async def resolve_people(self, info):
        persons = []
        request = info.context["request"]
        data = request.state.db.users

        for doc in data.find():
            persons.append(
                Person(name=doc['name'], age=doc['age'])
            )
        return persons


