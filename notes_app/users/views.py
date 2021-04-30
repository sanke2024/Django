from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout,login,authenticate
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm



def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))


def register(request):
    if request.method!='POST':
        form=UserCreationForm()
    else:
        form=UserCreationForm(data=request.POST)

        if form.is_valid():

            #login the user along here after he is registered
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username,password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
           

    context = {'form': form}
    return render(request, 'users/register.html', context)













# Create your views here.

# def login(request):
#     form=CreateUserForm()
#     context={'form':form}

#     if request.method == 'POST':
#         form=CreateUserForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#     return render(request,'users/login.html',context)
