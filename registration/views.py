from django.contrib import messages
<<<<<<< HEAD
from django.contrib.auth.decorators import user_passes_test
=======
>>>>>>> aae1622c46b2c75ac14801e20ae8ec9a373c9856
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import StudentForm
from .models import Student

def student_registration(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        contact_number = request.POST.get('contact_no')

        # Create a new Student object and save it to the database
        Student.objects.create(
            student_id=student_id,

            first_name=first_name,
            last_name=last_name,
            gender=gender,
            date_of_birth=date_of_birth,
            contact_number=contact_number
        ) 
        return redirect('registration_success')

    return render(
        request,
        'registration/registration.html',
    )

def registration_success(request):
    return render(
        request, 
        'registration/success.html'
    )

<<<<<<< HEAD

def staff_check(user):
    return user.is_authenticated and user.is_staff


@user_passes_test(staff_check, login_url='login')
def staff_dashboard(request):
    total_students = Student.objects.count()
    male_students = Student.objects.filter(gender='Male').count()
    female_students = Student.objects.filter(gender='Female').count()

    male_percent = (
        male_students / total_students * 100
        if total_students > 0 else 0
    )
    female_percent = (
        female_students / total_students * 100
        if total_students > 0 else 0
    )

    query = request.GET.get('q', '').strip()
    students = Student.objects.all().order_by('last_name', 'first_name')
    if query:
        students = students.filter(
            Q(student_id__icontains=query)
            | Q(first_name__icontains=query)
            | Q(last_name__icontains=query)
        )

    context = {
        'total_students': total_students,
        'male_students': male_students,
        'female_students': female_students,
        'male_percent': male_percent,
        'female_percent': female_percent,
        'students': students,
        'query': query,
    }
    return render(
        request,
        'registration/dashboard.html',
        context,
    )


@user_passes_test(staff_check, login_url='login')
=======
>>>>>>> aae1622c46b2c75ac14801e20ae8ec9a373c9856
def student_list(request):
    query = request.GET.get('q', '').strip()
    students = Student.objects.all().order_by('last_name', 'first_name')
    if query:
<<<<<<< HEAD
        students = students.filter(
            Q(student_id__icontains=query)
            | Q(first_name__icontains=query)
            | Q(last_name__icontains=query)
        )
=======
       students = students.filter(
           Q(student_id__icontains=query) |
           Q(first_name__icontains=query) |
           Q(last_name__icontains=query)
      )
>>>>>>> aae1622c46b2c75ac14801e20ae8ec9a373c9856
    return render(
        request,
        'registration/student_list.html',
        {'students': students, 'query': query},
    )

<<<<<<< HEAD

@user_passes_test(staff_check, login_url='login')
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(
        request,
        'registration/student_detail.html',
        {'student': student},
    )


@user_passes_test(staff_check, login_url='login')
=======
>>>>>>> aae1622c46b2c75ac14801e20ae8ec9a373c9856
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
<<<<<<< HEAD
            form.save()
            messages.success(request, 'Student record created successfully.')
            return redirect('student_list')
    else:
        form = StudentForm()
=======
            student = form.save()
            messages.success(request, 'Student record created successfully.')
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm()

>>>>>>> aae1622c46b2c75ac14801e20ae8ec9a373c9856
    return render(
        request,
        'registration/student_form.html',
        {'form': form, 'page_title': 'Register Student'},
    )

<<<<<<< HEAD

@user_passes_test(staff_check, login_url='login')
=======
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'registration/student_detail.html', {'student': student})

>>>>>>> aae1622c46b2c75ac14801e20ae8ec9a373c9856
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student record updated successfully.')
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm(instance=student)
<<<<<<< HEAD
=======

>>>>>>> aae1622c46b2c75ac14801e20ae8ec9a373c9856
    return render(
        request,
        'registration/student_form.html',
        {
            'form': form,
            'page_title': 'Update Student',
            'student': student,
        },
    )

<<<<<<< HEAD

@user_passes_test(staff_check, login_url='login')
=======
>>>>>>> aae1622c46b2c75ac14801e20ae8ec9a373c9856
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student record deleted successfully.')
        return redirect('student_list')
<<<<<<< HEAD
=======

>>>>>>> aae1622c46b2c75ac14801e20ae8ec9a373c9856
    return render(
        request,
        'registration/student_confirm_delete.html',
        {'student': student},
    )