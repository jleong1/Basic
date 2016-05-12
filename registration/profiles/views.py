from django.shortcuts import render
from .models import Profiles
from .forms import RegisterForm

def home(request):
    return render(request,'home.html')

def signin(request):
    #check form
    return render(request,'signin.html')

def signup(request):
    if request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            return render(request, 'profile.html')
        else:
            form = RegisterForm()
            return render(request, 'home.html')
    elif request.method=='GET':
        return render(request, 'signup.html')

def profile(request):
    return render(request, 'profile.html',{})

def editProfile(request):
    #GET and POST here for adding information about user, might have to split by editName,
    #edit email, edit password, etc...
    return render(request, '.html')

def uploadAvatar(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            m = Profiles.objects.get()
            m.avatar = form.cleaned_data['image']
            m.save()
            return HttpResponse('Avatar upload success')
    return HttpResponseForbidden('allowed only via POST')
