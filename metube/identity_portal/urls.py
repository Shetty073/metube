from django.urls import path

from .views import signin_view, signout_view, user_view

urlpatterns = [
    path('signin/', signin_view, name='signin'),
    path('signout/', signout_view, name='signout'),
    path('user/', user_view, name='user'),
]