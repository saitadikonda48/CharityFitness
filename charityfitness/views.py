from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.utils.safestring import mark_safe

from .forms import WeightForm, CalorieForm

from accounts.forms import LoginForm, RegisterForm, UserProfileChangeForm, MessageForm
from accounts.models import MyUser, UserProfile, Message

import datetime

def home(request):
	if request.user.is_authenticated():
		#Determine User
		user = MyUser.objects.get(username=request.user).userprofile

		# Change UserProfile info if needed
		editForm=UserProfileChangeForm(request.POST or None,
			initial={'full_name':user.full_name,
			'age':user.age,
			'height':user.height,
			'startWeight':user.startWeight,
			'startDate':user.startDate,
			'goalWeight':user.goalWeight,
			'goalDate':user.goalDate,
			'hobbies':user.hobbies
			})
		
		if editForm.is_valid():
			full_name = editForm.cleaned_data.get("full_name")
			age = editForm.cleaned_data.get("age")
			height = editForm.cleaned_data.get("height")
			startWeight = editForm.cleaned_data.get("startWeight")
			startDate = editForm.cleaned_data.get("startDate")
			goalWeight = editForm.cleaned_data.get("goalWeight")
			goalDate = editForm.cleaned_data.get("goalDate")
			activities = editForm.cleaned_data.get("hobbies")
			# Name check
			user.full_name = full_name
			user.hobbies = activities
			# Age check
			tempAge = user.age
			user.age = age
			if (age > 120) or (age < 8):
				messages.error(request, 'Age must be less than 120 and greater than 8.')
				user.age = tempAge
			# Height check
			tempHeight = user.height
			user.height = height
			if (height > 244) or (height < 61):
				messages.error(request, 'Height must be less than 244cm and greater than 61cm.')
				user.height = tempHeight
			# Weight check
			tempStartWeight = user.startWeight
			user.startWeight = startWeight
			if (startWeight > 450) or (startWeight < 35):
				messages.error(request, 'Starting weight must be less than 450lbs and greater than 35lbs.')
				user.startWeight = tempStartWeight
			tempGoalWeight = user.goalWeight
			user.goalWeight = goalWeight
			if (goalWeight > 450) or (goalWeight < 35):
				messages.error(request, 'Goal weight must be less than 450lbs and greater than 35lbs.')
				user.goalWeight = tempGoalWeight
			
			# Date check
			tempStart = user.startDate
			tempEnd = user.goalDate
			user.startDate = startDate
			user.goalDate = goalDate
			if startDate > goalDate:
				messages.error(request, 'The goal date must come AFTER the starting date.')
				user.startDate = tempStart
				user.goalDate = tempEnd
			
			user.save()


		#Create Expected Weight Data
		weightChangeList = [user.startWeight]
		dailyLoss = []
		deltaWeight = user.goalWeight - user.startWeight
		deltaTime = (user.goalDate - user.startDate).days
		sumOfDays = 0
		counter = 0
		while(counter!=deltaTime):
			counter = counter + 1
			sumOfDays = sumOfDays + counter

		convFact = 1.0*(deltaWeight)/(sumOfDays)
		counter = 0
		currWeight = user.startWeight
		while (counter < deltaTime):
			lossThatDay = (deltaTime - counter)*(convFact)
			dailyLoss.append(lossThatDay)
			currWeight = currWeight + lossThatDay
			weightChangeList.append(currWeight)
			counter = counter + 1

		#Check users weight
		weightForm = WeightForm(request.GET or None)
		todaysWeight = None
		if weightForm.is_valid():
			todaysWeight = weightForm.cleaned_data.get("your_weight")

		context={
		"todaysWeight":todaysWeight,
		"weightForm":weightForm,
		"editForm":editForm,
		"weightChangeList":weightChangeList,
		"startWeight":user.startWeight,
		"goalWeight":user.goalWeight,
		}
		template="home_logged_in.html"
	else:
		login_form = LoginForm()
		register_form = RegisterForm()
		context = {
			"login_form":login_form,
			"register_form":register_form,
		}
		template="home_visitor.html"

	return render(request,template,context)

def about(request):
	login_form = LoginForm()
	return render(request,"extra_info/about.html",{"login_form":login_form,})

def contact(request):
	login_form = LoginForm()
	messageForm = MessageForm(request.POST or None)
	confirmationText = ""
	if messageForm.is_valid():
		email = messageForm.cleaned_data.get("email")
		name = messageForm.cleaned_data.get("name")
		message = messageForm.cleaned_data.get("message")
		new_message = Message()
		new_message.email = email
		new_message.name = name
		new_message.message = message
		new_message.save()
		confirmationText = "Your message has been sent."
	context = {
		"messageForm":messageForm,
		"login_form":login_form,
		"confirmationText":confirmationText,
	}
	return render(request,"extra_info/contact.html",context)

def exercise(request):
	return render(request,"extra_info/exercise.html",{})

def diet(request):
	calorieForm = CalorieForm(request.POST or None)
	caloric_intake = 2000
	if calorieForm.is_valid():
		caloric_intake = calorieForm.cleaned_data.get("caloric_intake")

	context = {
		"calorieForm":calorieForm,
		"caloric_intake":caloric_intake,
	}
	return render(request,"extra_info/diet.html",context)

def injury(request):
	return render(request,"extra_info/injury.html",{})

