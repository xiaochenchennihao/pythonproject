from django import forms

class AuthorForm(forms.Form):
    name = forms.CharField(max_length = 32)
    age = forms.IntegerField()
    birthday = forms.DateField()
    email = forms.EmailField()
    phone = forms.CharField(max_length = 32)
    photo = forms.ImageField()
    address = forms.Textarea()