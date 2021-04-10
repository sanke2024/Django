"""defines urls for this app that is learning_logs """
from django.urls import path  # this imports path function which is important to map to views
from . import views #the dot tells Python to import views from the same directory as the
#current urls.py module
app_name = 'learning_logs' #ye zarrori hai namespace use krne ke liye
urlpatterns=[
 
    
    path('',views.index,name='index'),
    path('topics/',views.topics,name='topics'),
    path('topics/(?P<topic_id>\d+)/',views.thetopics,name='thetopics'),
    #the particular pattern is defined in the book
    path('new_topic/',views.new_topic,name='new_topic'),
    path('new_entry/(?P<topic_id>\d+)',views.new_entry,name='new_entry'),#captures a numerical value and stores it in the variable topic_id and passes it to the view function.
    path('edit_entry/(?P<entry_id>\d+)',views.edit_entry,name='edit_entry')
]