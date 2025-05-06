from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def monthly_challenge_by_number(request, month):
    return HttpResponse(month)

def monthly_challenge(request, month):
    challenge_text = None

    if month == 'january':
        challenge_text = "Write plans for starting year"
    elif month == 'february':
        challenge_text = "Walk at least 30 minutes per day"
    elif month == 'march':
        challenge_text = "Read book at leat 20 minutes per day"
    elif month == 'april':
        challenge_text = "Walk at least 30 minutes per day"
    elif month in ['may','june', 'july']:
        challenge_text = "Reduce weight with 1 kilogram"
    elif month == 'august':
        challenge_text = "Go on holiday"
    elif month in ['september', 'october', 'november', 'december']:
        challenge_text = "Maintain weight and read book at least 20 minutes per day"
    else:
        return HttpResponseNotFound("Wrong month")
    return HttpResponse(challenge_text)
