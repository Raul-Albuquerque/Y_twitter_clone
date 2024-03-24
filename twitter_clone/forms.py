from django import forms


# SIGNUP FORM

class SignUpForm(forms.Form):
  usuario = forms.CharField(max_length=150, required=False, widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'usuario', 'required': True}))
  nome = forms.CharField(max_length=150, required=False, widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Nome', 'required': True}))
  sobrenome = forms.CharField(max_length=150, required=False, widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Sobrenome', 'required': True}))
  email = forms.CharField(max_length=150, required=False, widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Email', 'required': True}))
  senha = forms.CharField(max_length=190, required=False, widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Senha', 'required': True, 'type': 'password'}))
  
  def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['usuario'].label = False
        self.fields['nome'].label = False
        self.fields['sobrenome'].label = False
        self.fields['email'].label = False
        self.fields['senha'].label = False

# SIGNIN FORM
  
class SignInForm(forms.Form):
  usuario = forms.CharField(max_length=150, required=False, widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'usuario', 'required': True}))
  senha = forms.CharField(max_length=190, required=False, widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Senha', 'required': True, 'type': 'password'}))

  def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
        self.fields['usuario'].label = False
        self.fields['senha'].label = False
