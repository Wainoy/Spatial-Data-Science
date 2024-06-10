# strings are written using single or double quotation marks.
#longer strings are written using triple quotes '''   '''
# an empty string can be defined ("")
course_intro = '''
Hello Eve, 
You are now learning python. All the best'''
print(course_intro)
print(course_intro[-3])
print(course_intro[:-1])
print(len(course_intro))
print(course_intro[:54])
print(course_intro[0:4]) #prints characters at index 0, 1, 2 and 3. character at [0] is a new line character
#passing strings
school_intro = course_intro[:]
print(school_intro)
