
from django import forms
from .models import Post, PostTemplate

class PostForm(forms.ModelForm):
    template = forms.ModelChoiceField(
        queryset=PostTemplate.objects.all(),
        required=False,
        empty_label="Select a template"
    )
    scheduled_time = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        help_text="Select a scheduled posting time. Leave empty for immediate posting."
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'platform', 'scheduled_time']

class PostTemplateForm(forms.ModelForm):
    class Meta: 
        model = PostTemplate
        fields = ['title', 'content', 'platform']

