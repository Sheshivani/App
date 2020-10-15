from django.shortcuts import render
from .forms import Pizzafroms, MultiplePizzaForm
from django.forms import formset_factory


def home(request):
    return render(request,'pizza/home.html')


def order(request):
    multiple_form = MultiplePizzaForm
    if request.method == 'POST':
        filled_forms = Pizzafroms(request.POST)
        if filled_forms.is_valid():
            notes = 'Thanks for Order! Your %s, %s and %s Pizza is on its way' %(filled_forms.cleaned_data['size'],
            filled_forms.cleaned_data['topping1'],
            filled_forms.cleaned_data['topping2'])
            new_forms = Pizzafroms()
            return render(request, 'pizza/order.html', {'pizzaforms': new_forms,'note': notes, 'multiple_form': multiple_form})

    else:
        forms = Pizzafroms()
        return render(request,'pizza/order.html', {'pizzaforms':forms, 'multiple_form': multiple_form})

def pizzas(request):
    number_of_pizzas = 2
    filled_mutiple_form_pizza = MultiplePizzaForm(request.GET)
    if filled_mutiple_form_pizza.is_valid():
        number_of_pizzas = filled_mutiple_form_pizza.cleaned_data['number']
    PizzaFormSet = formset_factory(Pizzafroms, extra = number_of_pizzas)
    formset = PizzaFormSet()
    if request.method == 'POST':
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data['topping1'])
            note = 'Pizza has been ordered!'
        else:
            note = 'Ordered was not created, Please try again'
        return render(request, 'pizza/pizzas.html', {'note': note, 'formset': formset})
    else:
        return render(request, 'pizza/pizzas.html', {'formset': formset})




