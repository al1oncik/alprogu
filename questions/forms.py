from django import forms


class QuestionCreateForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-title-input', 'placeholder': 'title'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-text-input', 'placeholder': 'text'}))
