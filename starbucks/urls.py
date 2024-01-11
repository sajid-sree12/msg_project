from django.urls import path
from starbucks import views
urlpatterns = [
    path("todo",views.home,name='home'),
    path("sd",views.get_coffees,name="get_coffees"),
    path("",views.one_coffee,name="one_coffee"),
    path("coffee/<int:pk>",views.coffee,name="coffee"),
    path("users",views.get_users,name="users")
]