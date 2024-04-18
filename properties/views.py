from django.shortcuts import render, redirect,  get_object_or_404
from .models import Property
from .forms import PropertyForm
from django.urls import reverse


def property_list(request):
    persons = Property.objects.all()
    return render(request, "properties/property_list2.html", {'properties': persons})


def property_detail(request, item_id):
    item = get_object_or_404(Property, pk=item_id)
    return render(request, 'properties/detail.html', {'item': item})

# Create your views here.

def add_properties(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('listing'))  # Redirect to a new URL if you want
    else:
        form = PropertyForm()
    return render(request, 'properties/add_property.html', {'form': form})


def edit_property(request, pk):
    property_instance = get_object_or_404(Property, pk=pk)
    if request.method == 'POST':
        form = PropertyForm(request.POST, instance=property_instance)
        if form.is_valid():
            form.save()
            return redirect(reverse('listing'))  # Redirect to detail page after editing
    else:
        form = PropertyForm(instance=property_instance)
    return render(request, 'properties/edit_property.html', {'form': form})