from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def login(request):
    form=UserCreationForm()
    context={'form':form}

    if request.method == 'POST':
        form=UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
    return render(request,'users/login.html',context)
