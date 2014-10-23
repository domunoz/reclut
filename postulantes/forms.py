#coding:utf-8
from django import forms 

class UploadFileForm(forms.Form):
    ttitle = forms.CharField(max_length=140)
    f = forms.FileField()
