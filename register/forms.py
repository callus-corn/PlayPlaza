from django import forms

from account.models import User


class UserCreationForm(forms.ModelForm):
    pass1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    pass2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email','name',)

    def clean_password2(self):
        pass1 = self.cleaned_data.get("pass1")
        pass2 = self.cleaned_data.get("pass2")
        if pass1 and pass2 and pass1 != pass2:
            raise form.ValidationError("Error")
        return pass2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["pass1"])
        if commit:
            user.save()
        return user
