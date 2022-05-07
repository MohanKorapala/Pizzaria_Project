from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

app_name = 'MainApp'

urlpatterns = [
    path('',views.index, name='index'),
    path('pizzas',views.pizzas, name='pizzas'),
    path('pizza/<int:pizza_id>/',views.pizza, name='pizza'),
    path('comments/<int:pizza_id>/', views.comments, name='comments'),
]

urlpatterns += staticfiles_urlpatterns()