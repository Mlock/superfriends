from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from apps.core.helpers import get_book_cover_url_from_api, redirect_back
from apps.core.models import Contact
from apps.core.forms import AddContactForm
from django.db.models.functions import Lower


def contact_home(request):
    contact_lists = Contact.objects.all().order_by(Lower('last_name'))
    context = {
        'all_contact_lists': contact_lists,
    }
    return render(request, 'pages/home.html', context)

def contact_details(request, contact_id):
    contact_list_requested = Contact.objects.get(id=contact_id)
    # contacts = IndividualContact.objects.filter(contact_list=contact_list_requested)
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
            form = AddContactForm()
        context = {
            'form': form,
        }
        return render(request, 'pages/form_page.html', context)
            # Contact.objects.create(
            #     first_name=form.cleaned_data['first_name'],
            #     last_name=form.cleaned_data['last_name'],
            #     email=form.cleaned_data['email'],
            #     picture=form.cleaned_data['picture'],
            #     phone=form.cleaned_data['phone'],
            #     address=form.cleaned_data['address'],
            #     birthday=form.cleaned_data['birthday'],
            #     notes=form.cleaned_data['notes'],
            #     type=form.cleaned_data['type'],
            #     frequency=form.cleaned_data['frequency'],
            #     linkedin=form.cleaned_data['linkedin'],
            #     facebook=form.cleaned_data['facebook'],
            #     instagram=form.cleaned_data['instagram'],
            #     twitter=form.cleaned_data['twitter'],
            #     creator_user=logged_in_user,
            # )
            # return redirect('/')
    else:
        form = AddContactForm()
    context = {
        'form': form,
    }
    return render(request, 'pages/form_page.html', context)


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

