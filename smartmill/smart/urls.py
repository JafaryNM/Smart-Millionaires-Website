from django.urls  import path
from .views import *

urlpatterns = [
    path('', DisplayHome.as_view(), name='homepage'),
    path('about/', DisplayAbout.as_view(), name='about'),
    path('contact/',DisplayContact.as_view(), name='contact'),
    path('services/',DisplayServices.as_view(), name='services')
]