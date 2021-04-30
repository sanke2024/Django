from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
# error -from django.core.urlresolvers import reverse
#Django 2.0 removes the django.core.urlresolvers module, which was moved to django.urls in version 1.10. You should change any import to use django.urls instead, like this:

from django.urls import reverse

from .models import Topic,Entry
from .forms import TopicForm,EntryForm
from django.contrib.auth.decorators import login_required


def check_topic_owner(topic,request):
    if topic.owner != request.user:
        raise Http404
# Create your views here.
def index(request):
    """homepage"""
    return render(request,'learning_logs/index.html')
#'learning_logs/index.html' -> template that will be returned when view.index maps to home page url

@login_required
def topics(request):
    """for topics page"""
    # topics=Topic.objects.order_by('date_added') -> instead we use below code for a particular user [explained on page 451]
    topics=Topic.objects.filter(owner=request.user).order_by('date_added')
    context={'topics':topics}
    return render(request,'learning_logs/topics.html',context)

@login_required
def thetopics(request,topic_id):
    """for a particular topic"""
    topic=Topic.objects.get(id=topic_id)
    
    #ownership check
    check_topic_owner(topic,request)

    entries=topic.entry_set.order_by('-date_added')
    context={'topic':topic,'entries':entries}
    return render(request,'learning_logs/thetopics.html',context)

@login_required
def new_topic(request):
    if request.method != 'POST':
        #'GET' means no data submitted so lets create a blank form
        form =TopicForm()#this form or class is already defined in forms.py file and imported
    else:
        form =TopicForm(request.POST)
        if form.is_valid():
            new_topic=form.save(commit=False)
           #connecting to new user
            new_topic.owner=request.user
            new_topic.save()

            #now insted of rendering anything we just save and  redirect to another page using reverse() to get url of that page and then that view will render accordingly
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    #if the request was GET then we need to render a form page
    context={'form':form} 
    return render(request,'learning_logs/new_topic.html',context)

@login_required  
def new_entry(request,topic_id):
    topic=Topic.objects.get(id=topic_id)
    check_topic_owner(topic,request)

    if request.method != 'POST':
        form =EntryForm()
    else:
        form =EntryForm(data=request.POST)

        if form.is_valid():
            new_entry=form.save(commit=False)
            new_entry.topic=topic

            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:thetopics',args=[topic_id]))
    context={'form':form,'topic':topic}
    return render(request,'learning_logs/new_entry.html',context)

@login_required
def edit_entry(request,entry_id):
    entry=Entry.objects.get(id=entry_id)
    topic=entry.topic
    
    #ownership check
    check_topic_owner(topic,request)
    # if topic.owner != request.user:
    #     raise Http404

    if request.method!='POST':
        form=EntryForm(instance=entry)

    else:
        form=EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:thetopics',args=[topic.id]))
    
    context={'entry':entry,'topic':topic,'form':form}
    return render(request,'learning_logs/edit_entry.html',context)
