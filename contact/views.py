from django.shortcuts import render, redirect, reverse, HttpResponse
from .forms import CommissionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from contact.models import Commission


def contact(request):

    return render(request, "contact.html", context)


@login_required
def commission(request, user_id):
    context = {}

    form = CommissionForm(request.POST or None, request.FILES or None)

    if form.is_valid():

        form.save()

        # If user has no commission setup, create one
        commission, _ = Commission.objects.get_or_create(user=request.user)

        # Add item to commissions
        commission.add()

        return render(request, "contact/commission_success.html")

    context['form'] = form
    return render(request, "contact/commission.html", context)


@login_required
def my_commissions(request):
    """
    A view to render the user's commissions
    """
    commission = None
    try:
        commission = Commission.objects.get(user=request.user)
    except Commission.DoesNotExist:
        pass

    context = {
        'commission': commission,
    }

    return render(request, 'contact/my_commissions.html', context)


@login_required
def commission_success(request):

    template = 'contact/commission_success.html'
    return render(request, template)
