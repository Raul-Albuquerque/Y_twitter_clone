from django import forms
from .models import Profile, Tweet


# SIGNUP FORM


class SignUpForm(forms.Form):
    usuario = forms.CharField(
        max_length=18,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "Username",
                "required": True,
                "max-length": 18,
            }
        ),
    )
    nome = forms.CharField(
        max_length=12,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "Name",
                "required": True,
                "max-length": 12,
            }
        ),
    )
    sobrenome = forms.CharField(
        max_length=14,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "Last Name",
                "required": True,
                "max-length": 14,
            }
        ),
    )
    email = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-input", "placeholder": "Email", "required": True}
        ),
    )
    senha = forms.CharField(
        max_length=190,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "Password",
                "required": True,
                "type": "password",
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields["usuario"].label = False
        self.fields["nome"].label = False
        self.fields["sobrenome"].label = False
        self.fields["email"].label = False
        self.fields["senha"].label = False


# SIGNIN FORM


class SignInForm(forms.Form):
    usuario = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-input", "placeholder": "Username", "required": True}
        ),
    )
    senha = forms.CharField(
        max_length=190,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "Password",
                "required": True,
                "type": "password",
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
        self.fields["usuario"].label = False
        self.fields["senha"].label = False


# POST TWEET FORM


class TweetForm(forms.ModelForm):
    content = forms.CharField(
        max_length=260,
        required=False,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "What is happening?!",
                "class": "new-tweet-textarea",
                "required": True,
                "max-length": 260,
            }
        ),
    )
    tweet_image = forms.ImageField(
        required=False,
        widget=forms.widgets.FileInput(attrs={"class": "new-tweet-image"}),
    )

    class Meta:
        model = Tweet
        exclude = {"user", "likes"}

    def __init__(self, *args, **kwargs):
        super(TweetForm, self).__init__(*args, **kwargs)
        self.fields["content"].label = False
        self.fields["tweet_image"].label = False


# EDIT PROFILE FORM


class EditProfileForm(forms.ModelForm):
    bio = forms.CharField(
        max_length=220,
        required=False,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Bio",
                "class": "edit-profile-textarea",
                "max-length": 220,
                "required": True,
            }
        ),
    )
    profile_image = forms.ImageField(required=False, label="Add Profile Picture")

    class Meta:
        model = Profile
        exclude = {"user", "follows", "creation_date"}

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.fields["bio"].label = False
