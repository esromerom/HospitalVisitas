from django.shortcuts import redirect, HttpResponse

# Create your views here.

def redireccion_login(request):
    return redirect('Hospital/')
def redireccion_home(request):
    return redirect('Hospital/')