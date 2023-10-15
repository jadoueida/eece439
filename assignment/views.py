from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from assignment.models import Contact
from assignment.forms import ContactForm
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from assignment.serializers import ContactsSerializer



@csrf_exempt
def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact_serialized = ContactsSerializer(data = form.cleaned_data)
            if contact_serialized.is_valid():
                contact_serialized.save()
                return HttpResponseRedirect('/')
    else:
        form = ContactForm()
    return render(request, 'asssignment/createcontact.html', {'form': form})




@csrf_exempt
def get_all_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'asssignment/all_contacts.html', {'contacts': contacts})


@csrf_exempt
def update_contact(request,id):
    contact_data = JSONParser().parse(request)
    contact = Contact.objects.get(id = id)
    contact_serializer = ContactsSerializer(contact, data=contact_data,partial=True)
    if contact_serializer.is_valid():
        contact_serializer.save()
        return JsonResponse("Updated Successfully", safe=False, )
    return JsonResponse("Failed to Update", safe=False)


@csrf_exempt
def get_contact_by_id(request, id):
    contact = get_object_or_404(Contact, id= id)
    return render(request, 'asssignment/view_contact.html', {'contact': contact})


@csrf_exempt
def delete_contact_by_id(request, id):
    contact = get_object_or_404(Contact, id=id)

    if request.method == 'POST':
        contact.delete()
        return HttpResponseRedirect('/')

    return render(request, 'asssignment/delete_contact.html', {'contact': contact})

@csrf_exempt
def update_contact(request, id):
    contact = get_object_or_404(Contact, id=id)

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact.first_name = form.cleaned_data['first_name']
            contact.last_name = form.cleaned_data['last_name']
            contact.address = form.cleaned_data['address']
            contact.profession = form.cleaned_data['profession']
            contact.telephone = form.cleaned_data['telephone']
            contact.email = form.cleaned_data['email']
            if 'picture' in request.FILES:
                contact.picture = request.FILES['picture']
            contact.save()
            return HttpResponseRedirect('/')
    else:
        form = ContactForm(initial={
            'first_name': contact.first_name,
            'last_name': contact.last_name,
            'address': contact.address,
            'profession': contact.profession,
            'telephone': contact.telephone,
            'email': contact.email,
        })

    return render(request, 'asssignment/update_contact.html', {'form': form, 'contact': contact})


