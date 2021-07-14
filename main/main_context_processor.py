from .models import Plan, System
import requests
from accounts.models import Investments
def systemprocessor (request) :
    system = System.objects.all()
    return {'system':system}


def planprocessor (request) :
    plan = Plan.objects.all()
    return {'plans':plan}


def bitcoinprice (request):
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    return {'coins' : data}
