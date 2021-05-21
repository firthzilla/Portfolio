from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/', views.portfolio_list, name='portfolio'),
    path('post-detail/<int:pk>/', views.get_post, name='post-details'),
]
