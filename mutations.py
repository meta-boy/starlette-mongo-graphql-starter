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


class UpdatePerson(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        age = graphene.Int()

    person = graphene.Field(Person)

    async def mutate(self, info, name, age):
        request = info.context['request']
        doc = request.state.db.users
        doc.update_one({'name': name}, {'$set': {'age': age}})
        person = Person(name=name, age=age)

        return UpdatePerson(person=person)


class DeletePerson(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    person = graphene.Field(Person)

    async def mutate(self, info, name):
        request = info.context['request']
        documents = request.state.db.users
        
        doc = documents.find_one_and_delete({
            'name': name
        })
        person = Person(name=name, age=doc['age'])
        return DeletePerson(person=person)


class Mutations(graphene.ObjectType):
    create_person = CreatePerson.Field()
    update_person = UpdatePerson.Field()
    delete_person = DeletePerson.Field()