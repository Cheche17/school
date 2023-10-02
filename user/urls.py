from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('account/', views.account, name='account'),
    path('favourite/', views.favourite, name='favourite'),
    path('invite/', views.invite, name='invite'),
    path('profile/', views.profile, name='profile'),
    path('landlord/', views.landlord, name='landlord'),
    path('manager/', views.Manager, name='manager'),
]