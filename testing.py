import random
import time
class Student: #student class
    def __init__(self, fname, lname, GPA, Grade, teacher):
        self.fname =fname
        self.lname = lname
        self.GPA = GPA
        self.Grade = Grade
        self.teacher = teacher
        temp =str("     "+ str(self.fname) + " " + str(lname) + " has a GPA of "+ str(self.GPA) + " and is in "+ str(self.Grade) +" grade. His teacher is Mr."+ str(self.teacher))
        print(temp)
        
class Teacher: # teacher class
    def __init__(self, fname, lname, Grades, ):
        self.fname =fname
        self.lname = lname
        self.Grades = Grades
        temp = str(self.fname) + " " + str(lname) + " teaches " + str(self.Grades) + " grade and has the following students"
        print (temp)
        
class School: #school class
    def __init__(self, name):
        self.name = name

        temp = str("Welcome to " + name + " school. The roster will load shortly.")

        print(temp)
        time.sleep(10)
        
def getRanName(num): # gets a random name
    fp = open("names.txt")
    for i, line in enumerate(fp):
        if i == num:
            temp = fp.readline()
            fp.close
            return(temp)
def getRanNum(max): #get a random number
    return (random.randint(0, max))

def getGrade(num): # check grade
    if num == 0:
        return "K"
    else:
        return num

def creatStu(num, teacher, grade): #makes al the students
    students = []
    for x in range (0, num):
        tempStu = Student(getRanName(getRanNum(2498)),getRanName(getRanNum(2498)),getRanNum(100), grade, teacher)
        students.append(tempStu)
    return students

def creatTea(num): # makes all the teachers
    teach = []
    for x in range(0, num):
        fname = getRanName(getRanNum(2498))
        lname = getRanName(getRanNum(2468))
        grade = getGrade(getRanNum(12))
        temptea = Teacher(fname, lname, grade)
        creatStu(getRanNum(10), lname, grade)
        teach.append(temptea)
    return teach
def creatSchool(): # makes the school
    name = getRanName(getRanNum(2498))
    Schooln = School(name)
    teacher =creatTea(getRanNum(20))
  
creatSchool()

