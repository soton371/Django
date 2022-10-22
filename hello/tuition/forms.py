from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100,label='your name')
    phone = forms.CharField(max_length=100,label='your phone')
    content = forms.CharField(max_length=100,label='your details')