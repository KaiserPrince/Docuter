from django.urls import path
from . import views  # Import your app's views

urlpatterns = [
    path("create-question/", views.create_question, name="create_question"),
    path("generate-docs/", views.generate_document, name="generate_document"),
]
