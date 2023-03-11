from django import forms
from django.contrib.auth import get_user_model


user = get_user_model()


class PostForm(forms.ModelForm):

    class Meta:
        model = user
        fields = ('first_name', 'last_name','email')