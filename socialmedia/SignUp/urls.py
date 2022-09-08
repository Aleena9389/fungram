from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.signup,name='signup'),
    path('sup',views.sup,name='signup_data'),
    path('login', views.login_request, name='login'),
    path('login_request',views.login_request,name="login_request"),
    path('profile',views.profile,name="profile"),
    path('comment',views.comment,name="comment"),
    path('com',views.com,name='comment_data'),
    path('logout', views.logout, name='logout'),


]


