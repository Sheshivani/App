from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Register
from django.db.models import Q
from django.contrib import messages
from django.http import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import serializerpersons

# Create your views here.

def indexView(request):
    return render(request,'index.html')

@login_required
def dashboardView(request):
    return render(request,'dashboard.html')

def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()

    return render(request,'registration/register.html',{'form':form})


def registration(request):
    return render(request,'registration.html')

def nextPage(request):
    fname = request.POST.get("fname")
    lname = request.POST.get("lname")
    contact = request.POST.get("contact")
    email = request.POST.get("email")

    register = Register(first_name=fname,last_name=lname, contact=contact, email=email)
    register.save()
    return render(request,'registration.html', {"message":"Detail registered!!"})

def search(request):
    if request.method == 'POST':
        srch = request.POST['srh']

        if srch:
            match = Register.objects.filter(Q(first_name__icontains=srch) |
                                            Q(contact__icontains=srch)
                                            )
            if match:
                return render(request,'search.html',{'sr':match })
            else:
                messages.error(request,'no result found')
        else:
            return HttpResponseRedirect('/search/')

    return render(request,'search.html')

class registerList(APIView):

    def get(self, request):
        person1 = Register.objects.all()
        serializers = serializerpersons(person1, many= True)
        return Response(serializers.data)

    def post(self):
        pass






