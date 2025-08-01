from django.shortcuts import render, HttpResponse, redirect
from test_app.models import test 


# Create your views here.
def home(request):

     return render(request, 'home.html')
     
def web(request):    
     return render(request,'web.html')

def form(request):
    if request.method == 'POST':
        var1 = request.POST.get('name')
        var2 = request.POST.get('contact')

        # Save data in DB
        test_instance = test(name=var1, number=var2)
        test_instance.save()

        return redirect('form')  # Redirect to home page

    return render(request, 'form.html')