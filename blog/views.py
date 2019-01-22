# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,reverse
from blog.models import Contact, Review, UserImage, Category, Course
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.urls import reverse
from slugify import slugify
from django.contrib.auth.decorators import login_required
from django.db.models import Count

u_image=''
# Create your views here.
def home(request):
	categories = Category.objects.all()
	courses = Course.objects.all()
	courses_count = Category.objects.annotate(num_courses=Count('course'))
	
	print 'courses_count',courses_count
	for i in range(len(courses_count)):
		print courses_count[i], courses_count[i].num_courses
	return render(request,'index.html',{'category' : categories, 'course' : courses, "userImage" : u_image, "courses_count" : courses_count })

def about(request):
	return render(request,'about.html',{"userImage" : u_image, })

def courses(request):
	categories = Category.objects.all()
	courses = Course.objects.all()
	return render(request,'courses.html',{'category' : categories, 'course' : courses, "userImage" : u_image, })

def blog(request):
	return render(request,'blog.html',{"userImage" : u_image})
	
def contact(request):
	if request.method=="POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		subject = request.POST.get('subject')
		message = request.POST.get('message')
		data = Contact.objects.create(name=name, email=email,subject=subject, message=message)
		data.save()
		return render(request,'contact.html',{'msg':"sucess","userImage" : u_image})
	else:
		return render(request,'contact.html',{"userImage" : u_image})

def register(request):
	if request.method=="POST":
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		username = request.POST.get('username')
		email = request.POST.get('email')
		passd = request.POST.get('passwords')
		image = request.FILES['user-image']
		username_check = User.objects.filter(username=username).exists()
		if username_check:
			return render(request,'register.html',{'username_exist':"yes"})
		email_check = User.objects.filter(email=email).exists()
		if email_check:
			return render(request,'register.html',{'email_exist':"yes"})

		data = User.objects.create(first_name=first_name, last_name=last_name, username=username, email=email)
		data.set_password(passd)

		data.save()
		data1= UserImage(author=data,image=image)
		data1.save()
		return render(request,'register.html',{'msg':"success","userImage" : u_image})
	else:
		return render(request,'register.html',{"userImage" : u_image})

# @login_required(login_url='/home') #redirect when user is not logged i
def signin(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/home')
	else:
		if request.method=="POST":
			# try:
			#   username = request.POST.get('username')
			#   user = User.objects.get(username=username)
			#   us_image = UserImage.objects.get(author=user)
			# except Exception as e:
			#   print 'eeror',e
			#   return render(request,'login.html',{'msg':"failure"})
			
			# global u_image
			# u_image = us_image.image
			
			# print 'us_image',us_image,us_image.image
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = User.objects.get(username=username)
			us_image = UserImage.objects.get(author=user)
			global u_image
			u_image = us_image.image
			r = authenticate(username=username,password=password)
			print (r)
			if r:
				login(request,r)
				return HttpResponseRedirect(reverse('home_url'))
				# return render(request,'index.html',{"userImage" : u_image})
			else:
				print("outside")
				return render(request,'login.html',{'msg':"failure"})
		else:
			return render(request,'login.html',{"userImage" : u_image})

def signout(request):
	logout(request)
	print ("logout")
	return HttpResponseRedirect('/home')
	# return render(request,'index.html',{"userImage" : u_image})

@login_required(login_url='/login') #redirect when user is not logged in
def write_review(request):
	if request.method=="POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		subject = request.POST.get('subject')
		message = request.POST.get('message')
		image = request.FILES['user-image']
		review_url = slugify(subject)
		review_check = Review.objects.filter(review_url=review_url).exists()
		if review_check:
			import uuid 
			review_url= review_url+ uuid.uuid4().hex[:3].upper()

			print review_url
		data = Review.objects.create(name=name, email=email,subject=subject, message=message, review_url=review_url, image=image)
		data.save()
		return render(request,'write-review.html',{'msg':"sucess","userImage" : u_image})
	else:
		return render(request,'write-review.html',{"userImage" : u_image})

def reviews(request):
	reviews = Review.objects.all()
	print (reviews)

	return render(request,'reviews.html',{'review' : reviews,"userImage" : u_image})

def review_detail(request, rv_slug):
	print('rv_slug',rv_slug)
	review = Review.objects.get(review_url=rv_slug)
	print('review',review)
	return render(request,'review_detail.html',{'i' : review,"userImage" : u_image})

def register_home(request):
	if request.method=="POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		full_name = name.split()
		first_name = full_name[0]
		last_name = ' '.join(full_name[1:])
		print (first_name, last_name, email)
		
		return render(request,'register.html',{'first_name': first_name, 'last_name': last_name, 'email': email,'userimage' : u_image })
	else:
		return render(request,'register.html',{})

def profile(request, username):
	if request.method=="POST":
		user = User.objects.get(username=username)

		# username = request.POST.get('username')
		# email = request.POST.get('email')
		# if (user.username == username and user.email == email):
		#   user.username = username
		#   user.email = email
		# else:
		#   username_check = User.objects.filter(username=username, email=email).exists()
		#   if username_check:
		#       return render(request,'profile.html',{'username_exist':"yes"})
		#   else:
		#       user.username = username
		#       user.email = email

		username = request.POST.get('username')
		if user.username == username:
			user.username = username
		else:
			username_check = User.objects.filter(username=username).exists()
			if username_check:
				return render(request,'profile.html',{'username_exist':"yes"})
			else:
				user.username = username

		email = request.POST.get('email')
		if user.email == email:
			user.email = email
		else:
			email_check = User.objects.filter(email=email).exists()
			if email_check:
				return render(request,'profile.html',{'email_exist':"yes"})
			else:
				user.email = email

		user.first_name = request.POST.get('first_name')
		user.last_name = request.POST.get('last_name')
		passd = request.POST.get('password')
		if request.FILES:
			image = request.FILES['user-image']
			print image
			uImage = UserImage.objects.get(author=user)
			uImage.image = image
			uImage.save()
		if user.password == passd:
			print("same password")
		else:
			user.set_password(passd)


		user.save()
		username = request.POST.get('username')
		user = User.objects.get(username=username)
		us_image = UserImage.objects.get(author=user)
		return render(request,'index.html',{"userImage" : u_image})

		# return HttpResponseRedirect(reverse('home_url'))
		# return render(request,'profile.html',{'msg' : user})
	else:
		# user = User.objects.get(username=username)
		# us_image = UserImage.objects.get(author=user)
		# u_image = us_image.image
		return render(request,'profile.html',{"userImage" : u_image})

def category_single(request, category_slug):
	category = Category.objects.get(category_slug=category_slug)
	courses = Course.objects.filter(category=category)
	print('category',category)
	print('courses',courses)
	return render(request,'category_single.html',{'i' : category, 'c' : courses, "userImage" : u_image})

def category(request):
	categories = Category.objects.all()
	courses = Course.objects.all()
	return render(request,'categories.html',{'category' : categories, 'course' : courses, "userImage" : u_image, })

def course_single(request, course_slug):
	course = Course.objects.get(course_slug=course_slug)
	return render(request,'course_single.html',{'c' : course, "userImage" : u_image})

def course_search(request):
	if request.method=="POST":
		course = request.POST.get('course')
		category = request.POST.get('category')
		courses = Course.objects.filter(course_name__contains=course, category__category_name__contains=category)
		course_count = courses.count()
		if courses:
			return render(request,'courses.html',{'search_courses': courses,'count': course_count,  'userimage' : u_image })
		else:
			# categories = Category.objects.all()
			# courses = Course.objects.all()
			# return HttpResponseRedirect(reverse('courses_url', args=()))
			# return render(request,'courses.html',{'error': "yes", "userImage" : u_image, })
			return render(request,'courses.html',{'error': "yes"})
	else:
		categories = Category.objects.all()
		courses = Course.objects.all()
		return render(request,'courses.html',{'category' : categories, 'course' : courses, "userImage" : u_image, })

def review_user_register(request):
	if request.method=="POST":
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		username = request.POST.get('username')
		email = request.POST.get('email')
		passd = request.POST.get('passwords')
		image = request.FILES['user-image']
		username_check = User.objects.filter(username=username).exists()
		if username_check:
			return render(request,'register.html',{'username_exist':"yes"})
		email_check = User.objects.filter(email=email).exists()
		if email_check:
			return render(request,'register.html',{'email_exist':"yes"})

		data = User.objects.create(first_name=first_name, last_name=last_name, username=username, email=email)
		data.set_password(passd)

		data.save()
		data1= UserImage(author=data,image=image)
		data1.save()
		return render(request,'login.html',{'msg':"success","userImage" : u_image})
	else:
		return render(request,'register.html',{"userImage" : u_image})      

def users(request):
	usertable = UserImage.objects.all()
	user_count = usertable.count()
	return render(request,'users.html',{'usertable' : usertable,"userImage" : u_image, "count" : user_count})

def user_edit(request, username):
	user=User.objects.get(username=username)
	userDetails = UserImage.objects.get(author=user)
	print user,username,userDetails
	return render(request,'user_edit.html',{'userDetails' : userDetails,"userImage" : u_image})
