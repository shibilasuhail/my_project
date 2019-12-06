from django import forms
from .models import enquery


class enqueryForm(forms.ModelForm):
    class Meta:
        model = enquery
        fields = ('name',
                  'email',
                  'subject',
                  'message',
                  )
