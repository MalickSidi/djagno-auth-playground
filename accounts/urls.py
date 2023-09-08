from django.urls import path
from .views import signup, profile

app_name = 'accounts'

urlpatterns = [
    path("signup", view=signup, name='signup'),
    path("profile", view=profile, name='profile'),
]
