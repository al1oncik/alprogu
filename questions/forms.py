from django import forms


class QuestionCreateForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'title'}))
    text = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'text'}))
