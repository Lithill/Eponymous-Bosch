from django.shortcuts import render, redirect, reverse, HttpResponse
from .forms import CommissionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def contact(request):

    return render(request, "contact.html", context)


@login_required
def commission(request):
    context = {}

    form = CommissionForm(request.POST or None, request.FILES or None)

    if form.is_valid():

        form.save()
        return render(request, "contact/commission_success.html")

    context['form'] = form
    return render(request, "contact/commission.html", context)


@login_required
def my_commissions(request):

    return render(request, 'contact/my_commissions.html')


def commission_success(request):

    template = 'contact/commission_success.html'
    return render(request, template)
