from django.urls import path
from . import views

urlpatterns = [
  path("users/documents/", views.DocumentViewSet.as_view(), name="get-documents"),
  path("users/resources/", views.ResourceViewSet.as_view(), name="get-resources"),
  path("users/courses/", views.CourseViewSet.as_view(), name="get-courses"),
  path("users/notifications/", views.NotificationViewSet.as_view(), name="get-notifications"),
  path("users/<user_id>/", views.GetUserByMatricNoView.as_view(), name="get-authenticated-user"),
]