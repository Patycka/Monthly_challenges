from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Write plans for new year",
    "february": "Walk at least 30 minutes per day",
    'march': "Read book at leat 20 minutes per day",
    'april': "Walk at least 30 minutes per day",
    'may': "Reduce weight with 1 kilogram",
    'june':"Reduce weight with 1 kilogram",
    'july': "Reduce weight with 1 kilogram",
    'august': "Go on holiday",
    'september': "Maintain weight and read book at least 20 minutes per day",
    'october': "Maintain weight and read book at least 20 minutes per day",
    'november': "Maintain weight and read book at least 20 minutes per day",
    'december': "Maintain weight and read book at least 20 minutes per day",
}

# Create your views here.

'''
Function changes number of the month written in url to the name of the month.
Next the view is changed to the view of specific month (monthly_challenge() is called). 
'''
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Wrong month")
    month_name = months[month-1]
    redirect_path = reverse("month-challenge", args=[month_name])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, 'challenges/challenge.html', {'text': challenge_text, 'month': month})
    except:
        return HttpResponseNotFound("<h1>Wrong month</h1>")

'''
Function shows all challenges as clickable link
'''
def show_all_challenges(request):
    response_data = "<ul>"
    for month in monthly_challenges.keys():
        month_path = reverse("month-challenge", args = [month])
        response_data += f'<li><a href="{month_path}">{month}</a></li>'
    response_data += '</ul>'
    return HttpResponse(response_data)
