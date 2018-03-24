from django import forms

class TextForm(forms.Form):
	name = forms.CharField(label='',max_length = 100,widget=forms.TextInput(attrs={'id':'namanyay-search-box','name':'q','placeholder':'Search here...'}))