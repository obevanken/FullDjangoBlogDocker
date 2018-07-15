from django import forms
from django.utils.translation import gettext_lazy as _
from .models import User, Post, Comment
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class RegistationForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirmation = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data["password"]
        password_confirmation = cleaned_data['password_confirmation']
        email = cleaned_data['email']
        username = cleaned_data['username']

        if len(password) < 8:
            self.add_error('password', _("Пароль маленький"))

        if password != password_confirmation:
            self.add_error('password_confirmation', _("Пароли не совпадают"))

        if User.objects.filter(username=username).count():
            self.add_error('username', _("пользователь уже существует :*"))


class PostForm(forms.Form):
        title = forms.CharField(min_length=6, max_length=64)
        text = forms.CharField(widget=CKEditorUploadingWidget())
        image = forms.ImageField(required=False)


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'image']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'avatar']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class CreateComment(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='Написать комментарий')


class EditFormComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
