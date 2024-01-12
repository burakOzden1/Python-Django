from django import forms


# kendi validatorlemizi yaptik.
def min_length_3(value):
    if len(value) < 3:
        raise forms.ValidationError("Kendi Denetimimiz, En az 3 karakter olmalı.")
