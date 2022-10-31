from django import forms

from Forms_Demos.web.models import Person


class NameForm(forms.Form):
    OCCUPANCIES = (
        (1, 'Child'),
        (2, 'High school student'),
        (3, 'Student'),
        (4, 'Adult'),
    )

    your_name = forms.CharField(
        max_length=30,
        label='Add first name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter name',
                'class': 'form-control',
            },
        )
    )
    age = forms.IntegerField(
        required=False,
        initial=0,
        help_text='Enter your name',
    )
    email = forms.CharField(
        widget=forms.EmailInput(),
    )

    url = forms.CharField(
        widget=forms.URLInput(),
    )
    secret = forms.CharField(
        widget=forms.PasswordInput(),
    )
    story = forms.CharField(
        widget=forms.Textarea(),
    )
    occupancy = forms.ChoiceField(
        choices=OCCUPANCIES,
    )
    occupancy_radio = forms.ChoiceField(
        choices=OCCUPANCIES,
        widget=forms.RadioSelect,
    )
    available = forms.ChoiceField(
        widget=forms.CheckboxInput,
    )


class PersonForm(forms.ModelForm):
    story = forms.CharField(
        widget=forms.Textarea,
    )

    class Meta:
        model = Person
        fields = '__all__'
        # or
        #fields = ('name','age')
        # or
        # exclude = ('pets',)
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            )
        }

        help_texts = {
            'name': 'Your name',
        }

        labels = {
            'age': 'The AGE',
        }
