
import csv
from datetime import date, datetime


def get_hours():
    """
    function to calculate hours spent on task
    Global variables to be used in other functions
    """

    print('This program calculates fees paid per hour.Enter hour in H:m using the 24 hour format.')

    today = datetime.today()
    start_time = input('Enter time started in H:m format: ')
    end_time = input('Enter time ended in H:m format: ')
    task = input('Enter task name: ')
    description = input('Give a brief description of task: ')

    # start_time_str = start_time
    start_time = datetime.strptime(start_time, '%H:%M').time()
    end_time = datetime.strptime(end_time, '%H:%M').time()

    # print(start_time_object, end_time_object)

    time_elapsed = datetime.combine(
        datetime.today(), end_time) - datetime.combine(date.today(), start_time)
    total_seconds = time_elapsed.seconds
    # print(total_seconds)
    hours = total_seconds/3600

    print('Number of hours spent on task is ', hours, 'hours.')

    get_price(hours)
    save_to_csv(today, task, description, hours, start_time, end_time)

# utilities
# its important to make your code functional and reusable
def get_price(hours):
    """
    calculates total amount for hours
    :param hours: hours spent 
    """
    price = round(hours * 5, 2)
    print("Total Price is $", price)


def save_to_csv(today, task, description, hours, start_time, end_time):
    """
    Write the file to CSV
    :param today: today
    :param task: etc
    """
    fee = '$5'
    with open('timeTracker.csv', 'a', newline='') as file:
        fieldnames = ['Date', 'Task Name', 'Description', 'Start Time',
                      'End Time', 'Number of hours', 'Price per hour', 'Fee Charged']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'Date': today, 'Task Name': task, 'Description': description, 'Start Time': start_time, 'End Time': end_time,
                         'Number of hours': hours, 'Price per hour': fee, 'Fee Charged': price})


def main():
    get_hours()


if __name__ == "__main__":
    main()
