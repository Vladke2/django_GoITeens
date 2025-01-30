from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView)
from user_drf.models import Users
from user_drf.serializer import UsersSerializer
from rest_framework.views import APIView


class UserListCreateAPIView(ListCreateAPIView):
    serializer_class = UsersSerializer
    queryset = Users.objects.all()


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UsersSerializer
    queryset = Users.objects.all()


class FilteredUserListAPIView(ListAPIView):     #Варіант 1
    serializer_class = UsersSerializer

    def get_queryset(self):
        queryset = Users.objects.all()
        age = self.request.query_params.get('age', None)
        name = self.request.query_params.get('name', None)

        if age:
            queryset = queryset.filter(age=age)
        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class AdultUserListAPIView(ListAPIView):     #Варіант 2
    serializer_class = UsersSerializer
    queryset = Users.objects.filter(age__gte=18)
