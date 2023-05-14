from django.shortcuts import render

# Create your views here.


def say_hello(request):
    x = 1
    y = 2

    context = {'name' : 'Andrej'}
    return render(request, 'hello.html', context)