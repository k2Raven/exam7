"""poll URL Configuration

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
from django.urls import path

from webapp.views import IndexView, PollView, PollCreateView, PollUpdateView, PollDeleteView,\
    ChoiceCreateView, ChoiceUpdateView, ChoiceDeleteView, AnswerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('poll/<int:pk>', PollView.as_view(), name='poll_view'),
    path('poll/add', PollCreateView.as_view(), name='poll_create'),
    path('poll/<int:pk>/edit/', PollUpdateView.as_view(), name='poll_update'),
    path('poll/<int:pk>/delete/', PollDeleteView.as_view(), name='delete_poll'),
    path('poll/<int:pk>/add-choice/', ChoiceCreateView.as_view(), name='choice_create'),
    path('choice/<int:pk>/edit/', ChoiceUpdateView.as_view(), name='choice_update'),
    path('choice/<int:pk>/delete/', ChoiceDeleteView.as_view(), name='delete_choice'),
    path('answer/<int:pk>/poll', AnswerView.as_view(), name='answer')

]
