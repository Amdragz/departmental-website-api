from django.urls import path
from . import views

urlpatterns = [
  path("users/<matricno>", views.GetUserByMatricNoView.as_view(), name="get-authenticated-user"),
]