from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import RegistrationForm,UserDataForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')  # Redirect to success page
    else:
        form = RegistrationForm()

    return render(request, 'registration/wld.html', {'form': form})

def registration_success(request):
    return render(request, 'registration/success.html')

from .forms import UserDataForm
# myapp/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import UserDataForm

@csrf_exempt
def user_data_submit_ajax(request):
    if request.method == 'POST':
        form = UserDataForm(request.POST)
        if form.is_valid():
            form.save()
       
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def admin_redirect_view(request):
    return redirect('admin:index')
