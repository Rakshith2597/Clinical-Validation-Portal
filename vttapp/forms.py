from django import forms
from .models import Testresult   
# class TuringTest(forms.Form):
# 	selection = forms.ChoiceField(required=True)
# 	confidence = forms.IntegerField(required=True)

# 	# def clean_selection_data(self):
# 	# 	data = self.cleaned_data['selection']
# 	# 	return data

class TuringTest(forms.ModelForm):

    class Meta:
        model = Testresult
        fields = ('selcted_image', 'confidence',)        
        


