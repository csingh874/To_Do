from django.urls import path
from . import views

urlpatterns = [
    path("",views.user_login,name="login"),
    path("logi/",views.user_logout,name="logout"),
    path("sign-up/",views.user_register,name="register"),
    path("home/", views.user_home, name="home"),
    path("password-change/", views.pass_change, name="password-change"),
    path("update/<str:pk>/",views.task_update,name="update"),
    path("delete/<str:pk>/",views.task_delete,name="delete"),
]