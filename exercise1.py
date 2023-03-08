#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def printFullName(self):
        return(self.firstname + " " + self.lastname)

class Student(Person):
    def __init__(self,firstname,lastname,subject):
        super(Student,self).__init__(firstname,lastname)
        self.subject = subject
    
    def printNameSubject(self):
        print(self.printFullName() + " is in subject: " + self.subject)
    
class Teacher(Person):
    def __init__(self,firstname,lastname,course):
        super(Teacher,self).__init__(firstname,lastname)
        self.course = course
    def printNameCourse(self):
        print(self.printFullName() + " teaches the course " + self.course)

me = Student('Benedikt', 'Daurer', 'physics')
me.printNameSubject()
filipe = Teacher("Filipe", "Maia", "Python programming")
filipe.printNameCourse()