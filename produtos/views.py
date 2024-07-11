import datetime
from tkinter import messagebox
from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Boletimb, Gravar
from .models import boletim as Boletim 
from .forms import AddRecordNotas, BoletimForm, Notas2b, SignUpForm, AddRecordForm




def index(request):
    # Check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "Voce Fez o Loggin com sucesso!")
			return redirect('index')
		else:
			messages.success(request, "Ocorreu um  Error ao Logar, Por favor tente denovo ...")
			return redirect('index')
	else:
		return render(request, 'index.html', {})

def logout_user(request):
	logout(request)
	messages.success(request, "Você foi Deslogado...")
	return redirect('index')
      
      
def aluno(request):
   regs = Gravar.objects.all()   
   
   return render(request, 'aluno.html', {'regs':regs}) 


def testnotaspage(request, matricula):
   try:
    notas= Boletim.objects.get(matricula = matricula)
    return render(request, 'testnotas.html', {'notas': notas})

   except Boletim.DoesNotExist:
    messages = "Error", "Notas Não Cadastradas"
    return render(request, 'testif.html',{'messages': messages})


		
		#return render(request, 'testnotas.html', {'notas': notas})
	
def boletim_view(request):
   
    if request.method == 'POST':
        matricula = request.POST.get('matricula')
        try:
            boletins = Boletimb.objects.get(matricula=matricula)
           
            return render(request, 'boletim_list.html', {'boletins': boletins, 'matricula': matricula})
        except Boletimb.DoesNotExist:
            messages = "Error", "Nada Cadastrado"
            return render(request, 'testif.html', {'messages': messages})
    return render(request, 'boletim_form.html')	
		
	    
def boletim(request):
    data_atual = datetime.datetime.now()
    ano = data_atual.year
    return render(request, 'boletim.html' ,{'ano': ano})
  
def testif(request):
	return render(request, 'testif.html' , {})  

def test(request, matricula):
     matricula = Gravar.objects.get(matricula=matricula)      
	 
	      
     return render(request, 'test.html', {'matricula': matricula}) 
     
def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Registro adicionado...")
				return redirect('aluno')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('index')

			                 
def add_aluno(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Registro adicionado...")
				return redirect('index')
		return render(request, 'aluno.html', {'form':form})
	else:
		messages.success(request, "Você deve estar logado...")
		return redirect('index')
			
	
def matricula_search(request):
  
    if request.method == 'POST':
       matricula = request.POST.get('matricula')
       try:
            registro = Gravar.objects.get(matricula=matricula)
           
            return render(request, 'boletim_result.html', {'registro': registro , 'matricula': matricula})
       except Gravar.DoesNotExist:
            messages = "Error", "Nada Cadastrado"
            return render(request, 'matricula_not_found.html', {'messages': messages})
    return render(request, 'boletim_form.html')	    
	
    
def att_record(request, matricula):
    if request.user.is_authenticated:
        ra =Gravar.objects.get(matricula = matricula)
        form = AddRecordForm(request.POST or None, instance=ra)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro Atualizado com Sucesso!')
            return redirect('aluno')
        return render (request, 'att_record.html', {'form': form})
        
    else:
        messages.success(request,"Você deve estar Logado para executar Isso!")
        return redirect('index')
    
def att_notas(request, matricula):
    if request.user.is_authenticated:
        ra =Boletimb.objects.get(matricula = matricula)
        form = BoletimForm(request.POST or None, instance=ra)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro Atualizado com Sucesso!')
            return redirect('aluno')
        return render (request, 'att_notas.html', {'form': form})
        
    else:
        messages.success(request,"Você deve estar Logado para executar Isso!")
        return redirect('index')
def delete_record(request, matricula):
	if request.user.is_authenticated:
		delete_it = Gravar.objects.get(matricula=matricula)
		delete_it.delete()
		messages.success(request, "Registro Apagado com Successo...")
		return redirect('aluno')
	else:
		messages.success(request, "Você deve estar Logado para executar Isso!")
		return redirect('index')



def boletim_list(request,matricula):
     try:
            data_atual = datetime.datetime.now()
            ano = data_atual.year
            boletins = Boletimb.objects.get(matricula=matricula)
            return render(request, 'boletim_list.html', {'boletins': boletins, 'matricula': matricula, 'ano': ano})
     except Boletimb.DoesNotExist:
            messages = "Error", "Nada Cadastrado"
            return render(request, 'testif.html', {'messages': messages})
    
    
    
    
    
             
def boletim_create(request):
    data_atual = datetime.datetime.now()
    ano = data_atual.year
    if request.method == 'POST':
        form = BoletimForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('aluno')
    else:
        form = BoletimForm()
    return render(request, 'boletimt_form.html', {'form': form,'ano': ano}) 
         
        

