from django.shortcuts import render
from django.views.generic import DetailView
from .models import Instrument


def index(request):
    instruments = Instrument.objects.order_by('title')[:3]

    context = {
        'instruments': instruments,
    }

    return render(request, 'index.html', context=context)


class InstrumentDetailView(DetailView):
    model = Instrument

    context_object_name = 'instrument_detail'
    template_name = 'instrument/detail.html'