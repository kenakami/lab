from django import forms
from django.core.exceptions import ValidationError

class CreateThreadForm(forms.Form):
    name = forms.CharField(required=False)
    subject = forms.CharField(required=False)
    comment = forms.CharField(widget=forms.Textarea, required=True)

    # TODO include image and location
    image = forms.ImageField(required=True)

    def clean_image(self):
        image = self.cleaned_data['image']
        limit_mb = 4
        if image and image.size > limit_mb * 1024 * 1024:
            raise ValidationError(f"Max size of an image is {limit_mb} MB")
        return image

    '''
    def clean(self):
        name = self.cleaned_data['name']
        subject = self.cleaned_data['subject']
        comment = self.cleaned_data['comment']
        image = self.cleaned_data['image']

        return self.cleaned_data
    '''

class ReplyForm(forms.Form):
    name = forms.CharField(required=False)
    comment = forms.CharField(widget=forms.Textarea, required=True)
    image = forms.ImageField(required=False)

    def clean_image(self):
        image = self.cleaned_data['image']
        limit_mb = 4
        if image and image.size > limit_mb * 1024 * 1024:
            raise ValidationError(f"Max size of an image is {limit_mb} MB")
        return image

    '''
    def clean(self):
        name = self.cleaned_data['name']
        comment = self.cleaned_data['comment']
        image = self.cleaned_data['image']

        return self.cleaned_data
    '''

