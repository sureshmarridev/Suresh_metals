from django.urls import path

from. import views

urlpatterns= [
    path('metals/', views.index, name='index'),
    path('', views.empty, name='empty'),
    path('login/', views.login, name='login'),
    path('summary/', views.summary, name='summary'),
]