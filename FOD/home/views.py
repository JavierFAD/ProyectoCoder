from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def contact(request):
    return render(request, 'contact.html')

def post(request):
    return render(request, "post.html")

def post2(request):
    return render(request, "post2.html")

def about(request):
    return render(request, "about.html")
