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

    commission_form = CommissionForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if commission_form.is_valid():
            commission = commission_form.save(commit=False)
            commission.user_id = user_id
            commission.save()
            messages.success(request, "Commission created successfully!")
            return render(request, "contact/commission_success.html")

    context = {
        'commission_form': commission_form
    }
    return render(request, "contact/commission.html", context)


@login_required
def my_commissions(request):
    """
    A view to render the user's commissions
    """
    commissions = None
    try:
        commissions = Commission.objects.filter(user=request.user)
    except Commission.DoesNotExist:
        pass

    return render(request, 'contact/my_commissions.html', {'commissions': commissions})


@login_required
def commission_success(request):

    template = 'contact/commission_success.html'
    return render(request, template)
