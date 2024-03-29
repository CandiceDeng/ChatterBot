"""ChatBot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path
from django.http import HttpResponse

from . import view
from . import response




def chat(request):
    userInput = request.POST['userInput']
    return HttpResponse(response.GetResponse(userInput[0]))


urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^$', view.ChatBotView.as_view()),
     url(r'^api/chatterbot', view.ChatterBotApiView.as_view(), name='chatterbot'),
    # path('chat', chat, name='chat'),
]
