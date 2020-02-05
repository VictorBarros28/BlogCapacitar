from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'pj':'poli junior'
    }

    return render(request,'core/index.html',context)


def contato(request):
    context = {
        'pj':'capacitar poli junior',
        'ano':2020,
    }

    return render(request,'core/contato.html',context)