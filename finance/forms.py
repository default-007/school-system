from django import forms
from .models import *
from authentication.models import User
from constants import *


class FeeTypeForm(forms.ModelForm):
    name = forms.CharField(
        label="Fee charge name", widget=forms.TextInput(attrs={"class": "form-control"})
    )
    student = forms.ModelChoiceField(
        label="Student",
        queryset=Student.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    amount = forms.IntegerField(
        label="Amount", widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    session = forms.ModelChoiceField(
        label="Session",
        queryset=Session.objects.all(),
        widget=forms.RadioSelect(attrs={"class": ""}),
    )
    term = forms.ChoiceField(label="Term", choices=TERM, widget=forms.RadioSelect())

    class Meta:
        model = OtherFeeCharges
        fields = ["name", "student", "amount", "session"]


""" class PayTypeForm(forms.ModelForm):
    student = forms.ModelChoiceField(label="Student", queryset=Student.objects.all())
    for_fee = forms.ModelChoiceField(label="Fee Charge", queryset=FeeType.objects.all())
    paid_amount = forms.IntegerField(
        label="Paid Amount", widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    payment_method = forms.ChoiceField(
        label="Payment Method", choices=PAYMENT_METHOD, widget=forms.RadioSelect
    )
    receipt_number = forms.ChoiceField(
        label="Receipt Number", widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = PayType
        fields = [
            "student",
            "paid_amount",
            "for_fee",
            "payment_method",
            "receipt_number",
        ] """


class FeeForm(forms.ModelForm):
    for_class = forms.ModelChoiceField(label="Class", queryset=Class.objects.all())
    term = forms.ChoiceField(
        label="Term",
        choices=TERM,
        widget=forms.RadioSelect(attrs={}),
    )
    tuition = forms.IntegerField(
        label="Tuition Fee", widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    lunch = forms.IntegerField(
        label="Lunch", widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    activity = forms.IntegerField(
        label="Activity", widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    maintenance = forms.IntegerField(
        label="Maintanace", widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    examination = forms.IntegerField(
        label="Examination", widget=forms.NumberInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Fee
        fields = [
            "for_class",
            "term",
            "tuition",
            "lunch",
            "activity",
            "maintenance",
            "examination",
        ]


class PaymentForm(forms.ModelForm):
    student = forms.ModelChoiceField(label="Student", queryset=Student.objects.all())
    paid_amount = forms.IntegerField(
        label="Paid Amount", widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    payment_method = forms.ChoiceField(
        label="Payment Method", choices=PAYMENT_METHOD, widget=forms.RadioSelect
    )
    term = forms.ChoiceField(label="Term", choices=TERM, widget=forms.RadioSelect())
    receipt_number = forms.CharField(
        label="Receipt Number", widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Payment
        fields = [
            "student",
            "paid_amount",
            "payment_method",
            "term",
            "receipt_number",
        ]


class ProfilePaymentForm(forms.ModelForm):
    paid_amount = forms.IntegerField(
        label="Paid Amount", widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    payment_method = forms.ChoiceField(
        label="Payment Method", choices=PAYMENT_METHOD, widget=forms.RadioSelect
    )
    term = forms.ChoiceField(label="Term", choices=TERM, widget=forms.RadioSelect())
    receipt_number = forms.CharField(
        label="Receipt Number", widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Payment
        fields = [
            "paid_amount",
            "payment_method",
            "term",
            "receipt_number",
        ]


class ExpenseForm(forms.ModelForm):
    name = forms.CharField(
        label="Name", widget=forms.TextInput(attrs={"class": "form-control"})
    )
    description = forms.CharField(
        label="Description", widget=forms.TextInput(attrs={"class": "form-control"})
    )
    term = forms.ChoiceField(label="Term", choices=TERM, widget=forms.RadioSelect)
    amount = forms.IntegerField(
        label="Amount", widget=forms.NumberInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Expense
        fields = ["name", "description", "term", "amount"]
