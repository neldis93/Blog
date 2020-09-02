from django import forms

from .models import Suscribers, Contact

class SuscriberForm(forms.ModelForm):
    class Meta:
        model= Suscribers
        fields= (
            'email',
        )
        widgets= {
            'email': forms.EmailInput(
                attrs= {
                    'placeholder':'Email',
                }
            ),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model= Contact
        fields= ('__all__')