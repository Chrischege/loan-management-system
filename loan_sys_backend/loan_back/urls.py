# add the url paths for the views
from django.urls import path
from . import views

app_name = 'loan_back'
urlpatterns = [
    path('', views.base_view, name='base'),
    path('loan/', views.loan_view, name='loan'),
    path('users/', views.users_view, name='users'),
    path('borrowers/', views.borrowers_view, name='borrowers'),
    path('applications/', views.applications_view, name='applications'),
]
