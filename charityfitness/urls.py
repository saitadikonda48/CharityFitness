"""charityfitness URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from charityfitness import views
from accounts import views

urlpatterns = [
	url(r'^$', 'charityfitness.views.home', name='home'),
    url(r'^about/$', 'charityfitness.views.about', name='about'),
    url(r'^contact/$', 'charityfitness.views.contact', name='contact'),
    url(r'^exercise/$', 'charityfitness.views.exercise', name='exercise'),
    url(r'^diet/$', 'charityfitness.views.diet', name='diet'),
    url(r'^injury/$', 'charityfitness.views.injury', name='injury'),
    url(r'^admin/', admin.site.urls),
    # auth login/logout
    url(r'^logout/$', 'accounts.views.auth_logout', name='logout'),
    url(r'^login/$', 'accounts.views.auth_login', name='login'),
    url(r'^register/$', 'accounts.views.auth_register', name='register'),
]
    
