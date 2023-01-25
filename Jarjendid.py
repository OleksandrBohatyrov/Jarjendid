from random import randint
#spisok=[] #pustoy spisok
#numbers=[1, 2, 3, 4, 5] #numbers
#abc=['Abc', 'B', 'c'] #string
#slovo="Programmeerimine"
#slovo_list=list(slovo)
#print(slovo)
#print(slovo_list)
#while True:
#    print("1- добавить букву в список")
#    print("2- склеить списки\n3-добавить букву на i - позицию\n4-Убрать букву из списка")
#    valik=int(input())
#    if valik==1:
#        a=input("Введи букву ")
#        slovo_list.append(a)
#        print(f"Добавили {a} новый список ", slovo_list)
#    elif valik==2:
#        slovo_list.extend(abc)
#        print(slovo_list)
#    elif valik==3:
#        a=input("Введи букву, которую хочешь добавить")
#        i=int(input("Введи номер позиции, куда хочешь добавить букву"))
#        slovo_list.insert(i-1,a) #0,1,2...
#        print(slovo_list)
#    elif valik==4:
#        a=input("Введи букву, которую хочешь удалить ")
#        n=slovo_list.count(a)
#        if n>10:
#            for i in range(n):
#                slovo_list.remove(a) 
#        else:
#            print("Искомой буквы нет")
#        print(slovo_list)

#--------------------------Nimede lisamine loendisse
#names = []

#for i in range(5):
#    name = input("Sisestage nimi: ")
#    names.append(name)

#print(" ", sorted(names))
#print("Viimati lisatud nimi:", names[-1])

#---------------------------Õpilased
#students = ['Juhan','Kati','Maarja','Mario','Mati']

#while True:
#    print("õpilased nüüd: ", students)
#    valik = input("Mida soovite valida? (add, remove, modify, quit) ")
#    if valik == "add":
#        name = input("Sisestage õpilase nimi, kelle soovite lisada: ")
#        students.append(name)
#    elif valik == "remove":
#        name = input("Sisestage kustutatava õpilase nimi: ")
#        students.remove(name)
#    elif valik == "modify":
#        old_name = input("Sisestage õpilase nimi, keda soovite muuta: ")
#        new_name = input("Sisestage uus nimi: ")
#        index = students.index(old_name)
#        students[index] = new_name
#    elif valik == "quit":
#        break
#    else:
#        print("Vale valik. Palun vali:: add, remove, modify, quit.")

#----------------Duplikaadid
#students = ['Juhan','Kati','Mario','Mario','Mati','Mati']


#ainulaadne_students = set(students)
#print("ainulaadne students:", ainulaadne_students)


#ainulaadne_students = list(dict.fromkeys(students))
#print("ainulaadne students:", ainulaadne_students)

#---------------Vanused

#ages = []
#for i in range(5):
#    ages.append(randint(1, 100))
#print(ages)
#largest_number = max(ages)
#smallest_number = min(ages)

#total = sum(ages)

#average = total / len(ages)

#print("Largest number:", largest_number)
#print("Smallest number:", smallest_number)
#print("Total:", total)
#print("Average:", average)


