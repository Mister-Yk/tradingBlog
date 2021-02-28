from django.db import models

# Create your models here.

class Accueil(models.Model):
    """Model definition for Accueil."""

    # TODO: Define fields here
    titre = models.CharField(max_length=255)
    contact = models.CharField(max_length=155)
    image = models.ImageField(upload_to="images")

    class Meta:
        """Meta definition for Accueil."""

        verbose_name = 'Accueil'
        verbose_name_plural = 'Accueils'

    def __str__(self):
        """Unicode representation of Accueil."""
        return self.titre


class Studio(models.Model):
    """Model definition for Studio."""

    # TODO: Define fields here

    titre =models.CharField(max_length=255)
    text = models.TextField()
    images = models.FileField(upload_to="images")

    class Meta:
        """Meta definition for Studio."""

        verbose_name = 'Studio'
        verbose_name_plural = 'Studios'

    def __str__(self):
        """Unicode representation of Studio."""
        return self.titre


class Equipe(models.Model):
    """Model definition for Equipe."""

    # TODO: Define fields here
    nom = models.CharField(max_length=255)
    specialite = models.CharField(max_length=255)
    images = models.FileField(upload_to="images/equipe")
    imageblog = models.FileField(upload_to="images/equipe")
    titre = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        """Meta definition for Equipe."""

        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'

    def __str__(self):
        """Unicode representation of Equipe."""
        return self.nom


  
class Auteur(models.Model):
    """Model definition for Auteur."""

    # TODO: Define fields here
    nom = models.CharField(max_length=255)
    mail = models.EmailField()
    image = models.FileField(upload_to="images")

    class Meta:
        """Meta definition for Auteur."""

        verbose_name = 'Auteur'
        verbose_name_plural = 'Auteurs'

    def __str__(self):
        """Unicode representation of Auteur."""
        return self.nom

class Categorie(models.Model):
    """Model definition for Categorie."""

    # TODO: Define fields here
    titre = models.CharField(max_length=255)
    text = models.CharField(max_length=100)
    images = models.FileField(upload_to="images")

    class Meta:
        """Meta definition for Categorie."""

        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Categorie."""
        return self.titre



class Commentaire(models.Model):
    """Model definition for Commentaire."""

    # TODO: Define fields here

    nom = models.CharField(max_length=255)
    mail = models.EmailField()
    message = models.TextField()


    class Meta:
        """Meta definition for Commentaire."""

        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaires'

    def __str__(self):
        """Unicode representation of Commentaire."""
        return self.nom

class Article(models.Model):
    """Model definition for Article."""

    # TODO: Define fields here
    titre = models.CharField(max_length=255)
    soustitre = models.CharField(max_length=300)
    description = models.TextField()
    titre1 = models.CharField(max_length=100)
    titre2 = models.CharField(max_length=100)
    description2 = models.TextField()
    images = models.FileField(upload_to="images")
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE, null=True)
    commentaire = models.ForeignKey(Commentaire, on_delete=models.CASCADE, null=True)
    categorie = models.ManyToManyField(Categorie)
    satut = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Article."""

        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        """Unicode representation of Article."""
        return self.titre



class Testimonial(models.Model):
    """Model definition for Testimonial."""

    # TODO: Define fields here
    text = models.CharField(max_length=300)
    images =models.FileField(upload_to="images")
    date = models.DateTimeField(auto_now_add=True)
    nom = models.CharField(max_length=255)
    nomauteur = models.CharField(max_length=255)
    agence = models.CharField(max_length=255)

    class Meta:
        """Meta definition for Testimonial."""

        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        """Unicode representation of Testimonial."""
        return self.nom


