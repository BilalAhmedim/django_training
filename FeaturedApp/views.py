from django.shortcuts import render, get_object_or_404
from .models import FeaturedApp
from .form import FeaturedAppForm, RawProductForm
from django.http import Http404


def product_list_view(request, ):
    queryset = FeaturedApp.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'FeaturedApp/list.html', context)


def dynamic_url_view(request, url_id):
    obj = get_object_or_404(FeaturedApp, id=url_id)
    # try:
    #     obj = FeaturedApp.objects.get(id=url_id)
    # except FeaturedApp.DoesNotExist:
    #     raise Http404
    context = {
        'object': obj
    }
    return render(request, 'FeaturedApp/details.html', context)


# Create your views here.
# def product_create_view(request):
#     form = RawProductForm()
#     if request.method == 'POST':
#         form = RawProductForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             FeaturedApp.objects.create(**form.cleaned_data)
#         else:
#             print(form.errors)
#     context_variable = {
#         'form':form
#     }
#     return render(request, 'FeaturedApp/product_create.html', context_variable)


def product_create_view(request):
    form = FeaturedAppForm(request.POST or None)
    # request.POST or None mean if request == post render out the form otherwise render out empty form
    if form.is_valid():
        form.save()
        form = FeaturedAppForm()
    context_variable = {
        'form': form,
    }
    return render(request, 'FeaturedApp/product_create.html', context_variable)


def product_detail_view(request):
    obj = FeaturedApp.objects.get(id=1)
    context_variable = {
        'object': obj,
    }
    return render(request, 'FeaturedApp/details.html', context_variable)
