from django.shortcuts import render
from django.utils import timezone
from .models import Post


def main(request):
	return render(request, 'News_page.html')

def News_page(request):
	return render(request, "News_page.html")

def sportspage(request):
	return render(request, "sportspage.html")


# Create your views here.
