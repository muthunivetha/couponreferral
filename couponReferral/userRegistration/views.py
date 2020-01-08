from django.shortcuts import render,redirect
from django.http import HttpResponse
import random,string
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import authenticate, login, logout
from django.utils.crypto import get_random_string
from userRegistration.forms import UserForm
from django.contrib.auth.decorators import login_required
from userRegistration.models import UserRegistration

# Create your views here.

def index(request):
	return render(request,'index.html',{'hh':'hjbkjhj'})

def register(request):
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		if user_form.is_valid() :
			user = user_form.save()
			# password = user_form.cleaned_data['password']
			# user.password=make_password(password)
			referral_code = request.POST.get('referral_code')
			if referral_code=='no' or referral_code=='No' or referral_code=='NO':
				referral_code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(7))
				user.referral_code=referral_code

			user.save()
			registered = True

		else:
			print(user_form.errors)
	else:
		user_form = UserForm()

	return render(request,'userregistration.html',{'user_form':user_form,'registered':registered})
	


	
def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		user = authenticate(username=username, password=password)
		u_pass=UserRegistration.objects.filter(username=username).values_list('password')[0][0]
		print(u_pass,"-----------")

		userdetails=UserRegistration.objects.filter(username=username)


		unique_id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(7))
		print(unique_id,"--------ijh-----")

		if password==u_pass:
			print("yess")
			return render(request,'userdetails.html',{'userdetails':userdetails})
		else:
			print("no")
			return HttpResponseRedirect(reverse('index'))
		# for i in use:
		# 	print(i.password)
		return HttpResponseRedirect(reverse('index'))



        

            
            
    

    
