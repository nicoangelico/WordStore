from django import forms

class NameForm(forms.Form):
    word_info = forms.CharField(max_length=100, label='' , widget=forms.TextInput(attrs={'class' : 'form-control mr-sm-2'}))