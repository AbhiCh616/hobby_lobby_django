from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from accounts.models import User

class UserCreationForm(forms.ModelForm):
    # Include all fields with a repeated password one
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'is_admin',)
    
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    # Replace password field with admin's disabled
    # password hash display field
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value
        # Done here because 'fields' doesn't have access to the initial value
        return self.initial["password"]