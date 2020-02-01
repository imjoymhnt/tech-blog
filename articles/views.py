from django.shortcuts import render
from .models import Article, About, Contact
from django.views.generic import ListView, DetailView, TemplateView
# Create your views here.

class HomePageView(ListView):
    model = Article
    template_name = 'articles/index.html'


class DetailPageView(DetailView):
    model = Article
    template_name = 'articles/detail.html'
    

class AboutPageView(ListView):
    model = About
    template_name = 'articles/about.html'

class ContactPageView(ListView):
    model = Contact
    template_name = 'articles/contact.html'
