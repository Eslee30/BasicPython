import datetime
import calendar
import random

#KALKULATOR

def calculator():
    while True:
        print()
        print("---Select operation---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
    
        operation = input("Select operation: ")
    
        if operation in ("1", "2", "3", "4"):
            num_01 = float(input("Enter first number: "))
            num_02 = float(input("Enter second number: "))
            
            if operation == "1":
                num_01 = str(num_01)
                num_02 = str(num_02)
                print("The result is:")
                print(num_01 + " + " + num_02 + " = " + str(num_01 + num_02))
                   
            elif operation == "2":
                num_01 = str(num_01)
                num_02 = str(num_02)
                print("The result is:")
                print(num_01 + " - " + num_02 + " = " + str(num_01 - num_02))

            elif operation == "3":
                num_01 = str(num_01)
                num_02 = str(num_02)
                print("The result is:")
                print(num_01 + " x " + num_02 + " = " + str(num_01 * num_02))
                   
            elif operation == "4":
                num_01 = str(num_01)
                num_02 = str(num_02)
                print("The result is:")
                print(num_01 + " : " + num_02 + " = " + str(num_01 / num_02))
            
        elif operation == "5":
            print("Thank you... Bye!")
            break

        else:
            print("Sorry, I don't understand. Please try again.")


#AGENDA

list_agenda = []

def event_input():
    event_name = input("What is the name of the event? ")
    event_day = int(input("What is the day of the event (1-7)? "))
    
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
        
    event_date = input("What is the date of the event (DD/MM/YY)? ")
    event_time = input("What is the time of the event (HH:MM)? ")

    dict_agenda = {
    "Event": event_name,
    "Day": weekday,
    "Date": event_date,
    "Time": event_time
    }
    
    list_agenda.append(dict_agenda)
    
    text_file_01 = open("agenda.txt","wt")
    text_file_01.write(str(list_agenda))
    text_file_01.close()
    
    print(event_name + " on " + weekday + ", " + event_date + " at " + event_time + " saved in agenda.")

def agenda():
    print("Welcome to the AI personal agenda!")
    print()
    print(calendar.calendar(datetime.datetime.now().year))
    
    while True:
        print()
        print("---Menu---")
        print("1. Add event")
        print("2. View agenda")
        print("3. Exit agenda")
    
        agenda_menu_input = input("Select menu: ")
    
        if agenda_menu_input == "1":
            event_input()
            
        elif agenda_menu_input == "2":
            if list_agenda == []:
                print("Agenda empty.")
            else:
                print("-Agenda-")
                for q in list_agenda:
                    print("Event: {}".format(q["Event"]))
                    print("Day: {}".format(q["Day"]))
                    print("Date: {}".format(q["Date"]))
                    print("Time: {}".format(q["Time"]))
                   
        elif agenda_menu_input == "3":
            print("Thank you... Bye!")
            break
            
        else:
            print("Sorry, I don't understand. Please try again.")


#BOTCHAT

list_chat = []

def chatbot():
    while True:
        chat = input("You: ")

        if "Who" in chat or "name" in chat or "Name" in chat:
            answer_name = [
            "My name's AI. What's yours?",
            "Thank you for asking. I'm AI.",
            "I'm AI. Nice to meet you... :)",
            "Glad you ask. My name is AI, your very own virtual assistant."
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

        text_file_02 = open("chatbot.txt", "wt")
        text_file_02.write(str(list_chat))
        text_file_02.close()

# ## Tugas Akhir

print("Hi, I'm AI, your virtual assistant!")
name = input("What is your name? ")
print("Hello, " + name + "!")

while True:
    print()
    print("How can I help you?")
    print("1. Calculator")
    print("2. Agenda")
    print("3. Chatbot")
    print("4. Exit")

    choice = input("Select: ")

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