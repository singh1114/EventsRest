from django import forms

# If you don't do this you cannot use Bootstrap CSS
class Parti_Form(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=30,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'Firstname'}))
    last_name = forms.CharField(label="Last Name", max_length=30,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'Lastname'}))
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    email =  forms.EmailField(label="email", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password', 'type': 'password'}))
