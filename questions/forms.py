from django import forms


class QuestionCreateForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-title-input', 'placeholder': 'title'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-text-input', 'placeholder': 'text'}))
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
    categories = forms.MultipleChoiceField(choices=choices, widget=forms.CheckboxSelectMultiple(attrs={'class' : 'category-checkbox'}))

class AnswerCreateForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control comment-input', 'placeholder': 'Your answer'}))