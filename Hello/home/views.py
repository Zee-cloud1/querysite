from django.shortcuts import render, HttpResponse
from datetime import date, datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
        "variable":"this is sent"
    } 
    
    return render(request, 'index.html',context)
def about(request):
    return render(request, 'about.html',)
def services(request):
    return render(request, 'services.html',)
def contact(request):
    if request.method=="POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact= Contact(name=name, phone=phone, email=email, desc=desc, date =datetime.today())
        contact.save()
        messages.success(request, 'Your query has been sent!')
    return render(request, 'contact.html',)       