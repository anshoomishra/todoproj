from django.urls import path
from account.views import UserCreateView,UserLoginView
from django.contrib.auth.views import LogoutView
app_name = "account"
urlpatterns = [
    path("sign-up/",UserCreateView.as_view(),name="sign-up"),
    path("logout/",LogoutView.as_view(),name="logout"),
    path("login/",UserLoginView.as_view(),name="login")

]

