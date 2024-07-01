from django.urls import path
from web.views import index, about, contact, com_course, dis_course

app_name = 'web'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('com-courses/', com_course, name='com_course'),
    path('dis-courses/', dis_course, name='dis_course'),
]
