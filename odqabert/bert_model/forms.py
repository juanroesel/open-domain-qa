from django import forms
from .models import QAInput

class InputForm(forms.ModelForm):
    class Meta:
              model = QAInput
              fields = "__all__"
    
    question = forms.CharField(max_length=512)
    context = forms.CharField(widget=forms.Textarea)
