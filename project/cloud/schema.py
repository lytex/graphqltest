from django.db.models import F, Value
import graphene
from graphene_django import DjangoObjectType
from .models import User, App
from sqids import Sqids
from django.db.models import F, Value
from django.db.models.functions import Concat, Cast
from django.db.models import CharField

sqids = Sqids(min_length=10)


class UserType(DjangoObjectType):
    class Meta:
        model = User

    def resolve_id(self, info):
        return "u_" + sqids.encode([self.id])


class AppType(DjangoObjectType):
    class Meta:
        model = App

    def resolve_id(self, info):
        return "u_" + sqids.encode([self.id])


class Query(graphene.ObjectType):
    user = graphene.List(UserType)
    app = graphene.List(AppType)

    def resolve_user(self, info, **kwargs):
        return User.objects.all()

    def resolve_app(self, info, **kwargs):
        return App.objects.all()


class UserMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        plan = graphene.String(required=True)

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, plan: str, id: str):
        user = User.objects.get(pk=sqids.decode(id.lstrip("u_"))[0])
        user.plan = plan
        user.save()
        return UserMutation(user=user)


class Mutation(graphene.ObjectType):
    update_question = UserMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
