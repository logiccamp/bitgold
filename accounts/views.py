from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .models import Investments, userprofile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
# Create your views here.
def loginpage (request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        if username == '' or password == '':
            message = 'Invalid login'
            return render(request, 'accounts/login.html', {'message':message})

        check_user = User.objects.filter(username=username).first()
        if check_user is None:
            message = 'Email does not exist in the database'
            return render(request, 'accounts/login.html', {'message':message})

        user = authenticate(username=username, password=password)
        if user:
            login(request, check_user)
            return redirect('homepage')
        else:
            message = 'Invalid login credentials'
            return render(request, 'accounts/login.html', {'message':message})
    return render(request, 'accounts/login.html')


def registerpage (request):
    if request.method == 'POST':
        
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email1 = request.POST['email1']
        email2 = request.POST['email2']
        wallet = request.POST['pay_account']
        securityquestion = request.POST['sq']
        securityanswer = request.POST['sa']
        agree = request.POST['agree']

        if not agree:
            message = "You must agree with terms and condition"
            return render(request, 'accounts/signup.html', {'message':message}) 

        if password1 == '' or username == '' or email1 == '' or securityquestion == '' or securityanswer == '': 
            message = "All fields are required"
            return render(request, 'accounts/signup.html', {'message':message}) 
        
        if password1 != password2:
            message = "Password do not match"
            return render(request, 'accounts/signup.html', {'message':message}) 

        if email1 != email2:
            message = "Email and confirm email must be the same"
            return render(request, 'accounts/signup.html', {'message':message}) 

        
        user = User(username=username, email=email1)
        user.set_password(password1)
        user.save()

        userpro = userprofile(user=user, BitcoinWallet=wallet, SecretQuestion=securityquestion, SecretAnswer=securityanswer)
        userpro.save()
        login(request, user)
        return redirect('homepage')
    return render(request, 'accounts/signup.html') 




def signout(request):
    logout(request)
    return redirect('homepage')


@login_required
def myaccount(request):
    myinvestments = Investments.objects.filter(user=request.user)
    return render(request, 'accounts/myaccount.html', {'myinvestments' : myinvestments})


@login_required
def invest(request):
    if request.method == 'POST':
        investment = {}
        user = request.user
        investment['planname'] = request.POST['planname']
        investment['deposit'] = request.POST['deposit']

        investment['return'] = request.POST.get('btcreturn')
        investment['btcdeposit'] = request.POST.get('btcdeposit')
        investment['amountreturn'] = request.POST.get('amountreturn')

    return render(request, 'accounts/investnow.html')

@login_required
def compelteinvestment(request):
    investment = Investments.objects.filter(user=request.user).last()
    return render(request, 'accounts/complete-investment.html', {"investment":investment})

