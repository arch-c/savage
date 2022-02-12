from django import forms


class BackCallForm(forms.Form):
    firstname = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Имя'}), max_length=100)
    lastname = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}), max_length=100)
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'placeholder': 'E-Mail'}))
    theme = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Тема'}), max_length=300)
    text = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Текст', 'style': 'resize:none'}))
