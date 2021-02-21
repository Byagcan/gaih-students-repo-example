#!/usr/bin/env python
# coding: utf-8

# In[ ]:


student1=input("Name and Surname: ")
student2=input("Name and Surname: ")
student3=input("Name and Surname: ")
student4=input("Name and Surname: ")
student5=input("Name and Surname: ")

notes1=[int(input("Midterm1:")),int(input("Final1:")),int(input("Homework1:"))]
notes2=[int(input("Midterm2:")),int(input("Final2:")),int(input("Homework2:"))]
notes3=[int(input("Midterm3:")),int(input("Final3:")),int(input("Homework3:"))]
notes4=[int(input("Midterm4:")),int(input("Final4:")),int(input("Homework4:"))]
notes5=[int(input("Midterm5:")),int(input("Final5:")),int(input("Homework5:"))]

Students=[student1,student2,student3,student4,student5]
StudentNotes=[notes1,notes2,notes3,notes4,notes5]
print("Student's Name-Surname: ",Students)
print("Student's Notes: ",StudentNotes)

sum1=0
for i in notes1:
  sum1 +=i
avg1=sum1/3  

sum2=0
for i in notes2:
  sum2 +=i
avg2=sum2/3

sum3=0
for i in notes3:
  sum3 +=i
avg3=sum3/3

sum4=0
for i in notes4:
  sum4 +=i
avg4=sum4/3

sum5=0
for i in notes5:
  sum5 +=i
avg5=sum5/3

Avg=[avg1,avg2,avg3,avg4,avg5]
print("Student's Average: ",Avg)

information={student1:avg1,student2:avg2,student3:avg3,student4:avg4,student5:avg5}
print("Student's İnformation: ",information)    
max=avg1
congrats=student1
for i,j in information.items():
  if(j>max):
    max=j
    congrats=i 
print("CONGRATULATE FOR YOUR SUCCSESS",congrats,"with score of: ",max)

