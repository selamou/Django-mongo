from django import forms
from .models import *

class PostCours(forms.ModelForm):
     class Meta:
        model = Cours
        fields = ('titre', 'description', 'pdf_cours')
class PostTd(forms.ModelForm):
     class Meta:
        model = Td
        fields = ('titre', 'description', 'pdf_TD','pdf_TD_correction')
class PostTp(forms.ModelForm):
     class Meta:
        model = Tp
        fields = ('titre', 'description', 'pdf_TP')
class PostProf(forms.ModelForm):
     class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password','phone')
        extra_kwargs = {'password': {'write_only': True}}
class EditProf(forms.ModelForm):
     class Meta:
        model = User
        fields = ('id', 'username', 'email','phone')
class PostEtd(forms.ModelForm):
     class Meta:
        model = EtudientProfile
        fields = ('id_filiere',)
class Postuser(forms.ModelForm):
     class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password','NNI')
        extra_kwargs = {'password': {'write_only': True}}
class Edituser(forms.ModelForm):
     class Meta:
        model = User
        fields = ('id', 'username', 'email','NNI')
class Editfil(forms.ModelForm):
     class Meta:
        model = Filiere
        fields = ('__all__')
class Editmat(forms.ModelForm):
     class Meta:
        model = Matiere
        fields = ('__all__')
