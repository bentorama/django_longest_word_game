from django.shortcuts import render
from django.http import HttpResponse
import string, random

# Create your views here.
def new(request):
  alphabet_string = string.ascii_uppercase
  alphabet_list = list(alphabet_string)
  letters_list = random.sample(alphabet_list, 10)
  context = {
    'letters': letters_list
  }
  return render(request, "longest_word/new.html", context)