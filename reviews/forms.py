from django import forms
from .models import ReviewsAndRatings

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewsAndRatings
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'review': 'Leave your review',
        }

        # self.fields['name'].widget.attrs['autofocus'] = True
        # for field in self.fields:
        #     if self.fields[field].required:
        #         placeholder = f'{placeholders[field]} *'
        #     else:
        #         placeholder = placeholders[field]
        #     self.fields[field].widget.attrs['placeholder'] = placeholder
        #     self.fields[field].widget.attrs['class'] = 'rounded-2 profile-form-input'
        #     self.fields[field].label = False