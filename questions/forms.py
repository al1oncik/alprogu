from django import forms
from .models import Topic


choices = (
                ("python","python"),
                ("django","django"),
                ("web","WEB"),
                ("c#","C#"),
                ("javascript", "JavaScript"),
                ("php", "PHP"),
                ("linux", "Linux"),
                ("windows", "Windows"),
                ("c++", "C++"),
                ("c", "C"),
                ("school", "School"),
                ("math", "Math"),
            )

class QuestionCreateForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-title-input', 'placeholder': 'title'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-text-input', 'placeholder': 'text'}))
    categories = forms.MultipleChoiceField(choices=choices, widget=forms.CheckboxSelectMultiple(attrs={'class' : 'category-checkbox'}))


class QuestionChangeForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-title-input', 'placeholder': 'title'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-text-input', 'placeholder': 'text'}))
    categories = forms.MultipleChoiceField(choices=choices ,widget=forms.CheckboxSelectMultiple(attrs={'class': 'category-checkbox'}))

    class Meta:
        model = Topic
        fields = ['title', 'text', 'categories']

class AnswerCreateForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control comment-input', 'placeholder': 'Your answer'}))