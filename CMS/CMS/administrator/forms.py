from django import forms
from teacher.models import Teacher
from django.contrib.auth import get_user_model

class UserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        placeholders=['First Name', 'Last Name', 'Username','Email']
        
        for ind,(name,field) in enumerate(self.fields.items()):
            field.widget.attrs.update({'placeholder': f'{placeholders[ind]}'})
        
class TeacherForm(forms.ModelForm):
    
    dateOfBirth =forms.DateField(widget = forms.SelectDateWidget) 
   
    class Meta:
        model = Teacher
        fields ='__all__'

        exclude = ('user',)
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = ['Profile Picture','Home Address', 'Telephone', 'Gender', 'Date of Birth', 'Designation']    
        for ind,(name,field) in enumerate(self.fields.items()):
            field.widget.attrs.update({'placeholder': f'{placeholders[ind]}'})