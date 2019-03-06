from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def food(request):
    return render(request,'food.html')

def game(request):
    return render(request,'game.html')

def career(request):
    return render(request,'career.html')

def demo(request):
    return render(request,'demo.html')

def chrono(request):
    return render(request, 'chrono.html')

def contact(request):
    return render(request, 'contact.html')

def posts(request):
    return render(request, 'posts.html')