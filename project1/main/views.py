from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from .forms import Image
from .models import LoadMultipleImages
from .db import *

# Create your views here.

def index(request):
    currentType = 'All'
    return render(request, 'main\index.html', {'owns': owns, 'types': types, 'currentType': currentType, 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})

def login(request):
    if request.method == 'POST':
        luser = request.POST

        for _user in users:
            if _user['login'] == luser['login'] and _user['password'] == luser['password']:
                global isLogin, isAdmin, user
                isLogin = True
                isAdmin = bool(_user['isAdmin'])
                user = _user
                
                return render(request, 'main\index.html', {'owns': owns, 'types': types, 'currentType': currentType, 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})
        return render(request, 'main/login.html', {'isFailed': True, 'types': types})
    else: return render(request, 'main/login.html', {'types': types})

def reg(request):
    if request.method == 'POST':
        ruser = request.POST
        form = Image(ruser, request.FILES)

        if form.is_valid():
            form.save()
            img_obj = form.instance

            global users, user, isLogin, isAdmin

            for _user in users:
                if _user['login'] == ruser['login']:
                    return render(request, 'main/reg.html', {'form': Image, 'types': types})

            users.append({
                'login': ruser['login'],
                'password': ruser['password'],
                'isAdmin': False,
                'img': img_obj.image.url
            })

            isLogin = True
            isAdmin = False
            user = users[len(users) - 1]
            

            return render(request, 'main\index.html', {'owns': owns,  'types': types, 'currentType': currentType,  'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})
    else: return render(request, 'main/reg.html', {'form': Image, 'types': types})

def Exit(request):
    global isAdmin, isLogin, user
    isAdmin = False
    isLogin = False
    user = None

    
    return render(request, 'main\index.html', {'owns': owns, 'types': types, 'currentType': currentType, 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})

def Sort(request):
    global currentType
    currentType = request.POST['type']
    
    return render(request, 'main\index.html', {'owns': owns, 'types': types, 'currentType': currentType, 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})
    
def Search(request):
    resul = []
    
    for item in owns:
        if str(item['street']).lower() == request.POST['Search'].lower() or str(item['street']).lower().__contains__(request.POST['Search'].lower()) or str(item['city']).lower() == request.POST['Search'].lower() or str(item['city']).lower().__contains__(request.POST['Search'].lower()):
            if currentType != None and item['type'] == currentType:
                resul.append(item)
            else:
                resul.append(item)

    if len(resul) > 0:
        return render(request, 'main\index.html', {'owns': resul, 'types': types, 'currentType': currentType, 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})
    else:
        if currentType == None:
            return render(request, "main\Error.html", {'error': "По запросу '" + request.POST['Search'] + "' ничего не найдено!"})
        else:
            return render(request, "main\Error.html", {'error': "В категории '" + currentType + "' по запросу '" + request.POST['Search'] + "' ничего не найдено!"})

def RemoveOwn(request):
    street = request.POST['street']

    _list = []

    for item in owns:
        if item['street'] != street:
            _list.append(item)

    owns.clear()
    for item in _list:
        owns.append(item)

    return render(request, 'main\index.html', {'owns': owns, 'types': types, 'currentType': currentType, 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})

def About(request):
    if request.method == 'POST':
        pass
    else:
        own = GetHouseByStreet(request.GET['street'])

        return render(request, 'main/about.html', {'user': user, 'isLogin': isLogin, 'types': types, 'own': own})


def CreateOwn(request):
    if request.method == 'POST':
        _own = request.POST
        
        form = Image(_own, request.FILES)

        if form.is_valid():
            form.save()
            img_obj = form.instance

            owns.append({
                'street': _own['street'],
                'city': _own['city'],
                'type': _own['type'],
                'img': img_obj.image.url,
                'price': float(_own['price']),
                'about': _own['about'],
                'raiting': _own['raiting']
            })
        return render(request, 'main\index.html', {'owns': owns, 'types': types, 'currentType': currentType, 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})
    else:
        return render(request, 'main\CreateOwn.html', {'types': types, 'form': Image, 'isLogin': isLogin, 'user': user})

def ChangeOwn(request):
    if request.method == 'POST':
        _own = request.POST

        for own in owns:
            if own['street'] == _own['oldStreetName']:

                own['street'] = _own['street']
                own['city'] = _own['city']
                own['type'] = _own['type']
                own['img'] = _own['img']
                own['price'] = float(_own['price'])
                own['about'] = _own['about']
                own['raiting'] = int(_own['raiting'])

                break

        return render(request, 'main\index.html', {'owns': owns, 'types': types, 'currentType': currentType, 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})
    else:

        for own in owns:
            if own['street'] == request.GET['street']:
                return render(request, 'main\ChangeOwn.html', {'types': types, 'own': own, 'user': user, 'isLogin': isLogin})