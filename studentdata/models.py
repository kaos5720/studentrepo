from django.db import models


class Branch(models.Model):
	branch_name = models.CharField(max_length=200)
	branch_code = models.CharField(primary_key=True, max_length=200	)

	class Meta:
		db_table = "Branch"
	def __str__(self):
		return ("{}".format(self.reg_no))

class Sem(models.Model):
	branch_code = models.ForeignKey(Branch, on_delete=models.CASCADE)
	sem = models.IntegerField(default=0)
	sem_id = models.AutoField(primary_key=True)

	class Meta:
		db_table = "Sem"


class Studentreg2(models.Model):
	first_name= models.CharField(max_length=200)
	last_name= models.CharField(max_length=100)
	reg_no = models.IntegerField(primary_key=True)
	branch_code = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)
	sem = models.ForeignKey(Sem, on_delete=models.CASCADE, null=True)


	class Meta:
		db_table = "Studentreg"

	def __str__(self):
		return ("{} {}".format(self.first_name,self.last_name))

class Subjects(models.Model):
	sem_id = models.ForeignKey(Sem, on_delete=models.CASCADE, null=True)
	subject_name = models.CharField(max_length=200)
	subject_code = models.CharField(primary_key=True, max_length=200)
	
	class Meta:
		db_table = "Subjects"
	def __str__(self):
		return ("{}".format(self.subject_name))

class Student(models.Model):
	reg_no = models.ForeignKey(Studentreg2, on_delete=models.CASCADE, null=True)
	subject_name = models.CharField(max_length=200, null = True)
	total_marks = models.IntegerField(max_length=10, null = True)
	branch_code = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)
	sem = models.ForeignKey(Sem, on_delete=models.CASCADE, null=True)

	class Meta:
		db_table = "Student"


class TotalMarks(models.Model):
	reg_no = models.ForeignKey(Studentreg2, on_delete=models.CASCADE, null=True)
	subject_name = models.CharField(unique = True, max_length=200, null=True)
	total_marks = models.IntegerField(max_length=10, null = True)
	# subject_id = models.ForeignKey(Sem, on_delete=models.CASCADE, null=True)

	class Meta:
		db_table = "Marks"