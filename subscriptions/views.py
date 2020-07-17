from django.shortcuts import render, redirect
from .models import  Subscription
from django.contrib import messages

def subscriptions(request):
    subs= Subscription.objects.order_by('-expiry_date')
    context={
        'subs': subs
    }
    return render(request, 'pages/subscriptions.html', context)
