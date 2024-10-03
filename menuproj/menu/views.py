from django.shortcuts import render

def home(request):
    context = {
        'some_data': 'This is some additional data',
    }
    return render(request, 'menu.html', context)