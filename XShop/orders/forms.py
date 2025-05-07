import re
from django import forms


class CreateOrderForm(forms.Form):
    
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    requires_delivery = forms.ChoiceField(
        choices=[
            ('0', False),
            ('1', True),
        ]
    )
    
    delivery_address_city = forms.CharField(required=False)
    delivery_address_street = forms.CharField(required=False)
    delivery_address_house = forms.CharField(required=False)
    delivery_address_apartment = forms.CharField(required=False)
    delivery_notes = forms.CharField(required=False)
    
    payment_on_get = forms.ChoiceField(
        choices=[
            ('0', False),
            ('1', True),
        ]
    )
    
    def clean_phone_number(self):
        data = self.cleaned_data['phone_number']
        
        if not data.isdigit():
            raise forms.ValidationError('Phone number must contain digits only')
        
        patterns = re.compile(r'^\d{10}$')
        if not patterns.match(data):
            raise forms.ValidationError('Invalid phone number format')
        
        return data