# Importing libraries
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import pywhatkit as kt
import getpass

# Defining the chatbot
cbot = ChatBot('Baymax')

# Training the chat bot using yml files
trainer = ChatterBotCorpusTrainer(cbot)
trainer.train(r'C:\Users\Adil\Desktop\IS proj\training\conversations.yml',
              r'C:\Users\Adil\Desktop\IS proj\training\greetings.yml',
              r'C:\Users\Adil\Desktop\IS proj\training\medical.yml',              
              r'C:\Users\Adil\Desktop\IS proj\training\trivia.yml'
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
            if symptom.lower() == diseases_list[i][j].lower():
                diseases_list[i][5] += 1

    return diseases_list

# Function to get index of the disease with the highest probability(count)
def disease_index(diseases_list):
    x = []
    list1 = [0]*len(diseases_list)

    for i in range(len(diseases_list)):
        list1[i] = diseases_list[i][5]

    maximum = max(list1)
    for i in range(len(list1)):
        if list1[i] == maximum:
            x.append(i)
            
    if maximum == 0:
        return None

    return x

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
    print('-'*72)
    print()

#Function to get a starred line for aesthetics in terminal
def sline():
    print()
    print('*'*72)
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
    users_details[user_name] = []

    print('\nPlease enter your personal details: ')
    height = input('Enter your height(in inches): ')
    weight = input('Enter your weight(in kgs): ')

    users_details[user_name] += [height, weight]
    print('\n\n\tAccount created\n\tPlease login again\n')

line()
count = 4
name = ''
# User login 
while count > 0:
    user = input("enter username: ")
    pass1 = getpass.getpass("enter password: ")
    if user in users_pass and users_pass[user] == pass1:
        name = user
        break

    else:
        line()
        count -= 1
        print(f'Incorrect id/pass\nYou have {count} valid retries left')
        line()
        if count == 0:
            exit()

sline()     
print(f"Baymax- Hello there i'm Baymax\nWelcome {name}")

while True:
    try:
        sline()
        sline()
        inp = input(f'{name}- ')

        if 'symptom' in inp.lower():
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

            index_list = disease_index(disease_list)

            if index_list == None:
                print('Baymax- Disease not available in database checking for symptoms online :(')
                symps='+'.join(list1)
                print("Baymax- Found details online")
                kt.search(symps)

            else: 
                if len(index_list) == 1:   
                    print(f'Baymax- You are most likely suffering from {disease_list[index_list[0]][0]}')
                    ch3 = input('Baymax- Do you want to know more about this disease?: ').lower()
                    if ch3 == 'yes':
                        b = disease_list[index_list[0]][0]
                        kt.search(b)

                else:
                    l2 = [0]*len(index_list)
                    print(f'Baymax- You have symptoms of following diseases: - ')  
                    for i in range(len(index_list)):
                        l2[i] = disease_list[index_list[i]][0]
                        print(f'{i+1}. {disease_list[index_list[i]][0]}')
                    ch3 = input('Baymax- Do you want to know more about this disease(s)?: ').lower()
                    if ch3 == 'yes':
                        for i in range(len(index_list)):
                            x = l2[i]
                            kt.search(x)

            for i in range(len(disease_list)):
                disease_list[i][5] = 0        
            line()
            
        elif 'disease' in inp.lower():
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
            line()
            
        elif 'emergency' in inp.lower():
            line()
            print("Baymax- Enter your location")
            print("Baymax- Finding nearby hospitals")  
            c = input('')
            b = 'hospitals near- ' + c
            kt.search(b)
            line()

        elif 'test' in inp.lower() or 'rt-pcr' in inp.lower():
            line()
            print("Baymax- Enter your location")
            c = input('')
            print("Baymax- Found test centres near you")       
            b = 'covid test centres near- ' + c
            kt.search(b)
            line()

        elif 'setting' in inp.lower():
            line()
            print(f'Baymax- Hello {name} \nWhat would you like to do today?')
            ch5 = input('1. View user details \n2. Change user details \n')

            if ch5 == '1':
                print(f'{name} details: ')
                print(f'height: - {users_details[name][0]}')
                print(f'weight: - {users_details[name][1]}')

            elif ch5 == '2':
                new_height = input('Enter new height: ')
                users_details[name][0] = new_height
                new_weight = input('Enter new weight: ')
                users_details[name][1] = new_weight
                
                print('\nBaymax- Response recorded!\n')
            line()

        elif 'exit' in inp.lower() or 'quit'in inp.lower() or 'bye' in inp.lower():
            print('Baymax- Thank you \nHave a great day :)')
            sline()
            exit()
            
        else:
            bot_input = cbot.get_response(inp)
            print('Baymax-',bot_input)

    except(KeyboardInterrupt,EOFError,SystemExit):
        break