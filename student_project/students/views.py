from django.shortcuts import get_object_or_404, render

from .models import Student


def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {
        'students': students
    })

def student_detail(request, id):
    student = get_object_or_404(Student, id=id)

    return render(request, 'students/student_detail.html', {
        'student': student
    })