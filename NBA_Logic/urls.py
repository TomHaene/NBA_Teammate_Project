from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('returnResults',views.returnResults, name='returnResults'),
    path('testing',views.testing, name='testing'),
    path('goBack',views.goBack, name='goBack')

]

# Note that 'home was the name of the function, but I could change this to whatever I liked

