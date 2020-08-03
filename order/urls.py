from django.urls import path, re_path

from . import views


app_name = 'order'

urlpatterns = [
    path(r'list_users/', views.ListUsers.as_view(), name='List_users'),
    re_path(r'^list_register_users/(?P<registration_date>.+)/$', views.ListRegisterUsers.as_view(), name='List_register_users'),
]