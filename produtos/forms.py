from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Gravar, boletim, boletim2b,Boletimb
from produtos import models

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	nome = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	#last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))


	class Meta:
		model = User
		fields = ('nome',  'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	




# Create Add Record Form
class AddRecordForm(forms.ModelForm):
	matricula = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Matricula", "class":"form-control"}), label="")
	nome = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Nome", "class":"form-control"}), label="")
	
	email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")
	genero = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Genero", "class":"form-control"}), label="")
	endereco = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Endereço", "class":"form-control"}), label="")
	nascido = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Nascimento", "class":"form-control"}), label="")
	contato = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Contato", "class":"form-control"}), label="")
	cidade = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Cidade", "class":"form-control"}), label="")
	estado = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Estado", "class":"form-control"}), label="")
	

	class Meta:
		model = Gravar
		exclude = ("criado_em"),

class AddRecordNotas(forms.ModelForm):
	matricula = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Matricula", "class":"form-control"}), label="")
	nome = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Nome", "class":"form-control"}), label="")	
	matematica = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Matematica", "class":"form-control"}), label="")
	portugues = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Português", "class":"form-control"}), label="")
	fisica = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Fisica", "class":"form-control"}), label="")
	quimica  = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Quimica", "class":"form-control"}), label="")
	ingles = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Ingles", "class":"form-control"}), label="")
	geografia = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Geografia", "class":"form-control"}), label="")
	historia = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Historia", "class":"form-control"}), label="")
	ciencias = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Ciências", "class":"form-control"}), label="")

	class Meta:
		model = boletim
		exclude = (""),
  
class Notas2b(forms.ModelForm):
	
	matematica1b = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Matematica", "class":"form-control"}), label="")
	portugues1b = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Português", "class":"form-control"}), label="")
	

	class Meta:
		model = boletim2b
		exclude = (""),
  
class BoletimForm(forms.ModelForm):
    class Meta:
        model = Boletimb
        fields = [
            'aluno', 'matricula', 
            'ciencias_bim1', 'ciencias_bim2', 'ciencias_bim3', 'ciencias_bim4',
            'matematica_bim1', 'matematica_bim2', 'matematica_bim3', 'matematica_bim4',
            'geografia_bim1', 'geografia_bim2', 'geografia_bim3', 'geografia_bim4',
            'historia_bim1', 'historia_bim2', 'historia_bim3', 'historia_bim4',
            'portugues_bim1', 'portugues_bim2', 'portugues_bim3', 'portugues_bim4',
            'ingles_bim1', 'ingles_bim2', 'ingles_bim3', 'ingles_bim4',
            'fisica_bim1', 'fisica_bim2', 'fisica_bim3', 'fisica_bim4',
            'quimica_bim1', 'quimica_bim2', 'quimica_bim3', 'quimica_bim4'
        ]  