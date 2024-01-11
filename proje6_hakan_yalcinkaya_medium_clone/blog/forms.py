from django import forms
from .models import BlogPost
from tinymce.widgets import TinyMCE


class BlogPostModelForm(forms.ModelForm):
    tag = forms.CharField(required=False)
    content = forms.CharField(widget=TinyMCE(attrs={"cols": 40, "rows": 20}))

    class Meta:
        model = BlogPost
        fields = [
            "title",
            "cover_image",
            "content",
            "category",
            "tag",
        ]
