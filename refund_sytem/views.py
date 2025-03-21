import os

import requests
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from refund_sytem.forms import CustomUserCreationForm, RefundRequestForm
from refund_sytem.models import CustomUser, RefundRequest


def index(request: HttpRequest):
    return redirect("refund_list")

class RefundRequestListView(LoginRequiredMixin, generic.ListView):
    model = RefundRequest
    template_name = "refunds/list.html"
    context_object_name = "refunds"
    paginate_by = 10


class RefundRequestDetailView(generic.DetailView):
    model = RefundRequest
    template_name = "refunds/detail.html"
    context_object_name = "refund"


class CreateRefundRequestView(LoginRequiredMixin, generic.CreateView):
    model = RefundRequest
    form_class = RefundRequestForm
    success_url = reverse_lazy("refund_list")
    template_name = "refunds/create.html"


class SignUpView(generic.CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy('refund_list')


class ValidateIBANView(LoginRequiredMixin, generic.DetailView):
    model = RefundRequest
    template_name = "refunds/list.html"

    print(os.getenv("X_API_KEY"))

    def get(self, request, *args, **kwargs):
        iban = request.GET.get('iban')
        if iban:
            api_url = f'https://api.api-ninjas.com/v1/iban?iban={iban}'
            response = requests.get(api_url, headers={
                'X-Api-Key': "/8bPV98KuaKUms5PQyX/pg==jHxLxNIAfdwiSckF"
            })

            if response.status_code == requests.codes.ok:
                iban_data = response.json()
                if iban_data["valid"]:
                    return redirect("refund_list")
                else:
                    return JsonResponse({'error': f'Error: {response.status_code}, {response.text}'}, status=400)
            else:
                return JsonResponse({"error": f"API error: {response.status_code}, {response.text}"}, status=500)
        else:
            return JsonResponse({'error': 'IBAN is required'}, status=400)
