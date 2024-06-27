class college:
    
    def collegename(self, c_name):
        print(f"The college name is {c_name}")

    
class department(college):

    def department(self, d_name):
        print(f"The department name is {d_name}")

    
class hod(department):

    def hodname(self, h_name):
        print(f"The HOD name is {h_name}")

    
class staff(hod):

    def staffname(self, sf_name):
        print(f"The staff name is {sf_name}")

    
class student(staff):

    def studentname(self, st_name):
        print(f"The student name is {st_name}")


student_obj = student()

c_name = input("College name? ")
student_obj.collegename(c_name)

d_name = input("Department name? ")
student_obj.department(d_name)

h_name = input("HOD name? ")
student_obj.hodname(h_name)

sf_name = input("staff name? ")
student_obj.staffname(sf_name)

st_name = input("student name? ")
student_obj.studentname(st_name)