from django.db import models
from django.contrib.auth.models import AbstractUser
# specifying choices
  
from django.conf import settings

# Add the import for GridFSStorage
from djongo.storage import GridFSStorage
grid_fs_storage = GridFSStorage(collection='myfiles', base_url=''.join(['/', 'myfiles/']))

# Create your models here.
#matieres
class Matiere(models.Model) :
    name = models.CharField(max_length=50, unique = True)
    description = models.CharField(max_length=150)
    image_matiere = models.FileField(upload_to="static/upload/images",blank=True)
    prof=models.ForeignKey('ProfProfile', on_delete=models.CASCADE)
    filiere=models.ForeignKey('Filiere', on_delete=models.CASCADE)
    def __str__(self):
        return self.name
from django.core.validators import FileExtensionValidator
#cours
class Cours(models.Model):
    titre = models.CharField(max_length=50, unique = True)
    description = models.CharField(max_length=150)
    pdf_cours = models.FileField(blank=True,validators=[FileExtensionValidator(['pdf'])],upload_to='Cours', storage=grid_fs_storage)
    Appartient = models.ForeignKey('Matiere',related_name="Matiere", on_delete=models.CASCADE)
    def __str__(self):
        return self.titre

class Td(models.Model):
    titre = models.CharField(max_length=50, unique = True)
    description = models.CharField(max_length=150)
    pdf_TD = models.FileField(validators=[FileExtensionValidator(['pdf'])],upload_to='TD', storage=grid_fs_storage)
    pdf_TD_correction = models.FileField(blank=True, null=True,validators=[FileExtensionValidator(['pdf'])],upload_to='TD', storage=grid_fs_storage)
    Appartient = models.ForeignKey('Matiere',related_name="Td", on_delete=models.CASCADE)
    def __str__(self):
        return self.titre

class Tp(models.Model):
    titre = models.CharField(max_length=50, unique = True)
    description = models.CharField(max_length=150)
    pdf_TP = models.FileField(validators=[FileExtensionValidator(['pdf'])],upload_to='TP', storage=grid_fs_storage)
    Appartient = models.ForeignKey('Matiere',related_name="Tp", on_delete=models.CASCADE)
    def __str__(self):
        return self.titre


#filier
class Filiere(models.Model):
    nom_Filiere = models.CharField(max_length=50, unique = True)
    def __str__(self):
        return self.nom_Filiere

#users
class User(AbstractUser):
    phone =models.PositiveIntegerField(blank=True,null=True)
    NNI =models.PositiveBigIntegerField(unique = True,null=True,blank=True)


class ProfProfile(models.Model):
    user = models.OneToOneField('User', related_name='teacher_profile', on_delete=models.CASCADE,primary_key=True)
    def __str__(self):
        return self.user.username
    
class EtudientProfile(models.Model):
    user = models.OneToOneField('User', related_name='student_profile', on_delete=models.CASCADE,primary_key=True)
    id_filiere= models.ForeignKey('Filiere',related_name="Filiere", on_delete=models.CASCADE )
    def __str__(self):
        return self.user.username
    

