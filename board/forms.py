from django import forms

class CreateThreadForm(forms.Form):
    name = forms.CharField(required=False)
    subject = forms.CharField(required=False)
    comment = forms.CharField(widget=forms.Textarea, required=True)
    # TODO include image and location

    def clean(self):
        name = self.cleaned_data['name']
        subject = self.cleaned_data['subject']
        comment = self.cleaned_data['comment']

        return self.cleaned_data

class ReplyForm(forms.Form):
    name = forms.CharField(required=False)
    comment = forms.CharField(widget=forms.Textarea, required=True)

    def clean(self):
        name = self.cleaned_data['name']
        comment = self.cleaned_data['comment']

        return self.cleaned_data

