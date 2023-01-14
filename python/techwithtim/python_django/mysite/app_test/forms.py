from django import forms

class CreateNewBlog(forms.Form):
    title = forms.CharField(label='Title', max_length=250)
    check = forms.BooleanField(required=False)
    