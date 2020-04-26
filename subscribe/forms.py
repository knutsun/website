from django import forms


class Subscribe(forms.Form):
    Email = forms.EmailField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'style': 'padding: 5px;',
                'placeholder': 'Enter email'
            }
        ))


    def __str__(self):
        return self.Email
