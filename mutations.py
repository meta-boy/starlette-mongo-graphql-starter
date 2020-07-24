import graphene
from models import Person


class CreatePerson(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        age = graphene.Int()

    person = graphene.Field(Person)

    async def mutate(self, info, name, age):
        request = info.context["request"]
        doc = request.state.db.users.insert(
            {
                'name': name,
                'age': age
            }
        )
        print(doc)
        person = Person(name=name, age=age)

        return CreatePerson(person=person)


class Mutations(graphene.ObjectType):
    create_person = CreatePerson.Field()
