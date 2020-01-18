from django.shortcuts import render, redirect, get_object_or_404
from .models import Rule
from .forms import RulesForm
import csv


def index(request):
    return render(request, 'loan/home.html', context)

def display_rules(request):
    my_rule = Rule.objects.get(pk=1)
    context = {
        'my_rule': my_rule
    }
    return render(request, 'loan/display_rules.html', context)

def rules(request, id=None):
    if id:
        rule = get_object_or_404(Rule, pk=id)
    else:
        rule = Rule()

    form = RulesForm(request.POST or None, instance=rule)
    if request.POST and form.is_valid():
        form.save()
        return redirect("display_rules")

    context = {
        'my_form': form
    }
    return render(request, 'loan/rules.html', context)
