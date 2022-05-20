from django import forms
from django.forms import DateInput, ModelForm
from .models import Donation

class DateInput(forms.DateInput):
    input_type = 'date'

class DonationForm(ModelForm):
    class Meta:
        model = Donation
        # fields = "__all__"
        fields = ('created_by','name','address','phone',
        'mode_donation','amount','cheque_no','cheque_micr','cheque_date','cheque_amount',
        'draft_no','draft_micr','draft_date','draft_amount')

        widgets = {
            'cheque_date':DateInput(),
            'draft_date' :DateInput(),
            'created_by':forms.TextInput(attrs={'value':'', 'id':'elder'}),
        }