from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from main.models import Plan, System
from accounts.models import Investments
import datetime 
# Create your views here.
@csrf_exempt
def invest(request):
    response = {}
    response['status'] = False
    data = JSONParser().parse(request)
    plan = Plan.objects.filter(dividend=float(data['plan'])).first()
    
    if plan is None:
        response['status'] = False
        response['message'] = "Invalid plan"
        return JsonResponse(response, safe=False)

    investmentday = datetime.date.today()
    returndate = datetime.date.today() + datetime.timedelta(days=30)

    if request.user == 'AnonymousUser' or request.user == 'AnonymousUser':
        response['status'] = False
        response['message'] = "Something went wrong, please refresh the page!!!"
        return JsonResponse(response, safe=False)
    status = "pending"
    addInvestment = Investments(user=request.user, plan=plan, deposit=float(data['deposit']), amountreturn=float(data['amountreturn']), btcdeposit=float(data['btcdeposit']), btcreturn=float(data['btcreturn']), status=status)
    addInvestment.save()
    response['status'] = True
    response['message'] = "Success"
    
    return JsonResponse(response, safe=False)