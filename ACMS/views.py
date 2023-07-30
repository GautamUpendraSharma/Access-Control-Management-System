from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
def Homepage(request):
    return render(request,"index.html")

def Loginpage(request):
    return render(request,"Login.HTML")

def ContactUs(request):
    return render(request,"contact.html")

def Help(request):
    return render(request,"help.html")

def Services(request):
    return render(request,"services.html")

def Getdetails(request):
    return render(request,"getdetails.html")

def run_python_code(request):
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    local_ip_address = s.getsockname()[0]
    s.close()
    result = "local_ip_address"
    data = {'result': result}
    return JsonResponse(data)