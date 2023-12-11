from django import forms
from .models import *
from django.utils import timezone
from django.shortcuts import get_object_or_404




class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ['name', 'contact', 'address', 'purpose', 'department','date','time_in','time_out','captured_photo']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Full Name'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Contact'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Address'}),
            'purpose': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Purpose'}),
            'department': forms.Select(attrs={'class': 'form-control','placeholder':'Department'}),
            'date': forms.TextInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Date'}),
            'time_in': forms.HiddenInput(),
            'time_out': forms.HiddenInput(),
            'captured_photo': forms.HiddenInput,

        }

        labels={
            'name': '',
            'contact': '',
            'address': '',
            'purpose': '',
            'department': '',
            'date': '',
            'captured_photo': 'Choose Photo'
        }

# forms.py
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['visitor', 'item_1', 'item_2', 'item_3', 'item_4', 'item_5', 'item_6', 'item_7', 'item_8', 'item_9', 'comment']
        widgets = {
            'visitor': forms.HiddenInput(),
            'item_1': forms.Select(attrs={'class': 'form-control'}),
            'item_2': forms.Select(attrs={'class': 'form-control'}),
            'item_3': forms.Select(attrs={'class': 'form-control'}),
            'item_4': forms.Select(attrs={'class': 'form-control'}),
            'item_5': forms.Select(attrs={'class': 'form-control'}),
            'item_6': forms.Select(attrs={'class': 'form-control'}),
            'item_7': forms.Select(attrs={'class': 'form-control'}),
            'item_8': forms.Select(attrs={'class': 'form-control'}),
            'item_9': forms.Select(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comment', 'rows': 4}),
        }

        labels = {
            'item_1': 'SQDO. I am satisfied with the service that i availed',
            'item_2': 'SQD1. I spend a reasonable amount of time for my transaction',
            'item_3': "SQD2. The office followed the transaction's requirements and steps based on the information provided.",
            'item_4': "SQD3. The steps (including payment) I needed to do for my transaction were easy and simple.",
            'item_5': "SQD4. I easily found information about my transaction from the office or its website.",
            'item_6': "SQD5. I paid a reasonable amount of fees for my transaction.",
            'item_7': 'SQD6. I feel the office was fair to everyone, or "walang palakasan", during my transaction.',
            'item_8': "SQD7. I was treated courteously by the staff, and (if asked for help) the staff was helpful.",
            'item_9': "SQD8. I got what I needed from the government office, or (if denied) denial of request was sufficiently explained to me.",

        }
   


class UniqueIDForm(forms.Form):
    unique_id = forms.CharField(
        max_length=11,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Unique ID'}),
        label=''
    )
