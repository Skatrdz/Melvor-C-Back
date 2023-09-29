from django.urls import path
from . import views
urlpatterns = [
     path('TokenView/', views.TokenView.as_view(), name='TokenView'),
     path('logout/', views.LogoutView.as_view(), name='logout')
]