from django import forms


class FiboForm(forms.Form):
    num = forms.CharField(label="num")


class ContactForm(forms.Form):
    first_name = forms.CharField(label = "first")
    last_name = forms.CharField(label = "last")
    address = forms.CharField(label = "address")
    profession = forms.CharField(label = "profession")
    telephone = forms.CharField(label = "telephone")
    email = forms.CharField(label = "email")
    picture = forms.ImageField(label = "profilepic", required=False)


