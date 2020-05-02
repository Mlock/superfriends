from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta, timezone

# from apps.core.helpers import get_book_cover_url_from_api, redirect_back
from apps.core.models import Contact
from apps.core.forms import AddContactForm, EditContactForm
from django.db.models.functions import Lower
from apps.accounts.models import User

from django.core.paginator import Paginator


def contact_home(request):
    due_contact_list = get_contacts_due(Contact.objects.filter(creator_user=request.user.id))
    contact_lists = Contact.objects.filter(creator_user=request.user.id).order_by(Lower('last_name'))
    paginator = Paginator(contact_lists, 5)
    countdowns = [get_contact_countdown(c) for c in contact_lists]
    filtered_countdowns = [get_contact_countdown(c) for c in due_contact_list]
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'all_contact_lists': contact_lists,
        'due_contact_list' : due_contact_list,
        'countdowns' : zip(contact_lists, countdowns),
        'filtered_countdowns' : zip(due_contact_list, filtered_countdowns),
        'page_obj': page_obj,
    }
    
    return render(request, 'pages/home.html', context)

# the new view finishes with a redirect to make button work- this one is "contacted" - jMc
@login_required
def update_contacted(request, contact_id): # , frequency modified
    contact = Contact.objects.get(id=contact_id)

    if contact.creator_user == request.user:
        contact.frequency_modified = datetime.now() + timedelta(days=1)
        contact.save()    

    return redirect('/')


    
    #After performing some kind of operation with side effects, like creating or deleting an object, it’s a best practice to redirect to another URL to prevent accidentally performing the operation twice.

# the new view finishes with a redirect to make button work- this one is "snooze" - jMc
# def home_set_snooze(request):

def user_page(request):
    contacts = Contact.objects.order_by(Lower('last_name'))
    contacts_by_user = contacts.filter(creator_user=request.user.id)
    countdowns = [get_contact_countdown(c) for c in contacts_by_user] # add countdown info 
    # this is about what you need on the template to make this work:
    # {% for contact, countdown in filtered_countdowns %}
    # because zip returns a tuple

    paginator = Paginator(contacts_by_user, 5)

    context = {
        'contacts': contacts_by_user,
        'countdowns': zip(contacts_by_user, countdowns),
        'user_on_page': request.user.id,
    }
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'pages/user_page.html', {'page_obj': page_obj})


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
            return redirect('/contact/'+str(contact.id))
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
            # check to see if frequency has changed - jMc
            if form.has_changed() and 'frequency' in form.changed_data:
                contact = form.save(commit=False)
                contact.frequency_modified = datetime.now()
                contact.save()    
            form.save()
            print('this is a test')
            return redirect('/contact/'+str(contact_id))

    else:
        # A GET, create a pre-filled form with the instance.
        form = EditContactForm(instance=contact_to_edit)
        print('this is a different test')

    context = {
        'form': form,
    }
    return render(request, 'pages/edit_contact.html', context)


@login_required
def contact_delete(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    if contact.creator_user == request.user:
        contact.delete()

    return redirect('/')



# jMc bgin
# converts the string that was stored in the DB to a time delta
# TODO frequency is likely best kept as an integer that gets converted to a time delta
# and then there is an alternative option to make the next contact an exact date with a calendar picker
# note: timedelta does not have values for year or month. As for Django DurationField, "on all databases 
#       other than PostgreSQL, comparing the value of a DurationField to arithmetic on 
#       DateTimeField instances will not work as expected", so I went with vanilla Python
def get_interval (frequency):
    
    conversions = {
        'daily' : timedelta(days=1),
        'weekly' : timedelta(days=7),
        'monthly' : timedelta(days=30),
        'quarterly' : timedelta(days=90),
        'yearly' : timedelta(days=365),
        'custom' : timedelta(days=14),
    }
    return conversions[frequency]

# for when intervals are stored as integers
def set_interval (frequency):
    conversions = {     
        'daily' : 1,
        'weekly' : 7,
        'monthly' : 30,
        'quarterly' : 90,
        'yearly' : 365,
        'custom' : 14, # arbitrary number until this is worked out
    }
    return conversions[frequency]

# this function can be used to display countown; it's being used in the filter - jMc
def get_contact_countdown (contact):
    
    reference_date = contact.frequency_modified if contact.frequency_modified is not None else contact.last_modified
    contact_countdown = (get_interval(contact.frequency) + reference_date) - datetime.now(timezone.utc) #will be frequency_modified once DB is updated 
    return contact_countdown.days
    


# write the logic that does the calculation. I need to know what today is vs. last modified + time delta
# for loop that goes through list and then filters
# TODO give the below a second integer input so that user can set their own threshold to be notified
def get_contacts_due(contact_list):
    filtered = []
    for contact in contact_list:
        if get_contact_countdown(contact) <= 3: # && snooze is in the past
            filtered.append(contact)
    return filtered
    #python has built in list filtering
            
# TODO skip function

    # contact due in contact_countdown days
    # render in red if negative #    

#*** add logic to edit_contact that triggers an update to frequency_modified when it's changed
# we don;t actually need tz if everything is relative to utc
# I'd rather save freq as integer

# if you click snooze, time delta would be one day, last modified also updates, snooze adds a day at a time
def save_snooze(): #onclick
    snooze = datetime.now(timezone.utc) + timedelta(days=1)
    return snooze

#jMc pseudo
# if you click contacted, last modified updates to today, time delta stays the same
# you can change time delta at anytime, and it would update last modified
# jMc end




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

# # @login_required
# def hi_friends(request):
#     if request.method == 'GET':
#         contact_lists = Contact.objects.all().order_by(Lower('last_name'))
#         for contact_lists:
#             reminder = contact_lists.frequency
#             x = reminder
#             contact_date = x - 1
#             if contact_date == 0:
#  context = {
#         'contact_list': contact_lists,
#         # 'all_friends': contacts,
#     }
#     return render(request, 'pages/home.html', context)

# # look at contact method
# def snooze(request, contact_id): 
#     Contact.frequncy += 1

# look at twitten (like the editing is snooze)

# def hi_friends(request):
#     if request.method == 'GET':
#         contact_list = Contact.objects.all().order_by(Lower('last_name'))

#         if contact_list.frequency


             
        

