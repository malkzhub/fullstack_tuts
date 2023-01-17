from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField(required=False)



    # Types of default forms in Django
    # {{ form.as_table }}
    # {{ form.as_p }}
    # {{ form.as_ul }}