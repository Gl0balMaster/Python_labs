"""создать структуру в которой храниться:
        шифр участника
        класс
        фамилия
        оценка по каждой задаче(всего 5 заданий) вводяться пользователем с клафиатуры
(ищется из изначального файла по шифру)

в конце концов вывод по классу, упорядоченного по убыванию и вывод суммарный балл всех участников
каждый класс в свой файл упорядочить по сумме оценок 

"""
from fileinput import filelineno

#шифр CCФФФФ

# student = {"шифр" : str, ""class"" : int, surname : str, t1 : int,t1 : int,t1 : int,t1 : int,t1 : int}

# шифр ККФФФФ
# student = {"шифр" : str, ""class"" : int, surname : str, t1 : int,t1 : int,t1 : int,t1 : int,t1 : int}

code_student_dict = dict()

sum_mark = {
    "11": 0,
    "10": 0,
    "09": 0,
}

def get_student_dict(code, clas, surname):
    code_student_dict[code] = {
        'clas': clas,
        'surname': surname,
        't1' : -1,
        't2': -1,
        't3': -1,
        't4': -1,
        't5': -1
    }

def add_mark(code, mark_num, mark):
    student = code_student_dict.get(code)
    student['t' + str(mark_num)] = mark

def get_all_students(file):
    for line in file:
        #code clas surname
        #0      1   2
        params = line.split()
        code = params[0]
        clas = params[1]
        surname = params[2]
        get_student_dict(code, clas, surname)


def summary_mark_by_class(file):
    for key , value in code_student_dict.items():
        clas = key[:2:]
        for i in range(5):
            sum_mark[clas] += int(code_student_dict[key]['t' + str(i + 1)])
    file.write("\n")
    for mark_class, mark in sum_mark:
        file.write(mark_class + " " + mark + "\n")

def write_out_file(file, code):
    student = code_student_dict[code]
    out = code + " " +  student["clas"] +" " + student["surname"] + " "+ str(student["t1"])+" "+str(student["t2"]) +" "+str(student["t3"])+" "+str(student["t4"]) + " " + str(student["t5"]) + "\n"
    file.write(out)


start_file_name = "start.txt"
start_file = open(start_file_name,'r')
end_file_name = "end.txt"
end_file = open(end_file_name, 'w')


#получаем из файла
get_all_students(start_file)

#ставим оценки
cur_code = str(input())
add_mark(cur_code, 4, 9)



#вывод в файл
for key, value in code_student_dict.items():
    write_out_file(end_file, key)

summary_mark_by_class(end_file)





