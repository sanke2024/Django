from django import forms
from .models import Entry, Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic#nested Meta class telling Django which model to base the form
        #because it is based on topic model so it will have fields that are there in Topic with all restrictions and requirements like text field size less than 200
        fields=['text']
        labels={'text':''}
class EntryForm(forms.ModelForm):
    class Meta:
        model=Entry#bas yahi krne se hi sara 'Entry' ka sara attributes aa gaya isme. foreign key wala bhi jisko hmne view mein update kiya hai.
        fields=['text']
        labels={'text':''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}# this is just customization of text area, it will be 80 column wide