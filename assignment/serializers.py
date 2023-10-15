from rest_framework import serializers
from assignment.models import Contact


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id','first_name', 'last_name', 'address', 'profession', 'telephone', 'email','picture']