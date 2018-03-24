from django import forms

class TextForm(forms.Form):
	name = forms.CharField(label='text',max_length = 100,widget=forms.TextInput(attrs={'id':'namanyay-search-box','name':'q'}))