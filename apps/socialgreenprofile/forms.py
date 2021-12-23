from django import forms

from .models import SocialgreenProfile


class SocialgreenProfileForm(forms.ModelForm):
    class Meta:
        model = SocialgreenProfile
        fields = ('avatar',)
