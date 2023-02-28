#!/usr/bin/env python3.4

import os,sys
import cgi, cgitb
cgitb.enable()
sys.stderr = sys.stdout

print('''\
Content-type:text/html\r\n
<html>
<head>
<title>Форма, строка запроса, запись и считывание</title>
</head>
<body>
<pre>
''')

form = cgi.FieldStorage()

print ("ключи(form.keys):",form.keys())
form_keys=list()
form_values=list() 
print  ("Названия ключей   и их значения (как есть)")
i=0
for key in form.keys():
    print  (i,  ": ", key," = ", form.getvalue(key))
    form_keys.append(key)
    i+=1
# сортируем список ключей (что-бы поля не сбоили при выводе в файл)
form_keys.sort() 
print  ("\n","Ключи  и их значения(после сортировки)")
i=0
for form_key in form_keys:
    form_value = form.getvalue(form_key)
    print  (i,  ": ", form_key," = ", form_value)
    form_values.append(form_value)
    i+=1
print(form_keys)
print(form_values)    


if "000_file_name" not in form:
    print ('''
    <form  action="http://g06u33.nn2000.info/cgi-bin/form_action.py"   target='_self' method='get'>
    Название файла: <input type="Техт" name="000_file_name" value="qs_file.txt" >
    Тип записи в файл:<select name="010_mode">
        <OPTION value="a">a - дозаписать в файл</OPTION> 
        <OPTION value="w">w - очисить файл и записать в файл</OPTION> 
        </select>
    Первая переменная: <input type="Техт" name="variable1" value="Иван" >
    Вторая переменная: <input type="Техт" name="variable2" value="1990" >
    <input type="reset"  name="reset" value="Обновить">
    <input type="submit" name="submit" value="Отправить">
    </form>
    ''')
else:
    print ("\nЗаписываем в файл:", form["000_file_name"].value)
    file = "../tmp/"+form["000_file_name"].value
    if(form["010_mode"].value=='w'):#0 - очищаем файл 
        file_stream = open(file, mode='w', encoding="utf-8", errors=None)
        file_stream.close()
    file_stream = open(file, mode='a', encoding="utf-8", errors=None)
    for form_key in form_keys:
        form_value = form.getvalue(form_key)
        file_stream.write("%2s ;%2s ;" % (form_key, form_value ))
    file_stream.write("\n")
    file_stream.close()
    print ("\nЗаписано в:", file)
    print("\nСчитываем данные из файла и обрабатываем")
    r_stream = open(file, mode='r', encoding="utf-8")
    for line in r_stream.readlines():
        print ('line: ',line,end='')
        words = line.split("; ")
        #print ("words:\n",words)

    print('''
</pre>
</body>
<html>
''')