from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import LoginForm,CreateUserForm, CreateRecordForm, UpdateRecordForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Record
from django.contrib import messages


def home(request):
    
    return render(request,'crm/index.html',{})


# register a user
def register(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Cuenta creada con éxito.')
            return redirect('login')
    context={'form':form}
    return render(request,'crm/register.html',context)


# login a user
def login_user(request):
    form=LoginForm()
    if request.method=='POST':
        form=LoginForm(request, data=request.POST)
        if form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('dashboard')    
        else:
            messages.success(request,'Hubo un error con el ingreso. Por favor inténtalo de nuevo.')
    context={'form':form}
    return render(request,'crm/login.html',context)


# dashboard
@login_required(login_url='login')
def dashboard(request):
    records=Record.objects.all()
    context={
        'records':records
    }
    return render(request,'crm/dashboard.html',context)


@login_required(login_url='login')
def create_record(request):
    form=CreateRecordForm()
    if request.method=='POST':
        form=CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Registro creado con éxito.')
            return redirect('dashboard')
    context={
        'form':form
    }
    return render(request,'crm/create_record.html',context)


@login_required(login_url='login')
def update_record(request,pk):
    record=Record.objects.get(id=pk)
    form=UpdateRecordForm(instance=record)
    if request.method=='POST':
        form=UpdateRecordForm(request.POST,instance=record)
        if form.is_valid():
            form.save()
            messages.success(request,'Registro actualizado con éxito.')
            return redirect('dashboard')
    context={
        'form':form
    }        
    return render(request,'crm/update_record.html',context)


@login_required(login_url='login')
def view_record(request,pk):
    all_records=Record.objects.get(id=pk)
    context={
        'record':all_records
    }
    return render(request,'crm/view_record.html',context)


@login_required(login_url='login')
def delete_record(request,pk):
    record=Record.objects.get(id=pk)
    record.delete()
    messages.success(request,'Registro eliminado con éxito.')
    return redirect('dashboard')
    

# user logout
def user_logout(request):
    auth.logout(request)
    messages.success(request,'Has salido de tu cuenta.')
    return redirect('login')
            

