from graphene import(
     ObjectType,
     String,
     Int,
     Field,
     Schema,
     List
)

from models import data



"""
    class PersonType:
        email:str
        first_name:str
        last_name:str
        age:int

"""

class PersonType(ObjectType):
    email=String()
    first_name=String()
    last_name=String()
    age=Int()

    #resolvers
    def resolve_email(person,info):
        return person.email

    def resolve_first_name(person,info):
        return person.first_name

    def resolve_last_name(person,info):
        return person.last_name


    def resolve_age(person,info):
        return person.age

class Query(ObjectType):
    all_people=List(PersonType)
    person=Field(PersonType,key=Int())

    def resolve_all_people(root,info):
        return data.values()

    def resolve_person(root,info,key):
        return data[key]

#schema
schema=Schema(query=Query)


# #query
# query_string="{allPeople{email lastName}}"

# print(schema.execute(query_string))