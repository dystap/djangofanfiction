from django import forms

from index.models import Profile

class ProfileForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=True, 
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Masukkan namamu di sini..."
        })
    )
    email = forms.EmailField(
        required=True, 
        widget=forms.TextInput(attrs={
            "type": "email",
            "class": "form-control",
            "placeholder": "Masukkan emailmu di sini..."
        })
    )
    date_of_birth = forms.DateField(
        required=True, 
        widget=forms.DateInput(attrs={
            "type": "date",
            "class": "form-control",
        })
    )
    hobby = forms.CharField(
        max_length=255,
        required=True, 
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Masukkan hobbymu di sini..."
        })
    )
    quote = forms.CharField(
        required=False, 
        widget=forms.Textarea(attrs={
            "rows": 5,
            "class": "form-control",
            "placeholder": "Masukkan quote favoritmu di sini..."
        })
    )

    def clean(self):
        cleaned_data = super().clean()

        # Custom Code

        return cleaned_data


    def save(self):

        cleaned_data = self.cleaned_data

        Profile.objects.create( 
            name=cleaned_data.get("name"),
            email=cleaned_data.get("email"),
            date_of_birth=cleaned_data.get("date_of_birth"),
            hobby=cleaned_data.get("hobby"),
            quote=cleaned_data.get("quote"),
        )
