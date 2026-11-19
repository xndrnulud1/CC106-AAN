from django import forms
<<<<<<< HEAD

from .models import Student


=======
from .models import Student

>>>>>>> aae1622c46b2c75ac14801e20ae8ec9a373c9856
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'student_id',
            'first_name',
            'last_name',
            'gender',
            'date_of_birth',
            'contact_number',
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
<<<<<<< HEAD
        }
=======
        }
>>>>>>> aae1622c46b2c75ac14801e20ae8ec9a373c9856
