from django.shortcuts import render

from funnys.models import Funny


def post_list(request):
    funnys = Funny.objects.all()
    return render(request, 'funnys/list.html', {'funnys': funnys})
