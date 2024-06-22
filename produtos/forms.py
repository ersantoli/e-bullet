from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Gravar, boletim
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