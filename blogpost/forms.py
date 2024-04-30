from django import forms
from .models import *
from datetime import timezone
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

    def clean_published_date(self):
        published_date = self.cleaned_data.get('published_date')
        if published_date and published_date > timezone.now():
            raise forms.ValidationError("Published date cannot be in the future.")
        return published_date
    
    
    