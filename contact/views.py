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
    page_name = "Commission Page"
    page_description = "Request a commission here!"
    context = {}

    commission_form = CommissionForm(
        request.POST or None,
        request.FILES or None
    )

    if request.method == 'POST':
        if commission_form.is_valid():
            commission = commission_form.save(commit=False)
            commission.user_id = user_id
            commission.save()
            return render(request, "contact/commission_success.html")

    context = {
        'commission_form': commission_form,
        'page_name': page_name,
        'page_description': page_description
    }
    return render(
        request, "contact/commission.html", context)


@login_required
def my_commissions(request):
    """
    A view to render the user's commissions
    """
    page_name = "My Commissions"
    page_description = "Go here to see your commission requests"
    commissions = None
    try:
        commissions = Commission.objects.filter(
            user=request.user).order_by('-last_modified')
    except Commission.DoesNotExist:
        pass
    context = {
        'page_name': page_name, 'page_description': page_description,
        'commissions': commissions}
    return render(request, 'contact/my_commissions.html', context)


@login_required
def commission_success(request):
    page_name = "Commission Success"
    page_description = "You have successfully requested a commission!"

    context = {'page_name': page_name, 'page_description': page_description}
    template = 'contact/commission_success.html'
    return render(request, template, context)
