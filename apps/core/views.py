from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import datetime

from apps.core.helpers import get_book_cover_url_from_api, redirect_back
from apps.core.models import IndividualContact, Contact
from apps.core.forms import AddFriendForm, AddContactForm
from django.db.models.functions import Lower


def contact_home(request):
    contact_lists = Contact.objects.all().order_by(Lower('last_name'))
    context = {
        'all_contact_lists': contact_lists,
    }
    return render(request, 'pages/home.html', context)

def contact_details(request, contact_id):
    contact_list_requested = Contact.objects.get(id=contact_id)
    contacts = IndividualContact.objects.filter(contact_list=contact_list_requested)
    context = {
        'contact_list': contact_list_requested,
        'all_friends': contacts,
    }
    return render(request, 'pages/details.html', context)

@login_required
def contact_create(request):
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        form = AddContactForm(request.POST, request.FILES)
        if form.is_valid():
            logged_in_user = request.user

            Contact.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                picture=form.cleaned_data['picture'],
                phone=form.cleaned_data['phone'],
                address=form.cleaned_data['address'],
                birthday=form.cleaned_data['birthday'],
                notes=form.cleaned_data['notes'],
                type=form.cleaned_data['type'],
                frequency=form.cleaned_data['frequency'],
                creator_user=logged_in_user,
            )
            return redirect('/')
    else:
        form = AddContactForm()
    context = {
        'form': form,
    }
    return render(request, 'pages/form_page.html', context)

<<<<<<< HEAD
=======


>>>>>>> master
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


# @login_required
# @login_required
# def user_dashboard(request):
#     context={

#     }
#     return render(request, 'pages/dashboard.html', context)
# @login_required
# def snooze(request, friend_id):
    

#     return redirect('/')

# @login_required
def hi_friends(request):
    if request.method == 'GET':
        contact_lists = Contact.objects.all().order_by(Lower('last_name'))
        for contact_lists:
            reminder = contact_lists.frequency
            x = reminder
            contact_date = x - 1
            if contact_date == 0:
 context = {
        'contact_list': contact_lists,
        # 'all_friends': contacts,
    }
    return render(request, 'pages/home.html', context)

# look at contact method
def snooze(request, contact_id): 
    Contact.frequncy += 1

# look at twitten (like the editing is snooze)

# def hi_friends(request):
#     if request.method == 'GET':
#         contact_list = Contact.objects.all().order_by(Lower('last_name'))

#         if contact_list.frequency


             
        

