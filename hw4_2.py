#1
# class GeeksPeople:
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email 
#         self.phone = phone

#     def __str__(self):
#         return f"Имя - {self.name}, почта - {self.email}, телефон - {self.phone}"


# class Student(GeeksPeople):
#     def __init__(self, name, email, phone, student_id, group_where_study):
#         GeeksPeople.__init__(self, name, email, phone)
#         self.student_id = student_id
#         self.group_where_study = group_where_study

#     def __str__(self):
#         return super().__str__() + f"ID: {self.student_id}, группа :{self.group_where_study} "
    
#     def study(self):
#         print(f"ID - {self.student_id}, группа в которой учиться - {self.group_where_study} ")


# student = Student("Нурай","nuraj9663@gmail.com", 755750238,2 , "Backend_12_2B")
# print(student)
# student.study()


# class Teacher(GeeksPeople):
#     def __init__(self, name, email, phone, teacher_id, group_where_theach):
#         GeeksPeople.__init__(self, name, email, phone)
#         self.teacher_id = teacher_id
#         self.group_where_teacher = group_where_theach

#     def teach(self):
#         print(f"ID - {self.teacher_id}, преподает группе - {self.group_where_teacher} ")
    
#     def __str__(self):
#         return super().__str__() + f"ID_teacher: {self.teacher_id}, teach_group :{self.group_where_teacher} "


# teacher = Teacher("Elmira","linalikaya@gmail.com", 507646420,3 , "Backend_13_1B")
# print(teacher)
# teacher.teach()


# class Admin(GeeksPeople):
#     def __init__(self, name, email, phone, admin_id, create_group):
#         GeeksPeople.__init__(self, name, email, phone)
#         self.admin_id = admin_id
#         self.create_group = create_group

#     def create_group1(self):
#         print(f"ID - {self.admin_id}, новая группа - {self.create_group}")

#     def __str__(self):
#         return super().__str__() + f"ID - {self.admin_id}, новая группа - {self.create_group}"


# admin = Admin("Ulan","ulan@gmail.com",722989328,4,"backend_14_1B")
# print(admin)
# admin.create_group1()


# class Mentor(Student, Teacher):
#      def __init__(self, name, email, phone, student_id, group_where_study, teacher_id, group_where_theach):
#          Student.__init__(self, name, email, phone, student_id, group_where_study)
#          Teacher.__init__(self, name, email, phone, teacher_id, group_where_theach)

# mentor = Mentor("Islam","Islam@gmail.com",50567678,5,"backend_14_", 6, "backend_14_2B")
# print(mentor)
# mentor.study()
# mentor.teach()