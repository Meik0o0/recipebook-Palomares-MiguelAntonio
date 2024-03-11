from django.http import HttpResponse

from django.shortcuts import render


# Create your views here
def index(request):
    return HttpResponse('Hello world! This came from the index view')

    return render(request, 'ledger/recipe_list.html', ctx)

def recipe_list(request):
    context = {'header_text': 'Recipe Book'}
    return render(request, 'ledger/recipe_list.html', context)

def recipe_1(request):
    context = {'header_text': 'Recipe Book'}
    return render(request, 'ledger/recipe_1.html', context)

def recipe_2(request):
    context = {'header_text': 'Recipe Book'}
    return render(request, 'ledger/recipe_2.html', context)