from django.shortcuts import render
from . models import Accueil, Studio , Equipe, Testimonial

# Create your views here.

def home(request):

    accueil = Accueil.objects.all()[1:]
    studio = Studio.objects.all()[:1]

    equipe = Equipe.objects.all()
    testimonial = Testimonial.objects.all()

    context = {
        'accueil':accueil,
        'studio':studio,
        'equipes':equipe,
        'testimonial':testimonial
        
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

