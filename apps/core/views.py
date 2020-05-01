from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import datetime

# from apps.core.helpers import get_book_cover_url_from_api, redirect_back
from apps.core.models import Contact
from apps.core.forms import AddContactForm, EditContactForm
from django.db.models.functions import Lower
from apps.accounts.models import User

from django.core.paginator import Paginator


def contact_home(request):
    contact_lists = Contact.objects.all().order_by(Lower('last_name'))
    paginator = Paginator(contact_lists, 5)
    context = {
        'all_contact_lists': contact_lists,
    }
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'pages/home.html', {'page_obj': page_obj})


def user_page(request, creator_user):
    contacts = Contact.objects.order_by(Lower('last_name'))
    contacts_by_user = contacts.filter(creator_user=creator_user)
    paginator = Paginator(contacts_by_user, 5)

    context = {
        'contacts': contacts_by_user,
        'user_on_page': creator_user,
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


