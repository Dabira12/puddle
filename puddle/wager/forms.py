from django import forms

from .models import Wager
import requests


INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    def get_event():
       response = requests.get("https://api.the-odds-api.com/v4/sports/soccer_epl/odds?regions=us&oddsFormat=decimal&apiKey=065f129f65ef12e03137bc35b65e27be")

       print(response)
    class Meta:
        model = Wager
        fields = ('sport', 'event', 'name', 'stake', 'odds', 'image' )

        labels = {
            'stake': 'Minimum stake',
            'sport': 'Sport League'
        }
        # YOUR_CHOICES = (
        #         ('', 'Select your zone'),
        #         ('1', 'First'), #First one is the value of the select option and the second is the displayed value in the option
        #         ('2', 'second'),
        #         )
        def get_event():
            response = requests.get("https://api.the-odds-api.com/v4/sports/soccer_epl/odds?regions=us&oddsFormat=decimal&apiKey=065f129f65ef12e03137bc35b65e27be")

            body = (response.json())
            YOUR_CHOICES = [('','Choose an upcoming match')]

            for event in body:
                ans = (event['id'], event['home_team'] + ' vs ' + event['away_team'])
                YOUR_CHOICES.append(ans)
            print(YOUR_CHOICES)
            return (YOUR_CHOICES)
            


        YOUR_CHOICES = get_event()
        widgets = {
            'sport': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'event': forms.Select(attrs={
                'class': INPUT_CLASSES
            }, choices= YOUR_CHOICES),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'odds': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'stake': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Wager
        fields = ('sport', 'event', 'name', 'stake', 'odds', 'image' )

        labels = {
            'stake': 'Minimum stake',
            'sport': 'Sport League'
        }

        def get_event():
            response = requests.get("https://api.the-odds-api.com/v4/sports/soccer_epl/odds?regions=us&oddsFormat=decimal&apiKey=065f129f65ef12e03137bc35b65e27be")

            body = (response.json())
            YOUR_CHOICES = [('','Choose an upcoming match')]

            for event in body:
                ans = (event['id'], event['home_team'] + ' vs ' + event['away_team'])
                YOUR_CHOICES.append(ans)
                print(YOUR_CHOICES)
            return (YOUR_CHOICES)
        


        YOUR_CHOICES = get_event()
        widgets = {
        'sport': forms.Select(attrs={
            'class': INPUT_CLASSES
        }),
        'event': forms.Select(attrs={
            'class': INPUT_CLASSES
        }, choices= YOUR_CHOICES),
        'name': forms.TextInput(attrs={
            'class': INPUT_CLASSES
        }),
        'odds': forms.NumberInput(attrs={
            'class': INPUT_CLASSES
        }),
        'stake': forms.NumberInput(attrs={
            'class': INPUT_CLASSES
        }),
        'image': forms.FileInput(attrs={
            'class': INPUT_CLASSES
        })
    }
