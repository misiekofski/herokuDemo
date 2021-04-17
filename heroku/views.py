from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView

from heroku.models import Bottle


# Create your views here.
class CellarView(View):
    def get(self, request):
        bottles = Bottle.objects.all()
        return render(request, 'cellar.html', context={'bottles': bottles})


class AddBottleView(CreateView):
    model = Bottle
    template_name = 'bottle_form.html'
    fields = ['year_produced', 'brand', 'description']
    success_url = reverse_lazy('cellar-view')


class UpdateBottleView(UpdateView):
    model = Bottle
    template_name = 'bottle_update_form.html'
    fields = ['description']
    success_url = reverse_lazy('cellar-view')
