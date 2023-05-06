
from datetime import datetime
from datetime import date
import calendar


# def question():
#     print("Which day of the week do yo want to count ?")
#     index = list(range(1,8))
#     for i, day in zip(index, calendar.day_name):
#         print (str(i) + ": " + day)
#     print("Or 'exit' to quite")
#     answer_day = input("?")
#     try:
#         answer_day_num = int(answer_day)
#         if answer_day == 'exit':
#             exit 
#         elif answer_day_num in range(1,7):
#             answer_month = input("Enter month:")
#             answer_month_num = int(answer_month)
#             if answer_month_num in range(1,12):
#                 answer_year = input ("Enter Year:")
#                 answer_year_num = int(answer_year)
#                 if answer_year_num > 0:
#                     print(answer_day_num,answer_month_num,answer_year_num)
#                     return(answer_day_num, answer_month_num, answer_year_num)
#                 else:
#                     print("Not valid input choose number equle 0 or greater")
#                     question()
#             else:
#                 print("Not valid input choose number 1 to 12")
#                 question() 
#         else:
#             print("Not valid input choose number 1 to 7")
#             question()
#     except ValueError:
#         print("You didn't give me a valid number!")
#         question()        
               
# question()

def question_day():
    global answer_day_num
    print("Which day of the week do you want to count ?")
    index = list(range(0,7))
    for i, day in zip(index, calendar.day_name):
        print (str(i) + ": " + day)
    print("Or 'exit' to quite")
    answer_day = input("Enter day: ")
    if answer_day == 'exit':
            exit()
    else:
        try:
            answer_day_num = int(answer_day)
            if answer_day_num in range(0,7):
                print("Chosen day: ",answer_day_num)
                return answer_day_num   
            else:
                print("Not valid input choose number 0 to 6")
                question_day()

        except ValueError:
            print("You didn't give me a valid number!")
            question_day()
       
def question_month():
    global answer_month_num
    try:             
        answer_month = input("Enter month: ")
        answer_month_num = int(answer_month)
        if answer_month_num in range(1,13):
            print("Chosen month: ",answer_month_num)
            return answer_month_num 
        else:
            print("Not valid input choose number 1 to 12")
            print("Chosen day: ",answer_day_num)
            question_month()

    except ValueError:
        print("You didn't give me a valid number!")
        print("Chosen day: ",answer_day_num)
        question_month()

def question_year():
    global answer_year_num
    try:
        answer_year = input ("Enter Year: ")
        answer_year_num = int(answer_year)
        if answer_year_num > 0:
            print("Chosen year: ",answer_year_num)
            return answer_year_num
        else:
            print("Not valid input choose number greater then 0")
            print("Chosen day: ",answer_day_num)
            print("Chosen month: ",answer_month_num)
            question_year()

    except ValueError:
        print("You didn't give me a valid number!")
        print("Chosen day: ",answer_day_num)
        print("Chosen month: ",answer_month_num)
        question_year()

while  True:     
    question_day()
    question_month()
    question_year()

    cal = calendar.monthcalendar(answer_year_num,answer_month_num)
    choosen_day_list = [el[answer_day_num] for el in cal]
    day_within_month = []
    for i in choosen_day_list:
        if i > 0: 
            day_within_month.append(i)
        else:
            continue
    print("There are ", len(day_within_month)," of those days in month and year specied \n --------------------")



