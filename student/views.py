from django.shortcuts import render,redirect
# from django.http import HttpResponseRedirect
# from django.urls import reverse
from .models import Student

# Create your views here.
def index(request):
    students = Student.objects.all()

    context = {'students':students}
    return render(request, 'index.html', context)

def view_student(request, id):
    student = Student.objects.get(pk=id)
    # return HttpResponseRedirect(reverse('index'))
    return redirect('index')

def add(request):
    if request.method == 'POST':
        new_student_number = request.POST.get('student_number')
        new_first_name = request.POST.get('first_name')
        new_last_name = request.POST.get('last_name')
        new_email = request.POST.get('email')
        new_field_of_study = request.POST.get('field_of_study')
        new_gpa = request.POST.get('gpa')

        new_student = Student(student_number=new_student_number, first_name=new_first_name, last_name=new_last_name, email=new_email, field_of_study=new_field_of_study, gpa=new_gpa)

        new_student.save()
        return render(request, 'add.html', {'success':True})
    
    else:
        return render(request, 'add.html')


def edit(request, id):
    student = Student.objects.filter(pk=id).all()
    student = student[0]

    if request.method == 'POST':
        new_student_number = request.POST.get('student_number')
        new_first_name = request.POST.get('first_name')
        new_last_name = request.POST.get('last_name')
        new_email = request.POST.get('email')
        new_field_of_study = request.POST.get('field_of_study')
        new_gpa = request.POST.get('gpa')

        student.student_number = new_student_number
        student.first_name = new_first_name
        student.last_name = new_last_name
        student.email = new_email
        student.field_of_study = new_field_of_study
        student.gpa = new_gpa

        student.save()
        return redirect('index')

    return render(request, 'edit.html')
        
    
# def edit(request, id):
#     student = Student.objects.get(pk=id)

#     if request.method == 'POST':
#         new_student_number = request.POST.get('student_number')
#         new_first_name = request.POST.get('first_name')
#         new_last_name = request.POST.get('last_name')
#         new_email = request.POST.get('email')
#         new_field_of_study = request.POST.get('field_of_study')
#         new_gpa = request.POST.get('gpa')

#         student.student_number = new_student_number
#         student.first_name = new_first_name
#         student.last_name = new_last_name
#         student.email = new_email
#         student.field_of_study = new_field_of_study
#         student.gpa = new_gpa

#         student.save()
#         return redirect('index')

#     return render(request, 'edit.html', )

def delete(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return redirect('index')