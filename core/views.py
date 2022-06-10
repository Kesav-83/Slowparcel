from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib.auth import login
# Create your views here.
# 
def home(request):
    return render(request,'home.html')
@login_required()
def customer_page(request):
    return render(request,'home.html')
@login_required()
def courier_page(request):
    return render(request,'home.html')
def sign_up(request):
    form=forms.SignUPForm()
    if request.method=='POST':
       form=forms.SignUPForm(request.POST)
       if form.is_valid():
           email=form.cleaned_data.get('email').lower()
           user=form.save(commit=False)
           user.username=email
           user.save()
           login(request,user)
           return redirect('/')
    return render(request,'sign_up.html',{
            'form':form
        })


