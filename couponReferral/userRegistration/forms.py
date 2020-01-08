from django import forms
from userRegistration.models import UserRegistration


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	referral_code=forms.CharField(help_text="*type 'no' if you dont have a coupon code")
	class Meta():
         model = UserRegistration

         fields = ('username','password','email','age','city','referral_code')