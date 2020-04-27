from django import forms
from .models import FeaturedApp


class FeaturedAppForm(forms.ModelForm):
    title = forms.CharField(label='',
                            widget=forms.TextInput(attrs={
                                'placeholder': 'Enter Title'
                            })
                            )
    email   = forms.EmailField()
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(attrs={
                                      'class': 'New-Text Class',
                                      'row': 20,
                                      'cols': 20,
                                      'id': 'my-id'
                                  })
                                  )
    price = forms.FloatField(initial=199.1)

    class Meta:
        model = FeaturedApp
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if not 'cfe' in title:
            raise forms.ValidationError('Invalid Title')
        if not 'news' in title:
            raise forms.ValidationError('Invalid Title')

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if not email.endswith('edu'):
            raise forms.ValidationError('Invalid email')


class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Enter Title'}))
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(attrs={
                                      'class': 'New-Text Class',
                                      'row': 20,
                                      'cols': 20,
                                      'id': 'my-id'
                                  })
                                  )
    price = forms.FloatField(initial=199.1)
