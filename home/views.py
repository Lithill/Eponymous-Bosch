from django.shortcuts import render


def index(request):
    """ A view to return the index page """
    page_name = "Home Page"
    page_description = "The home page of Eponymous Bosch"

    context = {'page_name': page_name, 'page_description': page_description}
    return render(request, 'home/index.html', context)
