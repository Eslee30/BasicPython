#!/usr/bin/env python
# coding: utf-8

# In[64]:


#KALKULATOR

def select_operation():
    print()
    print("---Select operation---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
def calculator():
    while True:
        select_operation()
    
        operation = input("Select operation: ")
    
        if operation in ("1", "2", "3", "4"):
            num_01 = float(input("Enter first number: "))
            num_02 = float(input("Enter second number: "))
            
            if operation == "1":
                x = str(num_01 + num_02)
                num_01 = str(num_01)
                num_02 = str(num_02)
                print("The result is:")
                print(num_01 + " + " + num_02 + " = " + x)
                   
            elif operation == "2":
                y = str(num_01 - num_02)
                num_01 = str(num_01)
                num_02 = str(num_02)
                print("The result is:")
                print(num_01 + " - " + num_02 + " = " + y)

            elif operation == "3":
                p = str(num_01 * num_02)
                num_01 = str(num_01)
                num_02 = str(num_02)
                print("The result is:")
                print(num_01 + " x " + num_02 + " = " + p)
                   
            elif operation == "4":
                q = str(num_01 / num_02)
                num_01 = str(num_01)
                num_02 = str(num_02)
                print("The result is:")
                print(num_01 + " : " + num_02 + " = " + q)
            
        elif operation == "5":
            print("Thank you... Bye!")
            break

        else:
            print("Sorry, I don't understand. Please try again.")


# In[65]:


#AGENDA

import datetime
import calendar

list_agenda = []

def agenda_menu():
    print("---Menu---")
    print("1. Add event")
    print("2. View agenda")
    print("3. Exit agenda")

def event_input():
    event_name = input("What is the name of the event? ")
    print("What is the day of the event? (Please insert number only)")

    event_day = int(input("Day: "))
    
    if event_day == 1:
        weekday = "Monday"
    elif event_day == 2:
        weekday = "Tuesday"
    elif event_day == 3:
        weekday = "Wednesday"
    elif event_day == 4:
        weekday = "Thursday"
    elif event_day == 5:
        weekday = "Friday"
    elif event_day == 6:
        weekday = "Saturday"
    elif event_day == 7:
        weekday = "Sunday"
    else:
        print("Sorry, I don't understand. Please try again.")
        event_input()
        
    event_date = input("Date: ")
    event_month = input("Month: ")
    event_year = input("Year: ")

    dict_agenda = {
    "Event": event_name,
    "Day": weekday,
    "Date": event_date,
    "Month": event_month,
    "Year": event_year
    }
    
    list_agenda.append(dict_agenda)
    
    text_file_01 = open("agenda.txt","wt")
    text_file_01.write(str(list_agenda))
    text_file_01.close()
    
    print(event_name + " on " + weekday + ", " + event_month + "/" + event_date + "/" + event_year + " saved in agenda.")

def agenda():
    print("Welcome to the AI personal agenda!")
    print()
    print(calendar.calendar(datetime.datetime.now().year))
    
    while True:
        print() 

        agenda_menu()
    
        agenda_menu_input = input("Select menu: ")
    
        if agenda_menu_input == "1":
            event_input()
            
        elif agenda_menu_input == "2":
            if list_agenda == []:
                print("Agenda empty.")
            else:
                print("Agenda:")
                for q in list_agenda:
                    print("Event: {}".format(q["Event"]))
                    print("Day: {}".format(q["Day"]))
                    print("Date: {}".format(q["Date"]))
                    print("Month: {}".format(q["Month"]))
                    print("Year: {}".format(q["Year"]))
                   
        elif agenda_menu_input == "3":
            print("Thank you... Bye!")
            break
            
        else:
            print("Sorry, I don't understand. Please try again.")


# In[66]:


#BOTCHAT

import random
import datetime

list_chat = []

def chatbot():
    while True:
        chat = input("You: ")

        if "Who" in chat or "name" in chat or "Name" in chat:
            answer_name = [
            "My name's AI. What's yours?",
            "Thank you for asking. I'm AI.",
            "I'm AI. Nice to meet you... :)"
            ]
        
            random_answer_name = random.choice(answer_name)
            print("Chatbot: " + random_answer_name)
        
            dict_chat_name = { 
            "You": chat,
            "Chatbot": random_answer_name
            }
            
            list_chat.append(dict_chat_name)
        
        elif "today" in chat or "date" in chat or "day" in chat:
            date_time = datetime.datetime.now()
        
            answer_date = [
            "Today is " + date_time.strftime("%A") + ", " + date_time.strftime("%d") + " " + date_time.strftime("%B") + " " + date_time.strftime("%Y") + ".",
            "Hmm... let me check. It's " + date_time.strftime("%A") + ", " + date_time.strftime("%d") + " " + date_time.strftime("%B") + " " + date_time.strftime("%Y") + "."
            ]
        
            random_answer_date = random.choice(answer_date)
            print("Chatbot: " + random_answer_date)
        
            dict_chat_date = {
            "You": chat,
            "Chatbot": random_answer_date
            }
        
            list_chat.append(dict_chat_date)
        
        elif "show" in chat or "response" in chat or "responses" in chat or "all" in chat or "chats" in chat:
            print()
            print("Here are all of your chats:")
            for i in list_chat:
                print("You: {}". format(i["You"]))
                print("Chatbot: {}".format(i["Chatbot"]))
            print()
    
        elif "end" in chat or "End" in chat or "stop" in chat or "Stop" in chat:
            print("Thank you for chatting. Bye...")
            break
        
        else:
            answer_else = [
            "Wow, that's very interesting. Tell me more!!!",
            "I don't what that is... what is that?",
            "I learned a lot from you today :)",
            "I don't what that is. Can you explain it for me?",
            "Hmmm... very interesting :>"
            ]
            
            random_answer_else = random.choice(answer_else)
            print("Chatbot: " + random_answer_else)
            
            dict_chat_else = {
            "You": chat,
            "Chatbot": random_answer_else
            }
            
            list_chat.append(dict_chat_else)


# ## Tugas Akhir

# In[ ]:


#### import datetime
import calendar
import random

def menu():
    print()
    print("-----Menu-----")
    print("1. Calculator")
    print("2. Agenda")
    print("3. Chatbot")
    print("4. Exit")
    
print("Hi, I'm AI, your virtual assistant!")
name = input("What is your name? ")
print("Hello, " + name + "!")
print("How can I help you?")

while True:
    menu()

    choice = input("Select menu: ")

    if choice == "1":
        calculator()
        
    elif choice == "2":
        agenda()
        
    elif choice == "3":
        chatbot()
    
    elif choice == "4":
        print("Thank you... Bye!")
        break

    else:
        print("Sorry, I don't understand. Please try again.")