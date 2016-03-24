__author__ = 'Alexey Kutepov'

from django import forms


class CallbackForm(forms.Form):
    # name = forms.TextInput(required=False)
    email = forms.EmailField(required=False)
    phone = forms.CharField(required=False)


class QuestionForm(forms.Form):
    # name = forms.TextInput(required=False)
    email = forms.EmailField(required=False)
    phone = forms.CharField(required=False)
    question = forms.Textarea()


class OrderForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    phone = forms.CharField(required=False)
    description = forms.Textarea()
