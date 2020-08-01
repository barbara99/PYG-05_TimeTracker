
import csv

def getHours():             #function to calculate hours spent on task
    #Global variables to be used in other functions
    global hours   #number of hours spent
    global today        #gets date of making entry 
    global start_time
    global end_time, task, description
    print("This program calculates fees paid per hour.Enter hour in H:m using the 24 hour format.")
    today = date.today()
    
    start_time = input('Enter time started in H:m format: ')        #gets start time from user
    end_time = input('Enter time ended in H:m format: ')       #gets time of completion of tsk
    task= input('Enter task name: ')
    description = input('Give a brief description of task: ')
    
    start_time_str = start_time
    start_time_object = datetime.strptime(start_time_str, '%H:%M').time()   

    end_time_str = end_time
    end_time_object = datetime.strptime(end_time_str, '%H:%M').time()

    #print(start_time_object, end_time_object)
    

    time_elapsed = datetime.combine(date.today(), end_time_object) - datetime.combine(date.today(), start_time_object)
    #print(time_elapsed)

    total_seconds=time_elapsed.seconds
    #print(total_seconds)

    hours = total_seconds/3600                    #calculates total time spent on task
    print("Number of hours spent on task is ",hours,"hours.")
