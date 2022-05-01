from django.shortcuts import render, get_object_or_404
from main.models import Member, Department

from main.feedback import FeedbackForm

from django.http import HttpResponseRedirect
from django.urls import reverse

from . import forms

def home(request):
    return render(request, 'home.html', {})


def members(request):
    members = Member.objects.all()
    return render(request, 'member.html', {'members': members})

def member_detail(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    form = FeedbackForm(request.POST or None, initial ={
        'member':member
    })

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('{}?sent=True'.format(reverse('member-detail', kwargs={'member_id': member.id})))

    return render(request, 'member_detail.html', {
        'member': member,
        'form': form,
        'sent': request.GET.get('sent', False)
    })


def departments(request):
    departments = Department.objects.all()
    return render(request, 'departments.html', {'departments': departments})

def department_detail(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    return render(request, 'department_detail.html', {'departments': departments})


def form(request):
    form = forms.NameForm()

    if request.method == 'POST':
        form = forms.NameForm(request.POST)
        if form.is_valid():
            print('Validation success')
            print('Name: ' + form.cleaned_data['name'])
            print('Email: ' + form.cleaned_data['email'])
            print('Text: ' + form.cleaned_data['text'])

    return render(request, 'form.html', {'form': form})
