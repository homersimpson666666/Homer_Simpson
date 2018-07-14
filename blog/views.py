from django.shortcuts import render

from django.views.generic import TemplateView

#
# Create your views here.
class HomePageView(TemplateView):
	template_name = "index.html"
class AboutPageView(TemplateView):
	template_name= "about.html"
class DonatePageView(TemplateView):
	template_name = "donate.html"
class PoetryPageView(TemplateView):
	template_name = "poetry.html"
class TheBoyPageView(TemplateView):
	template_name = "theboy.html"
class ChatBotPageView(TemplateView):
	template_name = "chatbot.html"



