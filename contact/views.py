from django.shortcuts import render
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
        messages.info(
                    request, "Thank you for your enquiry!")

    context['form'] = form
    return render(request, "contact/commission.html", context)


@login_required
def my_commissions(request):

    return render(request, 'contact/my_commissions.html')
