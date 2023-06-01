from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm


from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def product_detail(request):
    return render(request, 'index_detail.html')


def cart(request):
    return render(request, 'cart.html')


def signup(request):
 
    if request.user.is_authenticated:
        return redirect('/shop')
     
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
 
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username,password = password)
            login(request, user)
            return redirect('/shop')
         
        else:
            return render(request,'signup.html',{'form':form})
     
    else:
        form = UserCreationForm()
        return render(request,'signup.html',{'form':form})
 
 
def signin(request):
    if request.user.is_authenticated:
        return redirect('/shop')
     
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password = password)
 
        if user is not None:
            login(request,user)
            return redirect('/shop')
        else:
            form = AuthenticationForm()
            return render(request,'signin.html',{'form':form})
     
    else:
        form = AuthenticationForm()
        return render(request, 'signin.html', {'form':form})
 
 
def signout(request):
    logout(request)
    return redirect('/shop/')
