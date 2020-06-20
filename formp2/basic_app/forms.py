from django import forms
from basic_app.models import people

class signup_form(forms.ModelForm):
    class Meta():
        model=people
        fields=('FirstName','LastName','Email','password')
