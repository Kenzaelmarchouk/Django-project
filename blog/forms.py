from django import forms
from .import models
#class CreateArticle(forms.Form):
	#nom=forms.CharField(max_length=50)
	#CNE=forms.CharField(max_length=10)
	#CNI=forms.CharField(max_length=8)
	#tel=forms.CharField(max_length=10)
	#email=forms.EmailField(label="ton email")
	#demande=forms.CharField(widget=forms.Textarea)
	#renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)


#class CreateArticle1(forms.Form):
	#choix_liste=(
		#("1","pavio1"),
		#("2","pavio2"),
		#("3","pavio3")
		#)
	#nom=forms.CharField(max_length=50)
	#chambre=forms.IntegerField()
	#demande=forms.CharField(widget=forms.Textarea)
	#pavion=forms.ChoiceField( choices=choix_liste)

class CreateAdmin(forms.ModelForm):
	class Meta:
		model=models.Formule
		fields=['name','CNE','CNI','telephone','email','demande']
		widget={
		      'name':forms.TextInput(attrs={'class':'form-control'}),
		       'CNE':forms.TextInput(attrs={'class':'form-control'}),
		       'CNI':forms.NumberInput(attrs={'class':'form-control'}),
                'telephone':forms.NumberInput(attrs={'class':'form-control'}),
                'email':forms.EmailInput(attrs={'class':'form-control'}),
                'demande':forms.Textarea(attrs={'class':'form-control'})
		}
 

class CreateInter(forms.ModelForm):
	class Meta:
		model=models.Formule1
		fields=['nom','chambre','demande','pavion']


class CreateUs(forms.ModelForm):
	class Meta:
		model=models.Formule2
		fields=['email']





			

	
	
		