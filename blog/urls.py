"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog import views
from django.conf import settings
from django.conf.urls.static import static  
urlpatterns = [
    url(r'^home$', views.home, name="home_url"),
    url(r'^about$', views.about, name="about_url"),
    url(r'^courses$', views.courses, name="courses_url"),
    url(r'^blog$', views.blog, name="blog_url"),
    url(r'^contact$', views.contact, name="contact_url"),
    url(r'^register$', views.register, name="register_url"),
    url(r'^login$', views.signin, name="login_url"),
    url(r'^logout$', views.signout, name="logoutt_url"),
    url(r'^write-review$', views.write_review, name="write-review_url"),
    url(r'^reviews$', views.reviews, name="reviews_url"),
    url(r'^reviews/(?P<rv_slug>[\w-]+)/$', views.review_detail, name="reviews_detail_url"),
    url(r'^register/$', views.register_home, name="register_home_url"),
    url(r'^profile/(?P<username>[\w-]+)$', views.profile, name="profile_url"),
    url(r'^categories/(?P<category_slug>[\w-]+)$', views.category_single, name="category_single_url"),
    url(r'^categories/$', views.category, name="category_url"),
    url(r'^courses/(?P<course_slug>[\w-]+)$', views.course_single, name="course_single_url"),
    url(r'^courses/$', views.course_search, name="course_search_url"),
    url(r'^register/', views.review_user_register, name="review_user_register_url"),
    url(r'^users/(?P<username>[\w-]+)$', views.user_edit, name="user_edit_url"),
    url(r'^users/$', views.users, name="users_url"),

    # url(r'^', views.home, name='home_url'),
    # url(r'^about/', views.about, name='about_url'),
]
    
urlpatterns += url(r'^$', views.home),

if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

