# Importing libraries
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import pywhatkit as kt
import getpass

# Defining the chatbot
cbot = ChatBot('Baymax')

# Training the chat bot using CorpusTrainer modules
trainer = ChatterBotCorpusTrainer(cbot)
trainer.train(r'C:\Users\Adil\Desktop\IS\training\conversations.yml',
              r'C:\Users\Adil\Desktop\IS\training\greetings.yml',
              r'C:\Users\Adil\Desktop\IS\training\medical.yml',              
              r'C:\Users\Adil\Desktop\IS\training\trivia.yml'
              )

# Local database of diseases with their symptoms
disease_list = [['Covid-19', 'dizziness', 'breathlessness', 'dry cough', 'loss in smell', 0],
                ['Allergic reaction', 'sneezing', 'blocked nose', 'wheezing','itchy rash',0],
                ['Common cold', 'sore throat', 'sneezing', 'runny nose', 'headache',0],
                ['Dehydration', 'dry mouth', 'tiredness', 'lightheaded', 'feeling thirsty', 0],
                ['Flu', 'chesty cough', 'high temperature', 'sore throat','sneezing', 0],
                ['Food poisoning', 'vomiting', 'loss of appetite', 'aching muscles', 'dizziness', 0],
                ['Severe Sunburn', 'swelling of skin', 'chills','dizziness', 'blistering', 0],
                ['Tuberculosis','cough','fever','weight loss','loss of apetite',0],
                ['Diarrhea','abdominal pain','dizziness','vomiting','fever',0],
                ['Cardiovascular Diseases (CVD)','shortness of breath','Chest pain and discomfort','Pain in the upper abdomen','numbness in arms',0],
                ['Diabetes','frequent urination','enhanced thirst','weight loss','extreme fatigue',0],
                ['Malignant','painless lump','fatigue','cough','shortness of breath',0],
                ['Malaria','fever','dizziness','headache','diarrhea',0],
                ['Chronic Obstructive Pulmonary Disease','wheezing','chest stiffness','lethargy','shortness of breath',0],
                ['Dengue','fever','headache','rashes','body pain',0],
                ['Chikungunya','fever','fatigue','rashes','body pain',0],
                ['Arthritis','pain','swelling','reduced motion','stiffness',0],
                ['AIDS','fever','sore throat','fatigue','infections',0],
                ['Chlamydia','genital pain','fluid discharge','pain in genitals','rashes',0],
                ['Depression','anxiety','sleep loss','loss of apetite','thoughts of suicide',0],
                ['Gonorrhoea','pain during urination','pain in the genital tract','abdominal pain','frequent urination',0],
                ['Hemorrhoids','itching','swelling','bleeding','pain',0],
                ['Herpes','sores','blisters','lessions','swelling',0]
]

# Function to check if symptom exists in the existing database and increasing the counter for matched instances
def check_list(symptom, diseases_list):
    for i in range(len(diseases_list)):
        for j in range(1,5):
            if symptom == diseases_list[i][j]:
                diseases_list[i][5] += 1
    return diseases_list

# Function to get index of the disease with the highest probability(count)
def disease_index(diseases_list):
    list1 = [0]*len(diseases_list)
    for i in range(len(diseases_list)):
        list1[i] = diseases_list[i][5]        
    maximum = max(list1)
    index1 = list1.index(maximum)
    if maximum == 0:
        return -1
    return index1

# Function to get index of disease that the user wants to search
def search_disease(Disease, diseases_list):
    for i in range(len(diseases_list)):
        if Disease.lower() == diseases_list[i][0].lower():
            return i
    else:
        return -1

#Function to get a dashed line for aesthetics in terminal
def line():
    print()
    for i in range(0, 72):
        print('-', end= '')
    print()

#Function to get a starred line for aesthetics in terminal
def sline():
    print()
    for i in range(0, 72):
        print('*', end= '')
    print()

#Defining a local user database for existing users   
users_pass = {'abc': '123',
              'xyz': '456'}

#Dictionary to store the basic details of a user
users_details = {'abc': ["5'6", "65 kgs"],
                 'xyz': ["5'7", "72 kgs"]}


#Main function
line()
ch1 = input('\n\t\tNew customer?\n\t(enter y else press any key): ').lower()
temp = []
#Function to add new user in database
if ch1 == 'y': 
    while 1:
        user_name = input("enter new username: ")
        if user_name in users_pass:
            print('User already exists')
        else:
            break
    password = getpass.getpass("enter new password: ")
    users_pass[user_name] = password

    print('\nPlease enter your personal details: ')
    height = input('Enter your height(in inches): ')
    weight = input('Enter your weight(in kgs): ')
    temp.append([height, weight])
    users_details[user_name] = temp
    print('\n\n\tAccount created\n\tPlease login again\n')

line()
count = 3
name = ''
# User login 
while count >= 0:
    user = input("enter username: ")
    pass1 = getpass.getpass("enter password: ")
    if user in users_pass and users_pass[user] == pass1:
        name = user
        break
    else:
        line()
        print(f'Incorrect id/pass\nYou have {count} valid retries left')
        line()
        count -= 1

sline()     
print(f"Baymax- Hello there i'm Baymax\nWelcome {name}")

while True:
    try:
        sline()
        #Menu for convenience of User
        ch2 = input(f'''\nWhat would you like to do today
1. Symptom analysis.
2. Disease symptoms.
3. MEDICAL EMERGENCY.
4. Corona virus test.
5. Do you want to speak to Baymax?
6. View/change user details.
7. Exit.\n''')   

        sline()
        #Swicth case to implement the menu
        match ch2:
            case '1':
                # print('success')
                list1=[] 
                
                line()
                sym1=input('Baymax- what symptom do u have?\n')
                disease_list = check_list(sym1, disease_list)
                list1.append(sym1)
                while True:
                    choice=input('Baymax- Do have any other symptoms?\n')
                    if choice=='yes':
                        sym=input("Baymax- please enter other symptoms\n")
                        disease_list = check_list(sym, disease_list)
                        list1.append(sym)
                    elif choice=='no':
                        break
                    else:
                        print('Baymax- Please enter a valid input')
                index1 = disease_index(disease_list)
                if index1 == -1:
                    print('Baymax- Disease not available in database checking for symptoms online :(')
                    symps='+'.join(list1)
                    print("Baymax- Found details online")
                    kt.search(symps)
                else:    
                    print(f'Baymax- You are most likely suffering from {disease_list[index1][0]}')
                    ch3 = input('Baymax- Do you want to know more about this disease?: ').lower()
                    if ch3 == 'yes':
                        b = disease_list[index1][0]
                        kt.search(b)
                line()

            case '2':
                line()
                a = (input('Baymax- Enter name of disease you want details of: '))
                index2 = search_disease(a, disease_list)
                if index2 == -1:
                    print(f"Baymax- details of {a} not available in existing database :( \nExpanding disease database and Checking disease symptoms online! ")
                    kt.search(a)
                else:
                    print(f"Baymax-Found details of {a}")
                    print("Baymax-These are the symptoms of the following conditions")
                    print(f'1. {disease_list[index2][1]} \n2. {disease_list[index2][2]} \n3. {disease_list[index2][3]} \n4. {disease_list[index2][4]} \n')
                    ch4 = input('Baymax- Do you want to know more about this disease?: ').lower()
                    if ch4 == 'yes':
                        kt.search(a)
                # print(f"Baymax-Found details of {a}")
                # print("Baymax-These are the symptoms of the following conditions")
                # kt.search(a)
                line()

            case '3':
                line()
                c = input('Baymax- Enter your location: ')
                print("Baymax- Finding nearby hospitals")
                b = 'hospitals near ' + c
                kt.search(b)
                line()

            case '4':
                line()
                c = input("Baymax- Enter your location: ")
                print("Baymax- Found test centres near you")       
                b = 'covid test centres near- ' + c
                kt.search(b)
                line()

            case '5':
                sline()
                bot_input = cbot.get_response('hey')
                print('Baymax-',bot_input)
                while 1:
                    a = (input(''))
                    if a.lower() == "quit" or a.lower() == 'exit':
                        break
                    bot_input = cbot.get_response(a)
                    print('Baymax- ',bot_input)
                sline()

            case '6':
                line()
                print(f'{name} details: ')
                print(f'height: - {users_details[name][0]}')
                print(f'weight: - {users_details[name][1]}')
                line()
                ch4 = input('Baymax- Would you like to make changes: ').lower
                if ch4 == 'yes':
                    new_height = input('Enter new height: ')
                    users_details[name][0] = new_height
                    new_weight = input('Enter new weight: ')
                    users_details[name][1] = new_weight
                    print('\nBaymax- Response recorded!\n')
                line()

            case '7':
                print('Baymax- Thank you \nHave a great day :)')
                sline()
                break

            case default:
                print('Invalid Input!')

        # bot_input = cbot.get_response(a)
        # print('Baymax- ',bot_input)
    except(KeyboardInterrupt,EOFError,SystemExit):
        break