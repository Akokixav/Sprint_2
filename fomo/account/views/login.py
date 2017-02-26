# from django import settings
from django.http import HttpResponseRedirect
from django_mako_plus import view_function
# from django.contrib.auth import authenticate, login
#
# from .. import dmp_render, dmp_render_to_string

from django.contrib.auth import authenticate, login

@view_function
def process_request(request):
    

    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username = username, password = password)


    #log the user in
    if user is not None:
        login(request, user)

    #go to the HTTP page
        return HttpResponseRedirect('/homepage/index/')

    return HttpResponseRedirect('/homepage/index')
