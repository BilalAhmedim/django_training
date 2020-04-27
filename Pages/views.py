from django.shortcuts import render


# Create your views here.
def home_view(response, *args, **kwargs):
    context_variable = {
        'title' : 'this is just title - home',
        'html' : '<h1>Hello World!</h1>',
        'list' : [123,321,987],
        'boolean': True
    }
    return render(response, 'Base.html', context_variable)
