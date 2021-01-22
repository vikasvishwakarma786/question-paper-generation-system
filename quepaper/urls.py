
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('add_question', views.add_question, name='add_question'),
    path("login_request", views.login_request, name="login_request"),
    path("logout_request", views.logout_request, name="logout"),
    path("login_view", views.login_view, name='login_view'),
    path("registration_view", views.registration_view, name='registration_view'),
    path("registration_request", views.registration_request, name='registration_request'),
    path("createqpaper", views.createqpaper, name='createqpaper'),
    path("add_question_request", views.add_question_request, name='add_question_request'),
    path("show_question", views.show_question, name='show_question'),
    path("create_request", views.create_request, name='create_request'),

]
