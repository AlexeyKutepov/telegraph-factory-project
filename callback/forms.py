__author__ = 'Alexey Kutepov'

from django import forms


class CallbackForm(forms.Form):
    # name = forms.TextInput()
    email = forms.EmailField()
    phone = forms.TextInput()


class QuestionForm(forms.Form):
    # name = forms.TextInput()
    email = forms.EmailField()
    phone = forms.TextInput()
    question = forms.Textarea()


class OrderForm(forms.Form):
    name = forms.TextInput()
    email = forms.EmailField()
    phone = forms.TextInput()
    description = forms.Textarea()
