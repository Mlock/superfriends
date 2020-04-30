from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import datetime

from apps.core.helpers import get_book_cover_url_from_api, redirect_back
from apps.core.models import Contact
from apps.core.forms import AddContactForm, EditContactForm
from django.db.models.functions import Lower


def contact_home(request):
    contact_lists = Contact.objects.all().order_by(Lower('last_name'))
    context = {
        'all_contact_lists': contact_lists,
    }
    return render(request, 'pages/home.html', context)

def contact_details(request, contact_id):
    contact_list_requested = Contact.objects.get(id=contact_id)
    context = {
        'contact_list': contact_list_requested,
    }
    return render(request, 'pages/details.html', context)

@login_required
def contact_create(request):
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        form = AddContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.creator_user = request.user
            contact.save()
            return redirect('/')
        else:
            context = {
                'form': form,
            }
            return render(request, 'pages/form_page.html', context)
    else:
        form = AddContactForm()
    context = {
        'form': form,
    }
    return render(request, 'pages/form_page.html', context)

def edit_contact(request, contact_id):
    # Get the contact we are looking for

    contact_to_edit = Contact.objects.get(id=contact_id)

    if request.method == 'POST':

        # Create a form instance and populate it with data from the request
        form = EditContactForm(request.POST, request.FILES, instance=contact_to_edit)

        if form.is_valid():
            form.save()
            print('this is a test')
            return redirect('/')

    else:
        # A GET, create a pre-filled form with the instance.
        form = EditContactForm(instance=contact_to_edit)
        print('this is a different test')

    context = {
        'form': form,
    }
    return render(request, 'pages/edit_contact.html', context)

# def reminder():
#     days = 1
#     week = 7
#     month = 30
#     reminder = days * input(int)
#     snooze = days + 1

@login_required
def contact_delete(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    if contact.creator_user == request.user:
        contact.delete()

    return redirect('/')


# @login_required
# def friend_list_create_book(request, friend_id):
#     # C in CRUD --- CREATE books in database
#     friend_list_requested = Contact.objects.get(id=friend_id)

#     # BONUS SOLUTION:
#     # Prevent users who are not the requested user from accessing this
#     if friend_list_requested.creator_user != request.user:
#         return redirect_back(request)

#     if request.method == 'POST':
#         # Create a form instance and populate it with data from the request
#         form = AddBookForm(request.POST)
#         if form.is_valid():

#             url = get_book_cover_url_from_api(form.cleaned_data['title'])

#             Book.objects.create(
#                 title=form.cleaned_data['title'],
#                 description=form.cleaned_data['description'],
#                 # SOLUTION:
#                 friend_list=friend_list_requested,
#                 cover_url=url,
#             )
#             # Redirect back to the reading list we were at
#             return redirect('/list/' + str(friend_list_requested.id) + '/')
#     else:
#         # if a GET  we'll create a blank form
#         form = AddFriendForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'pages/form_page.html', context)


# @login_required
# def friend_list_delete_book(request, book_id):
#     # D in CRUD, increase the votes count
#     book = Book.objects.get(id=book_id)

#     # BONUS SOLUTION: Security
#     if book.friend_list.creator_user == request.user:
#         book.delete()

#     return redirect_back(request)

# @login_required
# def friend_list_vote_up(request, contact_id):
#     # U in CRUD, increase the votes count
#     friend_list = FriendList.objects.get(id=contact_id)

#     # BONUS SOLUTION:
#     # Get the currently logged in user
#     logged_in_user = request.user
#     user_who_voted = friend_list.users_who_voted.filter(id=logged_in_user.id)
#     if not user_who_voted.exists():
#         print('can vote')
#         friend_list.votes = friend_list.votes + 1
#         # Record that this user has already voted on this reading list
#         friend_list.users_who_voted.add(logged_in_user)
#         friend_list.save()

#     return redirect_back(request)

# @login_required
# def friend_list_vote_down(request, contact_id):
#     # U in CRUD, decrease the votes count
#     friend_list = FriendList.objects.get(id=contact_id)

#     # BONUS SOLUTION:
#     logged_in_user = request.user
#     user_who_voted = friend_list.users_who_voted.filter(id=logged_in_user.id)
#     if not user_who_voted.exists():
#         print('can vote')
#         friend_list.votes = friend_list.votes - 1
#         # Record that this user has already voted on this reading list
#         friend_list.users_who_voted.add(logged_in_user)
#         friend_list.save()
#     return redirect_back(request)

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


