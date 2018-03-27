from django import forms


class Email(forms.Form):
    email = forms.EmailField( required=True)

'''class Apply_Job(forms.Form):
    firstname = forms.CharField(max_length=20)
    lastname = forms.CharField(max_length=15)
    uploadresume = forms.FileField(upload_to='documents')'''


