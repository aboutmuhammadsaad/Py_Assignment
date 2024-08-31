def manage_student_database():
    name:str=""
    student_list:list=[]
    id=1

    while True:
        name=input("Please enter the student's name (or type 'stop' to finish): ").strip()
        name= ' '.join(name.split())

        if name.lower()=="stop":
            break
        
        new_tuple=(id, name)
        
        names = [name for _, name in student_list]
        if new_tuple[1] not in names:
            student_list.append(new_tuple)
            id +=1
        else:
            print("This name is already in the list.")
    
    print("Complete List of Students (Tuples):")
    print(student_list)

    print("List of Students with IDs:")
    for a in student_list:
        print(f"ID: {a[0]} Name: {a[1]} ")
    
    print(f"Total number of students:{len(student_list)}")
    
    l=0
    names = [name for _, name in student_list]
    for h in names:
        d= len(h)
        l += d
        
    print(f"Total length of all student names combined:{l}")
    print(f"The student with the longest name is: {max(names, key=len)}")
    print(f"The student with the shortest name is: {min(names, key=len)}")

manage_student_database()    
    
    
    

