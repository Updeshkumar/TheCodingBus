from django import forms

class URLForm(forms.Form):
    url = forms.URLField(label="Enter URL", widget=forms.URLInput(attrs={'placeholder': 'https://example.com'}))
