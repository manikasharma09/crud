from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
	id_no=forms.CharField(widget=forms.TextInput(),max_length=100,required=True)
	name=forms.CharField(widget=forms.TextInput(),max_length=100,required=True)
	email=forms.CharField(widget=forms.TextInput(),max_length=100,required=True)
	college_name=forms.CharField(widget=forms.TextInput(),max_length=200,required=True)
	cgpa=forms.IntegerField(widget=forms.TextInput(),required=True)
	password=forms.CharField(widget=forms.TextInput(),max_length=100,required=True)

	class Meta:
		model=Profile
		fields=['id_no','name','email','college_name','cgpa','password']
