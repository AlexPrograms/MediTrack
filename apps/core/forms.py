from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
User = get_user_model()
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}))
    first_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Repeat password'})
        self.fields['username'].label = ''
        self.fields['password1'].label = ''

        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

        # self.fields['password1'].help_text \
        #     = '<ul class="form-text text-muted small"><li>Minimum 8 characters.</li></ul>'

        self.fields['password2'].label = ''
        # self.fields[
        #     'password2'].help_text \
        #     = '<span class="form-text text-muted"><small>Repeat the password for confirmation.</small></span>'
