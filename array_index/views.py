from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
import numpy as np


# Create your views here.

def gen(request):
   largest = None

   numbers = np.random.randint(100, size=(7))
   interval = np.array(numbers)
   

   for arr in interval:
      if largest is None or arr > largest:
         largest = arr

   answer = interval.tolist().index(largest)
   return render(request, 'array/index.html', {'interval': interval, 'answer': answer, 'largest': largest})


def number(interval):
   
   for arr in interval:
      if largest is None or arr > largest:
         largest = arr

   answer = interval.index(largest)
   print(answer)

