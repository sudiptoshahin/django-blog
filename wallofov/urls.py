
from django.urls import path
# from wallofov import views
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    path('about/', views.about, name='about')
]