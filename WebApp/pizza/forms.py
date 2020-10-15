from django import forms
from .models import Pizza

# class Pizzafroms(forms.Form):
#     topping1 = forms.CharField(max_length=100)
#     topping2 = forms.CharField(max_length=100)
#     size = forms.ChoiceField(label='Size', choices=[('small','small'),('Medium','Medium'),('Large','Large')])

class Pizzafroms(forms.ModelForm):

    class Meta :
        model = Pizza
        fields = ['topping1','topping2','size']
        lables={'topping1':'Topping 1 ', 'topping2':'Topping 2 '}

class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)
