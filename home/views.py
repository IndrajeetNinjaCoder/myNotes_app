from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Note

from django.db.models import Q

def home(request):
    allNotes = []
    currentuser = request.user
    if request.user.is_authenticated:
        allNotes = Note.objects.filter(user=currentuser)  
    # print(currentuser)
    return render(request, 'home/home.html', {'allNotes': allNotes})

def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        # if len(username)<3 or len(email)<3 or len(password)<3 or len(cpassword):
        #     return 

        if password != cpassword:
            return HttpResponse("Password Does not match")

        myuser = User.objects.create_user(username, email, password)
        myuser.save()
        return redirect('home')

    else:
        return HttpResponse('<h1>404 Page Not Found</h1>')

def handleLogin(request):
    if request.method == 'POST':
        lusername = request.POST['lusername']
        lpassword = request.POST['lpassword']

        user = authenticate(username=lusername, password=lpassword)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('home')
    else:
        return HttpResponse('<h1>404 Page Not Found</h1>')

def handleLogout(request):
    logout(request)
    return redirect('home')

def addNote(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        if len(title) > 2 and len(description) > 2:
            note = Note(user=request.user, title=title, description=description)
            note.save()
            return redirect('home')
        else:
            return redirect('home')
    else:
        return HttpResponse('<h1>404 Page Not Found</h1>')

def editNote(request):
    if request.method == 'POST':
        id = request.POST['noteid']
        title = request.POST['modalTitle']
        desc = request.POST['modalDesc']

        note = Note.objects.get(id=id)
        note.title = title
        note.description = desc
        # note = Note(title=title, description=desc)
        note.save()

        # print(id, title, desc)

        return redirect('home')
    return redirect('home')

def deleteNote(request, id):
    note = Note.objects.get(id=id)
    note.delete()
    return redirect('home')

def search(request):
    currentuser = request.user;
    query = request.GET['query']
    notes = Note.objects.filter(user=currentuser)
   
    allNotes = notes.filter(Q(title__icontains=query) | Q(description__icontains=query))
  
    return render(request, 'home/home.html', {'allNotes': allNotes})

