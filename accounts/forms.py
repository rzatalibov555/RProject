from django import forms
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

class LoginForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput) #Change password input type to password

    class Meta:
        model = User
        fields = ("username", "password")

    # ====================== FORM VALIDATIONS Start ======================
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        user = authenticate(username=username, password=password)
        print(user)

        if not user:
            raise forms.ValidationError("Username or password is wrong!")

        if not user.is_active:
            raise forms.ValidationError("Your account is not active!")

        return self.cleaned_data

    # ====================== FORM VALIDATIONS End   ======================


    # ====================== for add form-control class to all inputs Start ======================

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})
            self.fields[field].required = True

    # ====================== for add form-control class to all inputs End ======================






