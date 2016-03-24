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
            if 'email' in form.cleaned_data:
                email = form.cleaned_data['email']
            else:
                email = None
            if 'phone' in form.cleaned_data:
                phone = form.cleaned_data['phone']
            else:
                phone = None
            if email == "" and phone == "":
                return JsonResponse({"result": "error"})
            Callback.objects.create(
                email=email,
                phone=phone,
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
            if 'email' in form.cleaned_data:
                email = form.cleaned_data['email']
            else:
                email = None
            if 'phone' in form.cleaned_data:
                phone = form.cleaned_data['phone']
            else:
                phone = None
            if email == "" and phone == "":
                return JsonResponse({"result": "error"})
            Order.objects.create(
                name=form.cleaned_data['name'],
                email=email,
                phone=phone,
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
            if 'email' in form.cleaned_data:
                email = form.cleaned_data['email']
            else:
                email = None
            if 'phone' in form.cleaned_data:
                phone = form.cleaned_data['phone']
            else:
                phone = None
            if email == "" and phone == "":
                return JsonResponse({"result": "error"})
            if 'question' in form.cleaned_data:
                question = form.cleaned_data['question']
            else:
                phone = None
            Question.objects.create(
                email=email,
                phone=phone,
                datetime=timezone.now(),
                question=question,
            )
            return JsonResponse({"result": "ok"})
        else:
            return JsonResponse({"result": "error"})