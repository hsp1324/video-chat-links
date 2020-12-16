from django import forms

from .models import Link

class LinkForm(forms.ModelForm):
	title = forms.CharField(label='Title', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
	url = forms.URLField(label='Link', required=False, initial='http://')
	description = forms.CharField(
								required=False, 
								widget=forms.Textarea(
										attrs={
											"placeholder": "Your description", 
											"class": "new-class-name two", 
											"id": "my-id-for-textareas",
											"rows": 30, 
											"cols": 100
										}
									)
								)
	class Meta:
		model = Link
		fields = [
			'title', 
			'url', 
			'description'
		]
	def clean_title(self, *args, **kwargs):
		title = self.cleaned_data.get("title")
		if not "CFE" in title:
			return title
		if not "news" in title:
			raise forms.ValidationError("This is not a valid title")
		return title

	def clean_email(self, *args, **kwargs):
		email = self.cleaned_data.get("email")
		if not email.endswith("edu"):
			raise forms.ValidationError("This is not a valid email")
		return email




class RawLinkForm(forms.Form):
	title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
	url = forms.URLField(label='Your website', required=False)
	description = forms.CharField(
								required=False, 
								widget=forms.Textarea(
										attrs={
											"placeholder": "Your description", 
											"class": "new-class-name two", 
											"id": "my-id-for-textareas",
											"rows": 30, 
											"cols": 100
										}
									)
								)