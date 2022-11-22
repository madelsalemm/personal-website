from multiprocessing import context
from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import is_valid_path
from .models import Info , Portfolio , Skill
from django.core.mail import send_mail

from django.views.generic import DetailView 


'''
class InfoDetail(DetailView):
    model = Info
    template_name = 'contact/about.html'
    def get_context_data(self, *args, **kwargs):
        skill = Skill.objects.all()
        portfolio = Portfolio.objects.all()
        context = super(InfoDetail, self).get_context_data(*args, **kwargs)
        context['skill_list'] = skill
        context['portfolios'] = portfolio
        return context

'''
def infodetail (request , pk):
    myinfo = Info.objects.get (id=pk)
    skill = Skill.objects.all()
    portfolio = Portfolio.objects.all()
    
    if request.method =='POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        send_mail(subject, message, settings.EMAIL_HOST_USER , [email])
    context = {'skill_list' : skill , 'portfolios' : portfolio , 'myinfo' : myinfo}
    return render (request , 'contact/about.html' , context)
    



'''
class InfoDetail(DetailView):
    model = Info
    context_object_name = 'info'
    template_name = 'contact/about.html'

'''

'''
def send_message(request):
    myinfo = Info.objects.first()
    
    if request.method =='POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        send_mail(subject, message, settings.EMAIL_HOST_USER , [email])
    context = {'myinfo' : myinfo}
    return render (request , 'contact/contact.html' , context)
'''
'''
from rest_framework import generics 


class InfotList (generics.ListAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
    
class PostListApi(generics.ListCreateAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = ProfileImage
    
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProfileImage.objects.all()
    serializer_class = Portfolio
    lookup_field = 'id'

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SkillSerializer.objects.all()
    serializer_class = SkillSerializer
    lookup_field = 'id'
'''