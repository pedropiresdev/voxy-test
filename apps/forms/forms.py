import datetime

from django import forms
from django.core.exceptions import ValidationError


class TextBox(forms.Form):
    text_box = forms.Field()

    # TODO - Implement field validation using validators
    def is_valid(self):
        if not self.data:
            return False

        return True
