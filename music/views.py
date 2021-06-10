from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from .forms import InstrumentModelForm
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


class InstrumentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Instrument
    fields = ['title', 'history', 'poster', 'type']
    #form_class = InstrumentModelForm
    template_name = 'music/instrument_create_bootstrap_form.html'
    login_url = '/accounts/login/'
    permission_required = 'music.add_instrument'

class InstrumentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Instrument
    form_class = InstrumentModelForm
    template_name = 'music/instrument_bootstrap_form.html'
    login_url = '/accounts/login/'
    permission_required = 'music.change_instrument'


class InstrumentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Instrument
    success_url = reverse_lazy('instrument_list')
    login_url = '/accounts/login/'
    permission_required = 'music.delete_instrument'




def error_404(request, exception=None):
        return render(request, 'errors/404.html')


def error_500(request):
    return render(request, 'errors/500.html')


def error_403(request, exception=None):
    return render(request, 'errors/403.html')


def error_400(request, exception=None):
    return render(request, 'errors/400.html')