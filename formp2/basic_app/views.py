from django.shortcuts import render
from basic_app.forms import signup_form
# Create your views here.

def index(request):
    return render(request,'basic_app/index.html')

def signup(request):
    registered=False

    if request.method=='POST':
        registrationform=signup_form(request.POST)

        if registrationform.is_valid():
            customer=registrationform.save(commit=True)
            return index(request)
        else:
            print(registrationform.errors)
    else:
        registrationform=signup_form()

    return render(request,'basic_app/signup.html',{'registrationform':registrationform})
