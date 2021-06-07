from django.contrib import auth
from django.http import HttpResponseRedirect
from django.http.response import JsonResponse
from rest_framework import status



def login(request,usernam,passw):
    user = auth.authenticate(username=usernam, password=passw)

    if user is not None:
            auth.login(request, user)
            status = True
            return JsonResponse({'status': status})
    else :
        status = False
        return JsonResponse({'status':status})
    
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")
