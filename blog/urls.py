from django.conf.urls import url
import views

urlpatterns = [
	url(r'^$', views.HomePageView.as_view()),
	url(r'^about/$', views.AboutPageView.as_view()), #Add this /about/ route
	url(r'^donate/$', views.DonatePageView.as_view()), #Donate page
	url(r'^poetry/$', views.PoetryPageView.as_view()), #Poetry
	url(r'^theboy/$', views.TheBoyPageView.as_view()), #The Boy
	url(r'^chatbot/$', views.ChatBotPageView.as_view()), #The Boy	
]