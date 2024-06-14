from django.shortcuts import render



def get_main_page(request):
    return render(request, 'index.html')
# Create your views here.
