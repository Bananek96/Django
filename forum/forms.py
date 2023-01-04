from django import forms
from .models import Post, Answer


class PostForm(forms.ModelForm):
    title = forms.CharField(
        label="Tytuł",
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    description = forms.CharField(
        label="Treść",
        max_length=500,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Post
        fields = ('title', 'description',)


class AnswerForm(forms.ModelForm):
    text = forms.CharField(
        label="Komentarz",
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Answer
        fields = ('text',)
