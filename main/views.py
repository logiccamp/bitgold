from main.models import Rating
from django.shortcuts import render

# Create your views here.
def main (request):
    return render(request, 'main/home.html')


def about (request):
    return render(request, 'main/aboutus.html')

def investments (request):
    return render(request, 'main/investments.html')


def faqs (request):
    return render(request, 'main/faqs.html')


def ratings (request):
    rating = Rating.objects.all()
    return render(request, 'main/ratings.html', {'ratings':rating})



def support (request):
    return render(request, 'main/support.html')
