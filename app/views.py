from django.shortcuts import render
from .models import signup
from .forms import Abdi
# Create your views here.


def index(request):
    lis = signup.objects.order_by('F_Name')
    
    context = {
        "user":lis
    }

    return render(request,'Home.html',context)


def form_view(request):
    form = Abdi()

    if request.method == 'POST':
        form = Abdi(request.POST)

        if form.is_valid():
            myform = signup(F_Name = form.cleaned_data['Full_Name'],
                          E_mail = form.cleaned_data['Email'],
                          Username = form.cleaned_data['User_name'],
                          Password = form.cleaned_data['password'],
                          Phone = form.cleaned_data['phone'],
                          Address = form.cleaned_data['address'])
            myform.save()
            return index(request)
        else: 
            print('Error')


    return render(request,'form.html',{'Form':form})
