from django.shortcuts import render,redirect
from.forms import OrderForm

def index(request):
    return render(request, 'index.html')

def pizzas(request):
    return render(request, 'pizzas.html') 

def deals(request):
    return render(request, 'deals.html')

def orders(request):
    return render(request, 'orders.html')

def orders(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()  # Save the order to the database
            return redirect('index')  # Redirect to a success page or index
    else:
        form = OrderForm()
    return render(request, 'orders.html', {'form': form})