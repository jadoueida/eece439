from django.contrib import admin
from django.urls import path
from django.urls import re_path, include
from assignment import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_all_contacts, name='list_contacts'),
    re_path(r'^addcontact', views.add_contact, name='add-contact'),
    re_path(r'^updatecontact/(?P<id>\w+)$', views.update_contact),
    re_path(r'^deletecontact/(?P<id>\w+)$', views.delete_contact_by_id, name= 'deletecontact'),
    re_path(r'^contact/(?P<id>\w+)$', views.get_contact_by_id),


]