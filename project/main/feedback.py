from django import forms
from main.models import Feedback, Member


class FeedbackForm(forms.ModelForm):
    member = forms.ModelChoiceField(queryset=Member.objects.all(),
    widget=forms.HiddenInput)
    class Meta:
        model = Feedback
        fields = ('member', 'name', 'description')
