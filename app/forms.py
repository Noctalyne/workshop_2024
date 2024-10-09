from django import forms
from .models import User, UserTutor, Pathology, UserPathology, HealthMeasurements

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'birthday', 'sexe', 'phone', 'social_security_number']
        widgets = {
            'password': forms.PasswordInput(),
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }

class UserTutorForm(forms.ModelForm):
    class Meta:
        model = UserTutor
        fields = ['user_id', 'tutor_id', 'relationship', 'end_at']
        widgets = {
            'end_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class PathologyForm(forms.ModelForm):
    class Meta:
        model = Pathology
        fields = ['name', 'description', 'category', 'end_at']
        widgets = {
            'end_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class UserPathologyForm(forms.ModelForm):
    class Meta:
        model = UserPathology
        fields = ['user_id', 'pathology_id', 'diagnosis_date', 'severity', 'status']
        widgets = {
            'diagnosis_date': forms.DateInput(attrs={'type': 'date'}),
        }

class HealthMeasurementsForm(forms.ModelForm):
    class Meta:
        model = HealthMeasurements
        fields = ['user_id', 'pathology_id', 'measurement_type', 'measurement_date', 'value', 'unit']
        widgets = {
            'measurement_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
