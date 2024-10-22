from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request,'login.html')

def home_view(request):
    return render(request,'home.html')

def labaratory_view(request):
    return render(request,'labaratory.html')

def lab_attendant_view(request):
    return render(request,'lab_attendant.html')

def computers_view(request):
    return render(request,'computers.html')




