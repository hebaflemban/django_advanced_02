from django.shortcuts import render, redirect
from .models import Store
from .forms import StoreModelForm
from django.contrib import messages


# Create your views here.
def store_list(request):
    context = {
        "stores": Store.objects.all()
    }
    return render(request, 'store_list.html', context)


def store_detail(request, store_slug):
    context = {
        "store": Store.objects.get(slug=store_slug)
    }
    return render(request, 'store_detail.html', context)



def create_view(request):
    form = StoreModelForm()
    if request.method == 'POST':
        form = StoreModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Syore Added to the mall successfully!')
            return redirect ('list')

    context = {
        "form": form
    }
    return render(request, 'create_store.html', context)
