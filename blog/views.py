from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from .import forms
from .models import Article
#from  .models.User import User
from django.contrib.auth.models import User
articles=Article.objects.all().order_by()

# Create your views here.
def index(request):
	return render(request,'home.html',{'articles':articles})
	    

def detail(request):
	if request.method=='POST':
		form=forms.CreateAdmin(request.POST)
		if form.is_valid():
			form.save()
			return render(request,'response.html',{'form':form})
	else:
		form=forms.CreateAdmin()
	return render(request,'detail.html',{'form':form})

	

def detail1(request):
	if request.method=='POST':
		form=forms.CreateInter(request.POST)
		if form.is_valid():
			form.save()
			return render(request,'response1.html',{'form':form})
	else:
		form=forms.CreateInter()
			

	return render(request,'detail1.html',{'form':form})

def activite(request):
    return render(request,'activite.html',{'articles':articles})

	    
def compt(request):
	if request.method=='POST':
		form=UserCreationForm(data=request.POST)
		#form1=CreateUs(request.POST)
		if form.is_valid():
			user=form.save()
			login(request, user)
			return redirect('login_view')

	else:
		form=UserCreationForm()
	return render(request, 'compt.html',{'form':form})



def login_view(request):
    if request.method=='POST':
    	form=AuthenticationForm(data=request.POST)
    	if form.is_valid():
    		user=form.get_user()
    		login(request, user)
    		return redirect('index')
    else:
    	form=AuthenticationForm()
    return render(request, 'login.html',{'form':form}) 		

    		
def logout_view(request):
	if request.method=='POST':
		logout(request)
		return redirect('login_view')
	return render(request, 'logout.html')	


    			
    	#else:
    		#return redirect('compt')
    			

      	
#@login_required(login_url="/blog/compt/")




    