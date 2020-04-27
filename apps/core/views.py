from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import datetime

from apps.core.helpers import get_book_cover_url_from_api, redirect_back
from apps.core.models import Friend, FriendList
from apps.core.forms import AddFriendForm, AddFriendListForm


def friend_list_home(request):
    # R in CRUD --- READ ReadingLists from database
    # Using order_by('-votes') we'll get it with most votes on top

    friend_lists = FriendList.objects.all().order_by('-votes')
    hi_friends = FriendList.objects.all().order_by('-votes')

    context = {
        'hi_friends': hi_friends,
        'all_friend_lists': friend_lists,
    }
    return render(request, 'pages/home.html', context)

def friend_list_details(request, friend_id):
    # R in CRUD --- READ a single ReadingList & its books from database
    friend_list_requested = FriendList.objects.get(id=friend_id)
    # SOLUTION:
    friends = Friend.objects.filter(friend_list=friend_list_requested)
    context = {
        'friend_list': friend_list_requested,
        'all_friends': friends,
    }
    return render(request, 'pages/details.html', context)

@login_required
def friend_list_create(request):
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        form = AddFriendListForm(request.POST)
        if form.is_valid():
            # C in CRUD --- CREATE reading list in database

            # SOLUTION:
            logged_in_user = request.user
            # print('Current user:', logged_in_user)

            FriendList.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                address=form.cleaned_data['address'],
                birthday=form.cleaned_data['birthday'],
                notes=form.cleaned_data['notes'],
                type=form.cleaned_data['type'],
                frequency=form.cleaned_data['frequency'],
                # SOLUTION:
                creator_user=logged_in_user,
            )
            return redirect('/')
    else:
        # if a GET  we'll create a blank form
        form = AddFriendListForm()
    context = {
        'form': form,
    }
    return render(request, 'pages/form_page.html', context)


# def reminder():
#     days = 1
#     week = 7
#     month = 30
#     reminder = days * input(int)
#     snooze = days + 1

@login_required
def friend_list_delete(request, friend_id):
    # D in CRUD --- DELETE reading list from database
    friendlist = FriendList.objects.get(id=friend_id)

    # BONUS: Security
    if friendlist.creator_user == request.user:
        friendlist.delete()

    return redirect('/')


@login_required
def friend_list_create_book(request, friend_id):
    # C in CRUD --- CREATE books in database
    friend_list_requested = FriendList.objects.get(id=friend_id)

    # BONUS SOLUTION:
    # Prevent users who are not the requested user from accessing this
    if friend_list_requested.creator_user != request.user:
        return redirect_back(request)

    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        form = AddBookForm(request.POST)
        if form.is_valid():

            url = get_book_cover_url_from_api(form.cleaned_data['title'])

            Book.objects.create(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                # SOLUTION:
                friend_list=friend_list_requested,
                cover_url=url,
            )
            # Redirect back to the reading list we were at
            return redirect('/list/' + str(friend_list_requested.id) + '/')
    else:
        # if a GET  we'll create a blank form
        form = AddFriendForm()
    context = {
        'form': form,
    }
    return render(request, 'pages/form_page.html', context)


@login_required
def friend_list_delete_book(request, book_id):
    # D in CRUD, increase the votes count
    book = Book.objects.get(id=book_id)

    # BONUS SOLUTION: Security
    if book.friend_list.creator_user == request.user:
        book.delete()

    return redirect_back(request)

@login_required
def friend_list_vote_up(request, friend_id):
    # U in CRUD, increase the votes count
    friend_list = FriendList.objects.get(id=friend_id)

    # BONUS SOLUTION:
    # Get the currently logged in user
    logged_in_user = request.user
    user_who_voted = friend_list.users_who_voted.filter(id=logged_in_user.id)
    if not user_who_voted.exists():
        print('can vote')
        friend_list.votes = friend_list.votes + 1
        # Record that this user has already voted on this reading list
        friend_list.users_who_voted.add(logged_in_user)
        friend_list.save()

    return redirect_back(request)

@login_required
def friend_list_vote_down(request, friend_id):
    # U in CRUD, decrease the votes count
    friend_list = FriendList.objects.get(id=friend_id)

    # BONUS SOLUTION:
    logged_in_user = request.user
    user_who_voted = friend_list.users_who_voted.filter(id=logged_in_user.id)
    if not user_who_voted.exists():
        print('can vote')
        friend_list.votes = friend_list.votes - 1
        # Record that this user has already voted on this reading list
        friend_list.users_who_voted.add(logged_in_user)
        friend_list.save()
    return redirect_back(request)

# # Psuedo code
# if New friend added to friend_list, 
# Set reminder to contact friend in 7 days
# if snooze is selected, set reminder to contact friend in 24 hours

# @login_required
# def contact_friend(request, friend_id):
#     new_friend = friend_list.objects.get(id=list_id)



@login_required
def user_dashboard(request):
    context={

    }
    return render(request, 'pages/dashboard.html', context)
# @login_required
# def snooze(request, friend_id):
    

#     return redirect('/')


