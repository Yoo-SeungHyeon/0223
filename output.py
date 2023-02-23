#!/usr/bin/env python
# coding: utf-8

# In[1]:


def output_student(student):
    print('이름 =',student['name'], end='  ')
    print('국어 =',student['kor'], end='  ')
    print('수학 =',student['math'], end='  ')
    print('영어 =',student['eng'], end='  ')
    print('총점 =',student['total'], end='  ')
    print('평균 =',student['avg'], end='  ')
    print('평점 =',student['grade'])

