from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from .models import Pizza, Topping
from .forms import PizzaForm, ToppingForm

# Create your views here.
def index(request):
    return render(request, 'pizzeria_app/index.html')

@login_required
def pizzas(request):
    '''Show all pizzas.'''
    pizzas = Pizza.objects.filter(owner=request.user).order_by('name')
    context = {'pizzas' : pizzas}
    return render(request, 'pizzeria_app/pizzas.html', context)

@login_required
def pizza(request, pizza_id):
    '''Show a single pizza and all of its toppings.'''
    #pizza = Pizza.objects.get(id=pizza_id)
    pizza = get_object_or_404(Pizza, id=pizza_id)
    if pizza.owner != request.user:
        raise Http404
    toppings = pizza.topping_set.order_by('name')
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzeria_app/pizza.html', context)

@login_required
def new_pizza(request):
    '''Add a new pizza'''
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = PizzaForm()
    else:
        # POST data submitted; process data.
        form = PizzaForm(request.POST)
        if form.is_valid():
            new_pizza = form.save(commit=False)
            new_pizza.owner = request.user
            new_pizza.save()            
            return HttpResponseRedirect(reverse('pizzeria_app:pizzas'))
    context = {'form' : form}
    return render(request, 'pizzeria_app/new_pizza.html', context)

@login_required
def new_topping(request, pizza_id):
    '''Add a new topping for a particular pizza.'''
    pizza = Pizza.objects.get(id=pizza_id)
    if pizza.owner != request.user:
        raise Http404
    
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = ToppingForm()
    else:
        # POST data submitted; process data.
        form = ToppingForm(data=request.POST)
        if form.is_valid():
            new_topping = form.save(commit=False)
            new_topping.pizza = pizza
            new_topping.save()
            return HttpResponseRedirect(reverse('pizzeria_app:pizza', args=[pizza_id]))
    context = {'pizza' : pizza, 'form' : form}
    return render(request, 'pizzeria_app/new_topping.html', context)

@login_required
def edit_topping(request, topping_id):
    '''Edit an existing topping.'''
    topping = Topping.objects.get(id=topping_id)
    pizza = topping.pizza
    if pizza.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = ToppingForm(instance=topping)
    else:
        # POST data submitted; process data.
        form = ToppingForm(instance=topping, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('pizzeria_app:pizza', args=[pizza.id]))
    context = {'topping' : topping, 'pizza' : pizza, 'form' : form}
    return render(request, 'pizzeria_app/edit_topping.html', context)
    

    
