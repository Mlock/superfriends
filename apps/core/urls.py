from django.urls import path

from apps.core import views

urlpatterns = [
    path('', views.contact_home, name="home"),
    path('contact/<int:contact_id>/', views.contact_details),
    path('contact/create/', views.contact_create),
    path('contact/delete/<int:contact_id>/', views.contact_delete),
    path('contact/edit/<int:contact_id>/', views.edit_contact),
    path('users/', views.user_page, name="user_page"),
]
