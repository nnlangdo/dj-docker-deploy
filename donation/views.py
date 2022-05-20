from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Donation
from .forms import DonationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView
from num2words import num2words
# Create your views here.

def home(request):
    return render(request, 'donation/home.html')

# @login_required
def viewpage(request):
    donations_cash = Donation.objects.filter(mode_donation = 'Cash')
    donations_cheque = Donation.objects.filter(mode_donation = 'Cheque')
    donations_draft = Donation.objects.filter(mode_donation = 'Draft')

    context = {
        'donations_cash':donations_cash,
        'donations_cheque':donations_cheque,
        'donations_draft':donations_draft
    }
    return render(request, 'donation/semiadmin.html',context)


# @login_required
# def saveform(request):
#     form = DonationForm()
#     return render(request, 'donation/savedatamanual.html',{'form':form})

class AddDonationView(CreateView):
    model: Donation
    form_class = DonationForm
    template_name = 'donation/savedatamanual.html'

def receipt_bg(request):
    donor = Donation.objects.all().last()
    context = {
        'donor': donor
    }
    return render(request, 'donation/receipt-bgimg.html',context)

def receipt_main(request):
    donor = Donation.objects.last()
    if donor.mode_donation == 'Cash':
        donor_amount = donor.amount
    elif donor.mode_donation == 'Cheque':
        donor_amount = donor.cheque_amount
    else:
        donor_amount = donor.draft_amount
    donor_amount_words = num2words(donor_amount).title()

    context = {
        'donor': donor,
        'donor_amount_words':donor_amount_words
    }
    return render(request, 'donation/receipt-main.html',context)

def receipt_download(request,id):
    donor = Donation.objects.get(pk=id)
    if donor.mode_donation == 'Cash':
        donor_amount = donor.amount
    elif donor.mode_donation == 'Cheque':
        donor_amount = donor.cheque_amount
    else:
        donor_amount = donor.draft_amount
    donor_amount_words = num2words(donor_amount).title()
    context = {
        'donor':donor,
        'donor_amount_words':donor_amount_words
        }
    return render(request, 'donation/receipt-download.html',context)

class EditReceiptView(UpdateView):
    model = Donation
    template_name = 'donation/edit_receipt.html'
    fields = ['name','address','phone','mode_donation','amount','cheque_no','cheque_micr','cheque_date','cheque_amount',
    'draft_micr','draft_date','draft_amount',]
    success_url = reverse_lazy('viewpage')