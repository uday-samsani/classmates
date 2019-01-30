from django import forms
from django.contrib.auth import get_user_model

from .models import Post


class PostCreationForm(forms.ModelForm):
    post_body = forms.CharField(label='Body', widget=forms.Textarea(
        attrs={'placeholder': 'body'}))
    post_desc = forms.CharField(label='Description',
                                widget=forms.TextInput(attrs={'placeholder': 'description'}))

    class Meta:
        model = Post
        fields = ('post_desc', 'post_body')

    def save(self, commit=True):
        post = super(PostCreationForm, self).save(commit=False)
        post.posted_by = self.cleaned_data['posted_by']
        post.post_body = self.cleaned_data['post_body']
        post.post_desc = self.cleaned_data['post_desc']
        if commit:
            post.save()
        return post


class PostChangeForm(forms.ModelForm):
    post_body = forms.CharField(label='Body', widget=forms.Textarea(
        attrs={'placeholder': 'body'}))
    post_desc = forms.CharField(label='Description',
                                widget=forms.TextInput(attrs={'placeholder': 'description'}))
    readonly_fields = ('user', 'title')

    class Meta:
        model = Post
        fields = ('post_body', 'post_desc', 'posted_by')

    def save(self, commit=True):
        post = Post.objects.get(user=self.cleaned_data['user'])
        post.post_body = self.cleaned_data['post_body']
        post.post_desc = self.cleaned_data['post_desc']
        if commit:
            post.save()
        return post
