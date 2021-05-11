from django.shortcuts import render
from django.views.generic import ListView, View,  DetailView, UpdateView, DeleteView, ListView
from deposits.models import Deposit
from django.urls import reverse_lazy


from .forms import DepositAddForm


class AddDepositView(View):
    def post(self, request):

        form = DepositAddForm(request.POST)
        if form.is_valid():
            u = form.save()
            deposit = Deposit.objects.all()

            return render(request, 'index.html', {'deposits': deposit})

    def get(self, request):
        form_class = DepositAddForm

        return render(request, 'depositadd.html', {
            'form': form_class,
        })
class IndexView(ListView):
    model = Deposit

class GetDepositView(DetailView):
    model = Deposit
