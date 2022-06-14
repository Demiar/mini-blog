from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Comment

class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']


class CommentForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Comment
        fields = ['text']
