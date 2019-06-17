from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.template import loader
from django import forms


def base(request):
	return render(request,'basic/base.html')


def create(request):
    if(request.method=="POST"):
        form=ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            #return render(request,'basic/success.html',{'form':form})
            return redirect('read')
    else:
        form=ProfileForm()
    return render(request,'basic/register.html',{'form':form})


def read(request):
    allinfo=Profile.objects.all()
    return render(request,'basic/read.html',{'allinfo':allinfo})


def userdetails(request,id_no):
	userdetail=Profile.objects.filter(id_no=id_no).values()
	return render(request,'basic/userdetails.html',{'userdetail':userdetail})


def update(request,id_no):
    userdetail=Profile.objects.get(id_no=id_no)
    if(request.method=="POST"):
        form=ProfileForm(request.POST,instance=userdetail)
        if form.is_valid():
        	form.save()
        	return redirect('read')
    else:
        form=ProfileForm(instance=userdetail)
    return render(request,'basic/update.html',{'form':form})
 

def delete(request,id_no):
    userdelete=Profile.objects.get(id_no=id_no)
    userdelete.delete()
    return redirect('read')            	



