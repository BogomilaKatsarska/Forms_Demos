from django import forms
from django.shortcuts import render

from Forms_Demos.web.forms import NameForm, PersonForm
from Forms_Demos.web.models import Person


def index(request):
    name = None
    if request.method == 'GET':
        form = NameForm()
    else:
        form = NameForm(request.POST)
        if form.is_valid():
        # 1.checks if the entered data is valid
        # 2.fills in the data in cleaned_data
            name = form.cleaned_data['your_name']
            Person.objects.create(name=name)

    context = {
        'form': form,
        'name': name,
    }
    return render(request, 'index.html', context)


def index_model_form(request):
    if request.method == 'GET':
        form = PersonForm()
    else:
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form': form,
    }
    return render(request, 'model_forms.html', context)
