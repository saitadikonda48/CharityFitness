from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, HttpResponseRedirect, redirect
from django.utils.safestring import mark_safe

from .forms import LoginForm, RegisterForm
from .models import MyUser


def auth_logout(request):
	logout(request)
	return HttpResponseRedirect('/')

def auth_login(request):
	form = LoginForm(request.POST or None)
	next_url = request.GET.get('next')
	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			if next_url is not None:
				return HttpResponseRedirect(next_url)
			return HttpResponseRedirect("/")

	context = {"form": form}
	return render(request, "login.html", context)

def auth_register(request):
	register_form = RegisterForm(request.POST or None)
	if register_form.is_valid():
		username = register_form.clean_username()
		email = register_form.clean_email()
		password = register_form.clean_password2()
		new_user = MyUser()
		new_user.username = username
		new_user.email = email
		new_user.set_password(password)
		new_user.save()
		# Add message for success
		messages.success(request, 'Your account has been created.')
		return redirect('login')


	context = {
		"register_form":register_form,
		"action_value":"",
		"submit_btn_value":"Register",
	}
	return render(request,"accounts/register_form.html",context)
