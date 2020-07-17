#To do list application


"""
Semantics

On Run:
Menu is displayed
User is asked to select an operation
on selection, program performs the required operation
"""

# display menu
def Menu():
    print("Select 1: Create Task")
    print("Select 2: List Task")
    print("Select 3: Update Task")
    print("Select 4: Delete Task")
    print("Select 0: Exit Program")
    return
        
    
# Play application
def PlayApp():
    Menu()
    choice=-1
    while(choice!=0):
        print()
        print("Select option",end='')
        try:
            option=input()
            choice=int(option)
            if choice==1:
                CreateTask()
            elif choice==2:
                ListTask()
            elif choice==3:
                UpdateTask()
            elif choice==4:
                DeleteTask()
            elif choice==0:
                Exit()
        except:
            print("Invalid code")
    return

# Create a task
def CreateTask():
    try:
        print("Enter Title",end='')
        Title=""
        Title=input()
        while(Title=="" or Title==" "):
            print("Enter a title to proceed",end="")    
            Title=input()
        global Tasks
        Tasks.append([Title,"Incomplete"])
        print("Task created")
    except:
        print("Error Occurred: Try again")
    return

# Enlist the tasks
def ListTask():
    global Tasks
    try:
        for i in range(len(Tasks)):
            print("Code: "+str(i+1)+" Title: "+ Tasks[i][0]+ " status: "+Tasks[i][1])
    except:
        print("Error Occurred: Try again")
        
    return

# Updatetasks
def UpdateTask():
    global Tasks
    try:
        print("Select code of task")
        ListTask()
        TaskCode=input()
        TaskCode=int(TaskCode)-1
        print("Select S: Update Status")
        print("Select T: Update Title",end='')
        choice=input()
        while(choice!="S" and choice!="s" and choice!="T" and choice!="t"):
            print("Enter valid choice",end='')
            choice=input()
        if choice=="S" or choice=="s":
            UpdateStatus(TaskCode)
        elif choice=="T" or choice=="t":
            UpdateTitle(TaskCode)
        print("Task updated")
    except:
        print("Error Occurred: Try again")
            
        
    return

# Updatestatus of tasks
def UpdateStatus(TaskCode):
    global Tasks
    try:
        print("Select I: Incomplete")
        print("Select P: In Progress")
        print("Select C: Completed",end='')
        Title=input()
        while(Title!="I" and Title!="i" and Title!="P" and Title!="p" and Title!="C" and Title!="c"):
            print("Enter valid code to proceed",end='')
            Title=input()
        if Title=="I" or Title=="i":
            Tasks[TaskCode][1]="Incomplete"
        elif Title=="P" or Title=="p":
            Tasks[TaskCode][1]="In Progress"
        elif Title=="C" or Title=="c":
            Tasks[TaskCode][1]="Completed" 
    except: 
        print("Error Occurred: Try again")
    return

# Update title of tasks
def UpdateTitle(TaskCode):
    global Tasks
    try:
        print("Enter new title: ",end='')
        Title=input()
        while(Title=="" or Title==" "):
            print("Enter a valid title to proceed",end='')    
            Title=input()
        Tasks[TaskCode][0]=Title
    except:
        print("Error Occurred: Try again")
    return
    

#delete tasks
def DeleteTask():
    global Tasks
    try:
        print("Select code of task")
        ListTask()
        TaskCode=input()
        TaskCode=int(TaskCode)-1
        Tasks.pop(TaskCode)
        print("Task deleted")
    except:
        print("Error Occurred: Try again")
    return

# exit program
def Exit():
    return 0


Tasks=[]
PlayApp()



