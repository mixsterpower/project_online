from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from django.contrib.auth import authenticate, login,logout
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    context = {
        'test' : 'Hello',
    }

    return render(request,'index.html',context)

def login_view(request):
    if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/main')
            else:
                return JsonResponse({'error': 'Username or password wrong!!!!'}, status=401)
    else:
        return JsonResponse({'error': 'Username or password wrong!!!!'}, status=400)

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def home(request):
    context = {
        'test' : 'Hello',
    }


    return render(request,'main.html',context)

