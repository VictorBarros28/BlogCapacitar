from post.models import Post
from django import forms

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo','autor','content', 'img']

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo','autor','content', 'img']

