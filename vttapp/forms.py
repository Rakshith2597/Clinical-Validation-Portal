from django import forms
from .models import Testresult   
# class TuringTest(forms.Form):
# 	selection = forms.ChoiceField(required=True)
# 	confidence = forms.IntegerField(required=True)

# 	# def clean_selection_data(self):
# 	# 	data = self.cleaned_data['selection']
# 	# 	return data
CHOICES =( 
    ("Image1", "Image1"), 
    ("Image2", "Image2"), 

) 
class TuringTest(forms.ModelForm):
	selcted_image = forms.ChoiceField(required=True,widget=forms.RadioSelect(attrs={'class': 'primary'}),choices=CHOICES)
	confidence = forms.IntegerField(required=True)

	class Meta:
		model = Testresult
		fields = ('selcted_image', 'confidence',)

    
        
                
        


