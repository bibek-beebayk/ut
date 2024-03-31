from django import forms

from product.models import Requirement


class RequirementForm(forms.ModelForm):
    class Meta:
        model = Requirement
        fields = ["product", "email"]
        