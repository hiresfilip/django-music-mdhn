from django.shortcuts import render
from django.views.generic import DetailView, ListView
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


class InstrumentListView(ListView):
    model = Instrument

    context_object_name = 'instrument_list'
    template_name = 'instrument/list.html'
    paginate_by = 6


    def get_queryset(self):
        if 'type_name' in self.kwargs:
            return Instrument.objects.filter(type__name=self.kwargs['type_name']).all() # Get 5 books containing the title war
        else:
            return Instrument.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        if 'type_name' in self.kwargs:
            context['view_title'] = f"Typ: {self.kwargs['type_name']}"
            context['view_head'] = f"Typ nástroje: {self.kwargs['type_name']}"
        else:
            context['view_title'] = 'Typy'
            context['view_head'] = 'Přehled typů nastoje'
        return context
