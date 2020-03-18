from django.shortcuts import render

def list(request):
    return render(request, 'ingredients_list.html')
