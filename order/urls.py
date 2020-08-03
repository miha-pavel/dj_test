from django.urls import path, re_path

from . import views


app_name = 'order'

urlpatterns = [
    path(r'list_users/', views.ListUsers.as_view(),
        name='api_v1_list_users'),
    re_path(r'^list_users/(?P<registration_date>.+)/$', views.ListUsers.as_view(),
        name='api_v1_list_register_users'),
]