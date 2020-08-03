from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from order.serializers import UsersSerializer

User = get_user_model()


class ListUsers(generics.ListAPIView):
    serializer_class = UsersSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        registration_date = self.kwargs.get('registration_date', None)
        if registration_date is not None:
            queryset = queryset.filter(registration_date=registration_date)
        return queryset
