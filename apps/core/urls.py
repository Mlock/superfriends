from django.urls import path

from apps.core import views

urlpatterns = [
    # CRUD views for ReadingLists
    path('', views.friend_list_home, name="home"),
    path('friend/<int:friend_id>/', views.friend_list_details),
    path('friend/create/', views.friend_list_create),
    path('friend/delete/<int:friend_id>/', views.friend_list_delete),
    path('dashboard/', views.user_dashboard, name="dashboard")

    # # CRUD views for editing Books within ReadingLists
    # path('friend-create/<int:friend_id>/', views.friend_list_create_book),
    # path('friend-delete/<int:book_id>/', views.friend_list_delete_book),

    # CRUD views for voting on ReadingLists
#     path('friend/<int:friend_id>/vote/up/', views.friend_list_vote_up),
#     path('friend/<int:friend_id>/vote/down/', views.friend_list_vote_down),
]
