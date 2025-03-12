from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from refund_sytem.models import CustomUser, RefundRequest


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email",
        )


class RefundRequestForm(ModelForm):
    class Meta:
        model = RefundRequest
        exclude = ['user', 'status', 'iban_verified']
