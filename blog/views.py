from django.shortcuts import render

# Create your views here.

def home(request):

    context = {

    }
    return render(request, 'index.html', context)


def blog(request):
    context={

    }

    return render(request, 'blog.html', context)


def detail(request):
    context = {

    }

    return render(request, 'blog-detail.html', context)



def projetDetail(request):

    context = {

    }

    return render(request, 'projet-detail.html', context)


def contact(request):

    context = {

    }

    return render(request, 'contact.html', context)