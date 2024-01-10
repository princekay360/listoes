from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect

from client.models import Client


def index(request):
    is_login = 'false'
    try:
        try:
            client = Client.objects.get(pk=request.session.get("client_id"))
            is_login = "true"
            context = {
                'is_login': is_login,
                'client': client,
            }
        except KeyError:
            context = {
                'is_login': is_login,
                'client': '',
            }
    except ObjectDoesNotExist:
        context = {
            'is_login': is_login,
            'client': '',
        }

    return render(request, 'index.html', context=context)


def generate_id():
    no = str(Client.objects.all().count() + 1)
    cid = 'LCL' + no
    return cid


def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        gender = request.POST['gender']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']

        try:
            if Client.objects.get(phone=phone) or Client.objects.get(email=email):
                print("already exist")
        except ObjectDoesNotExist:
            new_member = Client(
                id=generate_id(), name=name, gender=gender, phone=phone, email=email, password=password
            )
            new_member.save()
            redirect("client_login")
    context = {
        'is_login': 'false',
        'client': '',
    }
    return render(request, 'signup.html', context)


def login(request):
    try:
        try:
            client = Client.objects.get(pk=request.session.get("client_id"))
            return redirect('client_index')
        except KeyError:
            pass
    except ObjectDoesNotExist:
        pass

    if request.method == 'POST':
        ep = request.POST['ep']
        password = request.POST['password']

        try:
            if Client.objects.get(email=ep).password == password or Client.objects.get(phone=ep).password == password:
                request.session['client_id'] = Client.objects.get(email=ep).id
                return redirect('client_index')
        except ObjectDoesNotExist:
            return redirect("client_login")

    context = {
        'is_login': 'false',
        'client': '',
    }
    return render(request, 'login.html', context)


def logout(request):
    request.session['client_id'] = None
    return redirect('client_login')


def profile(request):
    try:
        try:
            client = Client.objects.get(pk=request.session.get("client_id"))
            is_login = "true"
            context = {
                'is_login': is_login,
                'client': client,
            }
            return render(request, 'profile.html', context=context)
        except KeyError:
            return redirect('client_login')
    except ObjectDoesNotExist:
        return redirect('client_login')
