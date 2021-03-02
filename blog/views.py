from django.shortcuts import render,redirect
from . models import Accueil, Studio , Equipe, Testimonial, Article, Categorie, Contact, Newletter

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

    article = Article.objects.all()
    categorie = Categorie.objects.all()

    if request.method=="POST":
        email = request.POST.get('email')

        newletter = Newletter(
            email=email
        )

        newletter.save()
  
    context={
        'articles':article,
        'categories':categorie
   
     

    }

    return render(request, 'blog.html', context)


def detail(request, pk):

    try:
        article = Article.objects.get(id=pk)
        context = {
            'article':article
    }
    except:
        return redirect('home')

    return render(request,'blog-detail.html',context)



def projetDetail(request, pk):
    try:
        equipe = Equipe.objects.get(id=pk)
        context = {
            'equipe':equipe,
    }
    except:
        return redirect('home')

    return render(request, 'projet-detail.html', context)


def contact(request):

    if request.method=="POST":
        nom =request.POST.get('nom')
        email = request.POST.get('mail')
        message = request.POST.get('message')

        contact = Contact(
            nom=nom,
            mail=email, 
            message=message
        )

        contact.save()

    context = {

    }

    return render(request, 'contact.html', context)

