from django.urls import path
from . import views

urlpatterns = [
    path('hello/',views.hello_world),
    path('greet/<str:name>/',views.say_my_name),
    path('age/<int:age>/',views.guess_my_age),
    path('info/<str:name>/<int:age>/',views.guess_my_info),

]

