from django.urls import path

from apps.core import views

urlpatterns = [
    # CRUD views for ReadingLists
    path('', views.contact_home, name="home"),
    path('contact/<int:contact_id>/', views.contact_details),
    path('contact/create/', views.contact_create),
    path('contact/delete/<int:contact_id>/', views.contact_delete),
    path('contact/edit/<int:contact_id>/', views.edit_contact),

    # # CRUD views for editing Books within ReadingLists
    # path('friend-create/<int:friend_id>/', views.friend_list_create_book),
    # path('friend-delete/<int:book_id>/', views.friend_list_delete_book),

    # CRUD views for voting on ReadingLists
#     path('friend/<int:friend_id>/vote/up/', views.friend_list_vote_up),
#     path('friend/<int:friend_id>/vote/down/', views.friend_list_vote_down),

]
