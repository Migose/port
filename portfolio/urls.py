"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import portfolioapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', portfolioapp.views.home, name="home" ),
    path('traits/food', portfolioapp.views.food, name="food" ),
    path('traits/game', portfolioapp.views.game, name="game" ),
    path('traits/demo', portfolioapp.views.demo, name="demo" ),
    path('traits/career', portfolioapp.views.career, name="career" ),
    path('chrono', portfolioapp.views.chrono, name="chrono" ),
    path('posts', portfolioapp.views.posts, name="posts" ),
    path('contact', portfolioapp.views.contact, name="contact" ),
]
