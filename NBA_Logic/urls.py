from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

# Note that 'home was the name of the function, but I could change this to whatever I liked

