from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from forms import CallbackForm, QuestionForm, OrderForm
from models import Callback, Question, Order

# Create your views here.


def callback(request):
    """
    Handle callback
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = CallbackForm(request.POST)
        if form.is_valid():
            Callback.objects.create(
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                datetime=timezone.now()
            )
            return JsonResponse({"result": "ok"})
        else:
            return JsonResponse({"result": "error"})


def order(request):
    """
    Handle order
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            Order.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                datetime=timezone.now(),
                description=form.cleaned_data['description'],
            )
            return JsonResponse({"result": "ok"})
        else:
            return JsonResponse({"result": "error"})


def question(request):
    """
    Handle question
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            Question.objects.create(
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                datetime=timezone.now(),
                question=form.cleaned_data['question'],
            )
            return JsonResponse({"result": "ok"})
        else:
            return JsonResponse({"result": "error"})