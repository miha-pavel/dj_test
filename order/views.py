from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from order.serializers import UsersSerializer

User = get_user_model()

class ListUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

class ListRegisterUsers(generics.ListAPIView):
    serializer_class = UsersSerializer
    # filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = User.objects.all()
        registration_date = self.kwargs['registration_date']
        # registration_date = self.request.query_params.get('registration_date', None)
        print('registration_date: ', registration_date)
        return queryset.filter(registration_date=registration_date)
