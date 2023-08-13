from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomerCreateForm
from .models import Customer


def customer_list(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'customer/list.html', context)


def customer_create(request):
    form = CustomerCreateForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        context = {'form': form}
        return render(request, 'customer/create.html', context)


def customer_edit(request, id):
    customer = get_object_or_404(Customer, id=id)
    if request.method == 'POST':
        form = CustomerCreateForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerCreateForm(instance=customer)
        context = {'form': form}
        return render(request, 'customer/edit.html', context)


def customer_delete(request, id):
    customer = get_object_or_404(Customer, id=id)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    else:
        context = {'customer': customer}
        return render(request, 'customer/delete_confirm.html', context)
