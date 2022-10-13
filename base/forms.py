from dataclasses import fields
from django import forms
from django.forms import ModelForm
from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        labels={
            'service_name' : 'Select Service Name',
            'member_name'  : 'Select Your Name',
            'start' : 'Enter Starting Date',
            'end'   : 'Enter Ending Date',
            'total_d' : 'Enter Total Days'
        }
        widgets = {
                'start' : DateInput(),
                'end' : DateInput(),
        }


    def __init__(self,*args,**kwargs):
        super(ServiceForm,self).__init__(*args,**kwargs)
        self.fields['member_name'].empty_label ="Select"
        self.fields['end'].required =True
        self.fields['total_price'].required =False
