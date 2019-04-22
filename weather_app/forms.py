# @Date:   2019-04-21T14:51:20+06:00
# @Last modified time: 2019-04-21T15:38:58+06:00
from django import forms
from .models import City

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name']

        widgets={
                'name': forms.TextInput(attrs={
                                'class': 'input',
                                'placeholder': 'City name'
                            }
                        )
                    }
