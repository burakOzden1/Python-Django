from django import forms
from django.core import validators
from .models import BlogPost
from tinymce.widgets import TinyMCE


# # kendi validatorlemizi yaptik.
# def min_length_3(value):
#     if len(value) < 3:
#         raise forms.ValidationError("Kendi Denetimimiz, En az 3 karakter olmalı.")


class BlogPostModelForm(forms.ModelForm):
    tag = forms.CharField(required=False)
    content = forms.CharField(widget=TinyMCE(attrs={"cols": 40, "rows": 20}))
    # title = forms.CharField(validators=[validators.MinLengthValidator(3)])  # Burada varsayilan olarak djangonun hatasini dondurur.
    # title = forms.CharField(validators=[validators.MinLengthValidator(3, message="En az 3 karakter girebilirsiniz.")]) # Burada da kendi hata mesajimizi dondurduk.
    # title = forms.CharField(validators=[min_length_3]) # Burada da kendi hata mesajimizi dondurduk.

    class Meta:
        model = BlogPost
        fields = [
            "title",
            "cover_image",
            "content",
            "category",
            "tag",
        ]

    # # form icinde validator kullandik.
    # def clean_title(self):
    #     title = self.cleaned_data.get('title')
    #     if len(title) < 3:
    #         raise forms.ValidationError('Title en az 3 karakter olmali.')
    #     return title.upper()