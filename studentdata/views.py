from django.shortcuts import render
from rest_framework import viewsets
from .models import Studentreg2,Branch,Sem, Student, Subjects, TotalMarks
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest
import json
from django.http import Http404


# Create your views here.
def get_student_data(request):

	if request.method == "GET":
		reg_no = (request.GET['reg_no'])
		student_object = Student.objects.get(reg_no = reg_no)
		print(student_object.total_marks)
		return HttpResponse(student_object.total_marks)
	

def student_reg_form(request):

	if request.method == 'POST':

		received_json = json.loads(request.body)
		
		branch_object = Branch.objects.get(branch_code = received_json["branch_code"])
		sem_object = Sem.objects.get(sem = received_json["sem"], branch_code = branch_object)
			
		Studentreg2(first_name = received_json["first_name"], last_name = received_json["last_name"],
			 reg_no = received_json["reg_no"], branch_code = branch_object, sem = sem_object).save()
		reg_no_object = Studentreg2.objects.get(reg_no = received_json["reg_no"])
		Student(reg_no = reg_no_object,branch_code = branch_object).save()	
		return HttpResponse("Student registered")

def marks_entry(request):
	if request.method == 'POST':

		received_json = json.loads(request.body)
		reg_no = received_json["reg_no"]
		reg_no_object = Studentreg2.objects.get(reg_no = reg_no)
		if reg_no_object:			
			subject_object = Subjects.objects.get(subject_name = received_json["subject_name"])
			sem_id = reg_no_object.sem_id
			print(sem_id,received_json["subject_name"])
			subject_query = Subjects.objects.filter(sem_id = sem_id, subject_name = received_json["subject_name"])
			print(subject_query)
			if subject_query:
				if TotalMarks.objects.filter(subject_name = subject_object, reg_no = reg_no_object).exists():
					TotalMarks.objects.filter(subject_name=subject_object, reg_no = reg_no_object).update(total_marks=received_json["total_marks"])
					return HttpResponse("Marks updated")
				else:
					TotalMarks(reg_no=reg_no_object,subject_name = subject_object,total_marks=received_json["total_marks"]).save()
					return HttpResponse("Marks added")
			else:
				return HttpResponseBadRequest("Student not registered for  this subject")	
		else:
			raise Http404

def find_marks(request):
	if request.method == 'GET':
		received_json = json.loads(request.body)
		reg_no = received_json["reg_no"]
		if Studentreg2.objects.filter(reg_no = reg_no).exists():
			subject_name = received_json["subject_name"]
			subject_object = Subjects.objects.get(subject_name=subject_name)
			total_marks_query = TotalMarks.objects.filter(subject_name=subject_object,reg_no = reg_no)
			if total_marks_query.exists():
				student_reg = Studentreg2.objects.get(reg_no = reg_no)
				sem_object = Sem.objects.get(sem_id = student_reg.sem_id)
				branch_object = Branch.objects.get(branch_code = sem_object.branch_code_id)
				response = {
					"total_marks": total_marks_query[0].total_marks,
					"student_name" : student_reg.first_name,
					"student_reg_no": student_reg.reg_no,
					"branch_name": branch_object.branch_name,
					"sem":sem_object.sem
			 		}
				return HttpResponse (json.dumps(response),content_type="application/json")
			else:
				return HttpResponseNotFound ("Marks not entered")

			
		else:
			return HttpResponseNotFound ("No student registered")
# def display(request):
# 	st=Studentdatatable.objects.all() # Collect all records from table 
# 	return HttpResponse(st, content_type="application/json") 

# def passed(request):
# 	st=Studentreg.objects.all() 
# 	name=[]
# 	for sts in st:
# 		if sts.total_marks > 50:
# 			name.append(sts.first_name)	

# #	return render(request,'passed.html',{'name':name})
# 	return HttpResponse(name, content_type="application/json") 

# def failed(request):
# 	failed_list = []
# 	print("Printing failed student")
# 	student_fail = Studentreg.objects.filter(pass_status = False)	
# 	for st in student_fail:
# 		student_dict = {"StudentName" : st.first_name}
# 		failed_list.append(student_dict)
# 	print(failed_list)

# 	return HttpResponse(failed_list) 

# def add_student(request):
# 	request_body = json.loads(request.body)
# 	student_data = Studentdatatable(first_name=request_body["first_name"], 
# 		last_name=request_body["last_name"], total_marks = request_body["total_marks"])
# 	student_data.save()
# 	return HttpResponse(json.dumps(request_body), content_type="application/json") 



