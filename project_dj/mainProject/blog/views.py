from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author' : 'Alpha',
        'title' : 'backend eng',
        'content': 'my  incredible journey',
        'date_posted': '27th August 2024'
    },
    {
        'author': 'Sandy',
        'title': 'lecturer',
        'content': 'data science',
        'date_posted': '12th july  2024'
    },
    {
        'author': 'brian',
        'title': 'doctor',
        'content': 'medicine',
        'date_posted': '27th August 2026'
    },

]




def Homepage(request):
    context = {
        'posts': posts
    }
    return render(request, 'home.html', context)
def about(request):
    return render(request, 'about.html', {'title': ' blog about page'})