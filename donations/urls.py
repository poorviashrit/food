from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.FoodBridgeLoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_page, name='logout'),
    path('donate/', views.create_donation, name='create_donation'),
    path('<int:pk>/claim/', views.claim_donation, name='claim_donation'),
    path('<int:pk>/collected/', views.mark_collected, name='mark_collected'),
    path('<int:pk>/delete/', views.delete_donation, name='delete_donation'),
]
