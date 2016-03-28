from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from forms import CallbackForm, QuestionForm, OrderForm
from models import Callback, Question, Order

# Create your views here.
from telegraph_factory import settings


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
            try:
                send_mail(
                    "New request",
                    'Phone: ' + phone + '\n \nEmail: ' + email,
                    getattr(settings, "EMAIL_HOST_USER", None),
                    [settings.EMAIL_ADDRESS, ],
                    fail_silently=False,
                )
            except:
                pass
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
            if 'name' in form.cleaned_data:
                name = form.cleaned_data['name']
            else:
                name = None
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
                name=name,
                email=email,
                phone=phone,
                datetime=timezone.now(),
            )
            try:
                send_mail(
                    "New order",
                    'Phone: ' + phone + '\n \nEmail: ' + email,
                    getattr(settings, "EMAIL_HOST_USER", None),
                    [settings.EMAIL_ADDRESS, ],
                    fail_silently=False,
                )
            except:
                pass
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
            if 'name' in form.cleaned_data:
                name = form.cleaned_data['name']
            else:
                name = None
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
                question = None
            Question.objects.create(
                name=name,
                email=email,
                phone=phone,
                datetime=timezone.now(),
                question=question,
            )
            try:
                send_mail(
                    "New question",
                    'Phone: ' + phone + '\n \nEmail: ' + email,
                    getattr(settings, "EMAIL_HOST_USER", None),
                    [settings.EMAIL_ADDRESS, ],
                    fail_silently=False,
                )
            except:
                pass
            return JsonResponse({"result": "ok"})
        else:
            return JsonResponse({"result": "error"})