from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse
from app_profiles.forms import UserRegisterForm, AuthForm
from app_profiles.models import Profile

from django.db.models import F

from app_profiles.utils import buy_select_product

def RegisterView(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            cd = form.cleaned_data
            Profile.objects.create(user=user,
                                   first_name=cd['first_name'],
                                   last_name=cd['last_name'],
                                   date_of_birthday=cd['date_of_birthday'])
            user = authenticate(username=cd['username'], password=cd['password1'])
            login(request, user)
            return redirect(reverse('personal_account'))
    form = UserRegisterForm()
    return render(request, 'app_profiles/register_page.html', {'form': form})


def PersonalAccount(request):
    form = AuthForm()
    return render(request, 'app_profiles/personal_account.html', {'form': form})


def TopUp(request):
    if request.method == 'POST':
        profile = request.user.profile
        profile.balance += int(request.POST['count'])
        profile.save()
        return redirect(reverse('personal_account'))


def BuyProduct(request, shop_id, product_id):
    try:
        buy_select_product(request, shop_id, product_id)
        return HttpResponse('Товар куплен')
    except Exception as err:
        return HttpResponse(err.args)



def AuthView(request):
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse('personal_account'))
                else:
                    return HttpResponse('Пользователь не активен')
            else:
                return HttpResponse('Такого пользователя не существует')
        else:
            return HttpResponse('Проверьте правильность заполнения формы')
    form = AuthForm()
    return render(request, 'app_profiles/auth_page.html', {'form': form})
