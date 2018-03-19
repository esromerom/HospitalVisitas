from django.shortcuts import redirect, HttpResponse

# Create your views here.

def redireccion_login(request):
    return redirect('Hospital/home')
def redireccion_home(request):
    return redirect('home')