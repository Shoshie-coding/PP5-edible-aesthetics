from django.urls import path
from . import views

urlpatterns = [
    path(
        'add/',
        views.newsletter_signup,
        name='newsletter_signup'
        ),
]