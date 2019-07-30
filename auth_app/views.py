from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from django.http import JsonResponse

def login_view(request):
    if request.method == 'POST':
        user = authenticate(email=request.POST.get('email'), password=request.POST.get('pass'))
        if user is not None:
             login(request, user)
             return redirect('dashboard')
        else:
            messages.error(request, 'Username or password incorrect')
            return redirect('login')
    return render(request, 'login-template.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(request,
                                    username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


@csrf_exempt
def check_availability(request):
    data = {'msg': ''}
    User = get_user_model()
    if request.method == 'GET':
        email = request.GET.get('email')
        exists = User.objects.filter(email=email).exists()
        if exists:
            data['msg'] = 'found'
    return JsonResponse(data)
