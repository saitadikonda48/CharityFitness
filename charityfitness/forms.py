from django import forms

class WeightForm(forms.Form):
    your_weight = forms.FloatField(label='', 
    	widget=forms.TextInput(attrs={'placeholder': 'Enter Today\'s Weight'}))

class CalorieForm(forms.Form):
	caloric_intake = forms.IntegerField(label='',
		widget=forms.TextInput(attrs={'placeholder': 'Enter Caloric Intake'}))