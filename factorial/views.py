from django.shortcuts import render, redirect

from django.contrib.auth.models import User, auth




# Create your views here.


def createForm(request):
    return render(request, 'factorial/input.html')

def fact(request):
   number = request.POST['number']
   # factorial(number)

   number = int(number)
   if number == 0:
       return 1
   f = number * factorial(number-1)
   # print(f)
   n = str(f)
   count = len(n)
   # print(n)
   # print(count)
   i = count - 1
   # print(n[i])
   xx = 0
   while True:
      ii = n[i]
      if ii.strip() == '0':
         i -= 1
         xx += 1
         # print(xx) 
      elif ii.strip() != '0':
         # print("stop")
         break
   # print(xx)
   # return(f)
   
   return render(request, 'factorial/showfac.html', {'number': number,'total':f,'zero':xx})

def factorial(number):
   number = int(number)
   if number == 0:
        return 1
   f = number * factorial(number-1)
   # print(f)

   n = str(f)
   count = len(n)
   # print(n)
   # print(count)
   i = count - 1
   # print(n[i])
   xx = 0
   while True:
      ii = n[i]
      if ii.strip() == '0':
         i -= 1
         xx += 1
         # print(xx)
      elif ii.strip() != '0':
         # print("stop")
         break
   # print(xx)

   return(f)


   
      
   

