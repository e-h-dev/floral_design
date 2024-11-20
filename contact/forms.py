from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone', 'message', 'added_info')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'message': 'Your Message',
            'added_info': 'Any other Request',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'added_info':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = 'side-print'
            self.fields[field].label = False