from django.urls import path,include
from person import views

urlpatterns = [
    
    path('add/', views.person_create_view, name='person_add'),
    path('<int:pk>/', views.person_update_view, name='person_change'),
    
    
    path('ajax/load_division/', views.load_division, name='ajax_load_division'), # AJAX
    path('ajax/load_subdivision/', views.load_subdivision, name='ajax_load_subdivision'), # AJAX
]