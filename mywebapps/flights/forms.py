from django import forms 

class AgentProfile(forms.Form):
    First_name = forms.CharField(max_length= 50, required=False)
    Last_name = forms.CharField(max_length=50)
    email = forms.EmailField(label="Enter Your Email")
    acode = forms.IntegerField(help_text= "Must Be Filled")
    mobile = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput())
    textarea = forms.CharField(widget=forms.Textarea())
    checkbox = forms.CharField(widget=forms.CheckboxInput())
    
