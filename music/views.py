from django.shortcuts import render
from .models import Instrument


def index(request):
    instruments = Instrument.objects.order_by('title')[:3]

    context = {
        'instruments': instruments,
    }

    return render(request, 'index.html', context=context)
