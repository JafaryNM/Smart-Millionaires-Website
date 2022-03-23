from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class DisplayHome(TemplateView):
    template_name='index.html'
    
class DisplayAbout(TemplateView):
    template_name='about.html'

class DisplayContact(TemplateView):
    template_name='contact.html'
    
class DisplayServices(TemplateView):
    
    template_name='services.html'