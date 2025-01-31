from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['firstname', 'contact', 'address', 'pizza_type', 'quantity']
