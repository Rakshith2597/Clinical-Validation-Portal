from django import forms
from .models import Testresult,UserRequest

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

class UserRegistration(forms.ModelForm):
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)
	designation = forms.CharField(required=True)
	email_id = forms.CharField(required=True)
	registration_number = forms.CharField(required=True)

	class Meta:
		model = UserRequest
		fields = ('first_name','last_name','designation','email_id','registration_number',)


    
        
                
        


