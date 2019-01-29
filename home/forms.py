from django import forms
from django.contrib.auth import get_user_model

from .models import Post


class PostCreationForm(forms.ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(
        attrs={'placeholder': 'title'}))
    body = forms.CharField(label='Body', widget=forms.Textarea(
        attrs={'placeholder': 'body'}))
    description = forms.CharField(label='Description',
                                  widget=forms.TextInput(attrs={'placeholder': 'description'}))

    class Meta:
        model = Post
        fields = ('title', 'body', 'description')

    def save(self, commit=True):
        post = super(PostCreationForm, self).save(commit=False)
        post.user = self.cleaned_data['user']
        post.title = self.cleaned_data['title']
        post.body = self.cleaned_data['body']
        post.description = self.cleaned_data['description']
        if commit:
            post.save()
        return post


class PostChangeForm(forms.ModelForm):
    body = forms.CharField(label='Body', widget=forms.Textarea(
        attrs={'placeholder': 'body'}))
    description = forms.CharField(label='Description',
                                  widget=forms.TextInput(attrs={'placeholder': 'description'}))
    readonly_fields = ('user', 'title')

    class Meta:
        model = Post
        fields = ('body', 'description', 'title', 'user')

    def save(self, commit=True):
        post = Post.objects.get(user=self.cleaned_data['user'])
        post.body = self.cleaned_data['body']
        post.description = self.cleaned_data['description']
        if commit:
            post.save()
        return post
