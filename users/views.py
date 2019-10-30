import uuid
from django.template import RequestContext, Template
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import Context
from django.utiles.datastructure import MultiValueDictKeyError
from users.models import Users


def index(request):
    return HttpResponse('Hello, welcome')

def login(request):
    if request.method == 'GET':
        return render(
            request,
            'login.html',
            context={

            }
        )
    elif request.method == "POST":
        print(request.POST['username'], request.POST['password'])
        u = Users.objects.filter(
            username = request.POST['username'],
            password = request.POST['password']
        )
        if u:
            u[0].token = uuid.uuid4()
            u[0].save()
            return redirect(
                '/chat/'
            )
        else:
            return HttpResponse("User not found!", status=404)



def validate_user_add_request(data):
    if len(data['firstname'] < 2:
        return False, 'Firstname must be more than 2 characters', 'firstname'
    return True, ''



def user_list(request):
    if request.method == "POST":
        validate = validate_user_id_request(request.POST)
        if validate[0]:
            u = Users(
                firstname = request.POST['firstname'],
                lastname = request.POST['lastname'],
                username = request.POST['username'],
                password = '1234',
                avatar = '123qwe'
            )
            try:
            u.save()
            except:
                return HttpResponse(
                    "Duplicate",
                    status=400
                )
            return HttpResponse('Done!')
        else:
            return HttpResponse("Error", status = 400)

    elif request.method == 'GET':
        users = Users.objects.all()
        return render(
            request,
            'list.html',
            context={
                'users':users,
                'title': "List of Users",
                'test_dict':{
                    "name":"value"
                }
            }
        )