from django.shortcuts import render

# Create your views here.

def photo_add_view(request):
    context = {}
    return render(request, 'photos/index.html', context)