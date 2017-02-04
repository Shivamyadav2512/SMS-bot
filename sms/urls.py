'''from django.conf.urls import url, include
import views


urlpatterns = [
    url(r'^testing/$', views.testing),
    url(r'^common/$', views.CommonUrl.as_view()),
    url(r'^chatboturl/?$', views.ChatBot.as_view()),
]
'''

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.test),
]
