from django.urls import path, include
from . import views
from django.contrib import admin
# from studentdata.prac import Data

urlpatterns = [
	path("admin/", admin.site.urls),
	path("student", views.get_student_data),
	path("student/register", views.student_reg_form),
	path("student/marks",views.marks_entry),
	path("student/findmarks",views.find_marks)
    # path("students/",views.display, name='display' ),
    # path("students/passed/",views.passed, name='passed'),
    # path("students/failed/",views.failed, name='failed'),
    # path("students/addstudent/",views.add_student, name='add_student')
]	