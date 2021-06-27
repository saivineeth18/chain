from django import forms
from django.forms.widgets import Textarea

class form_registers(forms.Form):
    name = forms.CharField(label="Name",min_length=1,widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Name"}))
    email = forms.EmailField(label='Email',min_length=1,widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Email","size":"35px"}))
    message = forms.CharField(required=False,label='Subject Description',widget=forms.Textarea(attrs={'class':'form-control','placeholder':"Message"}))
    
    def __init__(self, *args, **kwargs):
        super(form_registers, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['name'].widget.attrs['style'] = 'border-radius: 4px;box-shadow: none;font-size: 14px;height: 44px;'
        self.fields['email'].widget.attrs['style']  = 'border-radius: 4px;box-shadow: none;font-size: 14px;height: 44px;'
        self.fields['message'].widget.attrs['style']  = 'border-radius: 4px;box-shadow: none;font-size: 14px;padding: 10px 12px;'