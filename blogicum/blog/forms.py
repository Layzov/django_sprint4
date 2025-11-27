from django import forms
from .models import Post, Comment
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', )


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author', 'is_published']
        widgets = {
            'pub_date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }

    # def clean_pub_date(self):
    #     pub_date = self.cleaned_data['pub_date']

    #     if pub_date < timezone.now():
    #         self.add_error('pub_date', 'Дата не может быть в прошлом')

    #     return pub_date


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', )
        widgets = {
            'text': forms.Textarea(attrs={'rows': 5, 'cols': 40, 'style': 'resize:none;'})
        }
