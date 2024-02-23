import streamlit as st
import time
import numpy as np
import pandas as pd
import pyttsx3
import streamlit as st
from PIL import Image
import numpy as np


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")  # Haven't found any native Bengali voice for microsoft sapi5 engine :(
engine.setProperty("voice", voices[0].id)

dataset = pd.read_csv("final.csv")
dataset1=pd.read_csv('updated_file.csv')

ANS_QUES_MAP = {
        "Hello There": ["hello", "hi", "hey", "hello there"],
        "I am Fine. What about you?": ["how are you", "how are you doing"],
        "It is nice to hear.": ["fine", "I am also fine", "I am well", "fine thank you", "i am doing well", "pretty good"],
        "I am NextStepBot,I am hear to help you with your carrer,Type Start Test to begain the test": ["who are you", "what is your identity", "what is your name"],
        "Sy MCA Group 1": ["who made you", "who created you", "who is your creator"],
        "You are welcome": ["thanks", "thank you"],
        "Thank you": ["nice", "great", "good", "wonderful"],
        "Should I tell you a joke or play any music for you?": ["my mood is off", "i am not feeling great"]
    }


def ana_one():
    # st.experimental_rerun()
    st.title("Language Recommendation")
    # st.write("This is the content for subpage one.")

    questions = ['',
                'What is your Age?',
                 'You are from which Country?',
                 'The Currency in your Country is?',
                 'Your current position is ',
                 'What is your highest education level',

                 'What is your ethnicity?',
                 'What is your gender?',
                 'DO you have any hobbies?',
                 'Your job satisfaction',
                 'Your job search status',

                 'What is your current Job status',
                 # 'What are the language desired next year',
                 'What language you have worked on 1',
                 'What language you have worked on 2',
                 'What language you have worked on 3',
                 'What are the operating systems you are familiar with',
                 
                 'Your profession',
                 'Current Salary type',
                 'Current salary usd',
                 'Your undergrad majors was in ?',
                 'No of years you have been coding for',

                 'No of years you have been coding professionally',
                 'Your Competence level',
                 'What type of Employement do you expect'
                 ]

    questions_old=['Acedamic percentage in Operating Systems.', 'Acedamic percentage in Algorithms.',
       'Acedamic Percentage in Programming Concepts.',
       'Acedamic Percentage in Software Engineering.', 'Percentage in Computer Networks.',
       'Acedamic Percentage in Electronics Subjects.',
       'Acedamic Percentage in Computer Architecture.', 'Acedamic Percentage in Mathematics.',
       'Acedamic Percentage in Communication skills', 'How many hours of working you will prefer per day?',
       'How much you will rate yourself in Logical quotient?', 'how many hackathons have you participated?', 'How much you will rate yourself in coding skills?',
       'How much you will rate yourself in public speaking?', 'Can you work long time before system?',
       'Are you capable of self-learning?', 'Have you done any Extra-courses?', 'Have you done any certifications?',
       'Workshops done?', 'Have you taken any talent tests before?', 'Have you taken olympiads test?',
       'How are your reading and writing skills?.', 'what is your memory capability score?',
       'What is your interested subjects?', 'What is your interested career area?', 'What will you prefer Job or Higher Studies?',
       'What type of company do you want to settle in?',
       'Have you Taken any inputs from seniors or elders?', 'Are you interested in games?',
       'Which type of Books are you interested?', 'What matters for you most work or salary?',
       'Are you in a Realtionship?', 'What kind of behaviour you have?',
       'Are you intrested in Management or Technical job?', 'What will you prefer?', 'Are you hard worker or smart worker?',
       'Have you worked in teams ever?', 'Are you Introvert?']
    flag=1
    st.title("NextStepBot")
    # banner=Image.open("img/21.png")
    # st.image(banner, use_column_width=True)
    st.write("Hi! I'm NextStepBot, your personal career counseling bot. Ask your queries in the text box below and hit enter. If and when you are ready to take our personality test, type \"start test\" and you're good to go!")


    query = get_text()
    if (query==""):
        ans = "Hi, Dr Mukesh Mohania , I'm NextStepBot. \nHow can I help you?"
        st.text_area("NextStepBot:", value=ans, height=100, max_chars=None)
        speak(ans)

    elif 'start test' in query:
        flag=0
        ans = "Sure, good luck!"
    # elif(flag==0):
    #     #st.write(flag)
    #     ans = "Sure, good luck!"
    #     speak(ans)
    else:
        ans = botans(query)
        st.text_area("NextStepBot:", value=ans, height=100, max_chars=None)
        speak(ans)

    if (flag == 0):

        # st.title("Job MATCH IQ TEST:")
        kr = st.selectbox("Would you like to begin with the test?", ["Select an Option", "Yes", "No"])
        if (kr == "Yes"):

            lis = []
            if (kr == "Yes"):
                st.subheader("Question 1")
                st.write(questions[1])
                inp1 = st.text_input("", key='1')
                if ((inp1 != "")):
                    lis.append(int(inp1))
                    
                    
                    st.subheader("Question 2")
                    st.write(questions[18])
                    inp18 = st.text_input("", key='18')
                    if ((inp18 != "")):
                        lis.append(int(inp18))
                        
                        
                        st.subheader("Question 3")
                        st.write(questions[20])
                        inp20 = st.text_input("", key='20')
                        if ((inp20 != "")):
                            lis.append(int(inp20))
                        
                        
                            st.subheader("Question 4")
                            st.write(questions[21])
                            inp21 = st.text_input(
                                "", key='21')
                            if ((inp21 != "")):
                                lis.append(int(inp21))
                        

                                st.subheader("Question 5")
                                st.write(questions[2])
                                inp2 = st.selectbox("", ['Select an option','United Kingdom', 'United States','South Africa', 'Nigeria' ,'India',
            'Netherlands' ,'Israel', 'Sweden', 'Australia' ,'Greece' ,'Poland' ,'Belgium',
            'Argentina' ,'Russian Federation' ,'Indonesia', 'Germany' ,'Ireland' ,'France',
            'Ukraine', 'Denmark' ,'China', 'Latvia' ,'Algeria','Colombia' ,'Japan',
            'Finland' ,'Romania' ,'Brazil' ,'Bulgaria' , 'Canada' ,'Portugal' ,'Italy' ,'New Zealand', 'Turkey'
            'Czech Republic' ,'Austria', 'Egypt' ,'Spain' ,'Slovakia' ,'Croatia' ,'Mexico',
            'Norway', 'Switzerland' ,'Armenia' ,'Bangladesh' ,'United Arab Emirates',
            'Singapore', 'Dominican Republic', 'Malaysia' ,'Sri Lanka', 'Serbia',
            'Philippines', 'Botswana' ,'Paraguay' ,'Georgia' ,'Uruguay' ,'Belarus',
            'Lithuania', 'Thailand', 'Afghanistan', 'Estonia' ,'Nepal', 'Hungary' ,'Malta',
            'Myanmar', 'Costa Rica' ,'Hong Kong (S.A.R.)' ,'Bosnia and Herzegovina',
            'Ghana', 'Taiwan', 'Lebanon' ,'Peru' ,'Kenya', 'Chile' ,'Viet Nam' ,'Slovenia',
            'Uzbekistan', 'Republic of Korea','El Salvador' ,'Cambodia' ,'South Korea',
            'Tunisia' ,'Saudi Arabia',
            'The former Yugoslav Republic of Macedonia', 'Morocco' ,'Yemen', 'Uganda',
            'United Republic of Tanzania', 'Cuba' ,'Ethiopia' ,'Iceland' ,'Oman',
            'Ecuador', 'Other Country (Not Listed Above)' ,'Jordan',
            'Republic of Moldova' ,'Honduras' ,'Azerbaijan' ,'Cyprus',
            'Syrian Arab Republic', 'Nicaragua', 'Kazakhstan' ,'Kuwait' ,'Cameroon',
            'Luxembourg' ,'Albania' ,'Bahrain' ,'Zimbabwe' ,'Guatemala', 'Mozambique',
            'Bolivia', 'Mauritius', 'Montenegro', 'Sudan', 'Maldives' ,'Turkmenistan',
            'Panama' ,'Lesotho,' 'Somalia' ,'Qatar', 'Mongolia', 'Kyrgyzstan' ,'Swaziland',
            'Rwanda', 'Fiji' ,'Marshall Islands', 'Iraq' ,'Jamaica' ,'Trinidad and Tobago',
            'Libyan Arab Jamahiriya', 'Madagascar' ,'Namibia', 'Tajikistan', 'Malawi',
            'Bhutan' ,"Côte d'Ivoire", 'Andorra','Bahamas' ,'Gambia', 'Sierra Leone',
            'Togo' ,'Zambia', 'Benin' ,'Democratic Republic of the Congo',
            'Suriname', 'Senegal' ,'Liechtenstein',
            'Barbados' ,'Saint Lucia' ,'Monaco', 'Guyana', 'Dominica' ,'Eritrea', 'None',
            'Iran', 'Brunei Darussalam' ,'Gabon', 'Guinea', 'Angola', 'Timor-Leste',
            'Djibouti', 'Burundi' ,'Burkina Faso', 'Haiti',
            'Saint Vincent and the Grenadines', 'San Marino',
            "Lao People's Democratic Republic", 'Seychelles',
            "Democratic People's Republic of Korea", 'Chad', 'Mali' ,'Nomadic',
            'Isle of Man' ,'Kosovo', 'Niger'], key='2')
                                if (inp2 != "Select an option"):
                                    lis.append(inp2)
                                    

                                    st.subheader("Question 6")
                                    st.write(questions[3])
                                    inp3 = st.selectbox("", ['Select an option','British pounds sterling (£)' ,'U.S. dollars ($)',
                                                            'South African rands (R)','Euros (€)' ,'Swedish kroner (SEK)',
                                                            'Australian dollars (A$)' ,'Indian rupees (₹)' ,'Polish złoty (zł)',
                                                            'Russian rubles (₽)' ,'Danish krone (kr)', 'Chinese yuan renminbi (¥)',
                                                            'Japanese yen (¥)' ,'Brazilian reais (R$)','Canadian dollars (C$)',
                                                            'Mexican pesos (MXN$)', 'Norwegian krone (kr)' ,'Swiss francs',
                                                            'Singapore dollars (S$)', 'Bitcoin (btc)'], key='3')
                                    if (inp3 != "Select an option"):
                                        lis.append(inp3)


                                        st.subheader("Question 7")
                                        st.write(questions[4])
                                        inp4 = st.selectbox("",['Select an option','Developer' ,'Manager' ,'Non Developer' ,'Student' ,'Non developer'], key='4')
                                        if (inp4 != "Select an option"):
                                            lis.append(inp4)
                                            

                                            st.subheader("Question 8")
                                            st.write(questions[5])
                                            inp5 = st.selectbox("",['Select an option','Bachelors' ,'Associate' ,'No Degree' ,'Masters' ,'Professional' ,'Doctorate' ,'None'], key='5')
                                            if (inp5 != "Select an option"):
                                                lis.append(inp5)

                                                st.subheader("Question 9")
                                                st.write(questions[6])
                                                inp6 = st.selectbox("",['Select an option','White or European descent' ,'Black or African descent' ,'South Asian',
            'Middle Eastern' ,'Hispanic or Latino' ,'East Asian' 'Native American',
            'None' ,'White or of European descent', 'Black or of African descent',
            'Multiracial' ,'Biracial' ,'Indigenous' ,'Southeast Asian'],key='6')
                                                if (inp6 != "Select an option"):
                                                    lis.append(inp6)

                                                    st.subheader("Question 10")
                                                    st.write(questions[7])
                                                    inp7 = st.selectbox("", ['Select an option','Male' ,'Non-binary' ,'Female' ,'None'],key='7')
                                                    if (inp7 != "Select an option"):
                                                        lis.append(inp7)

                                                        st.subheader("Question 11")
                                                        st.write(questions[8])
                                                        inp8 = st.selectbox("", ['Select an option','Yes' ,'No' ,'None'], key='8')
                                                        if (inp8 != "Select an option"):
                                                            lis.append(inp8)

                                                            st.subheader("Question 12")
                                                            st.write(questions[9])
                                                            inp9 = st.selectbox("", ['Select an option','Moderately dissatisfied' ,'Moderately satisfied',
            'Neither satisfied nor dissatisfied', 'Slightly satisfied',
            'Extremely satisfied', 'Slightly dissatisfied' 'Extremely dissatisfied',
            'None', 'Very satisfied' ,'Very dissatisfied'],key='9')
                                                            if (inp9 != "Select an option"):
                                                                lis.append(inp9)

                                                                st.subheader("Question 13")
                                                                st.write(questions[10])
                                                                inp10 = st.selectbox("", ['Select an option','I am actively looking for a job',
            'I’m not actively looking, but I am open to new opportunities',
            'I am not interested in new job opportunities' 'None']
            ,
                                                                                    key='10')
                                                                if (inp10 != "Select an option"):
                                                                    lis.append(inp10)

                                                                    st.subheader("Question 14")
                                                                    st.write(questions[11])
                                                                    inp11 = st.selectbox("",
                                                                                        ['Select an option','None', 'Not seeking', 'Seeking',
            'I’m not actively looking, but I am open to new opportunities',
            'I am actively looking for a job',
            'I am not interested in new job opportunities']
            ,
                                                                                        key='11')
                                                                    if (inp11 != "Select an option"):
                                                                        lis.append(inp11)

            #                                                            st.subheader("Question 12")
            #                                                            st.write(questions[12])
            #                                                            inp12 = st.selectbox("",['Select an option','Go', 'C#', 'Assembly' ,'C' ,'Matlab', 'Erlang', 'Java', 'Python' ,'PHP',
            # 'JavaScript', 'C++' ,'SQL' ,'CoffeeScript' ,'Groovy' ,'Ruby', 'Haskell' ,'Swift',
            # 'Rust', 'Clojure' ,'Julia' ,'F#' ,'Bash/Shell' ,'TypeScript' ,'Objective-C' ,'R',
            # 'Kotlin', 'Perl' ,'Lua' ,'Scala' ,'Delphi/Object Pascal' ,'HTML' ,'Hack',
            # 'Ocaml' ,'VB.NET' ,'CSS' ,'VBA', 'Cobol', 'Visual Basic 6', 'None' ,'Elixir',
            # 'HTML/CSS' ,'Bash/Shell/PowerShell' ,'Dart', 'Other(s):', 'WebAssembly'],key='12')
            #                                                            if (inp12 != "Select an option"):
            #                                                                lis.append(inp12)

                                                            

                                                                        st.subheader("Question 15")
                                                                        st.write(questions[15])
                                                                        inp15 = st.selectbox("", ['Select an option','Linux-based' ,'Windows' ,'MacOS' ,'BSD/Unix' ,'None'],key='15')
                                                                        if (inp15 != "Select an option"):
                                                                            lis.append(inp15)

                                                                            st.subheader("Question 16")
                                                                            st.write(questions[16])
                                                                            inp16 = st.selectbox("",
                                                                                                ['Select an option','None', 'Non developer' ,'Developer' ,'Novoice' ,'Student' ,'Ex-Developer']

                                                                                                ,
                                                                                                key='16')
                                                                            if (inp16 != "Select an option"):
                                                                                lis.append(inp16)

                                                                                st.subheader("Question 17")
                                                                                st.write(questions[17])
                                                                                inp17 = st.selectbox("",
                                                                                                    [
                                                                                                        'Select an option' ,'Yearly', 'Monthly' ,'Weekly' ,'None']


                                                                                                    ,
                                                                                                    key='17')
                                                                                if (inp17 != "Select an option"):
                                                                                    lis.append(inp17)

                                                                                    

                                                                                    st.subheader("Question 18")
                                                                                    st.write(questions[19])
                                                                                    inp19 = st.selectbox("",
                                                                                                        [
                                                                                                            'Select an option','Other Science' ,'Computer Science' ,'Arts and Science' ,'Engineering',
'No major' ,'Business' ,'Info Systems' ,'Web Design/Dev', 'Math/Stat' ,'None',
'No Major']


                                                                                                        ,
                                                                                                        key='19')
                                                                                    if (
                                                                                            inp19 != "Select an option"):
                                                                                        lis.append(inp19)

                                                                                        

                                                                                    

                                                                                        st.subheader(
                                                                                            "Question 19")
                                                                                        st.write(
                                                                                            questions[22])
                                                                                        inp22 = st.selectbox(
                                                                                            "", [
                                                                                                'Select an option','None' 'Average' ,'A little below average' ,'A little above average',
'Far above average' ,'Far below average']
,
                                                                                            key='22')
                                                                                        if (inp22 != "Select an option"):
                                                                                            lis.append(inp22)
                                                                                            
                                                                                            
                                                                                            st.subheader("Question 20")
                                                                                            st.write(questions[23])
                                                                                            inp23 = st.selectbox("", ['Select an option' ,'Full-time' ,'Part-time' ,'Self-employed' ,'None' ,'Not employed' ,'Student',
'Not employed, and not looking for work' ,'Retired'],key='23')
                                                                                            if (inp23 != "Select an option"):
                                                                                                lis.append(inp23)
                                                                                                
                                                                                                
                                                                                                
                                                                                                st.subheader("Question 21")
                                                                                                st.write(questions[12])
                                                                                                inp12 = st.selectbox("", ['Select an option','JavaScript', 'C#' ,'C', 'Java', 'Assembly' ,'Python', 'C++', 'PHP' ,'SQL',
                                    'Erlang' ,'Go' ,'Ruby', 'Perl', 'Objective-C' ,'Swift' ,'CoffeeScript' ,'Groovy',
                                    'Hack', 'F#' ,'Haskell' ,'Clojure', 'R' ,'Ocaml' ,'Delphi/Object Pascal' ,'VBA',
                                    'Lua' ,'Bash/Shell', 'VB.NET', 'Scala' ,'Matlab' ,'Julia' ,'HTML' ,'Rust',
                                    'Kotlin' ,'TypeScript', 'Cobol' ,'Visual Basic 6' ,'CSS' ,'None' ,'HTML/CSS',
                                    'Bash/Shell/PowerShell' ,'Elixir' ,'Dart' ,'Other(s):' ,'WebAssembly'],

                                                                                                                    key='12')
                                                                                                if (inp12 != "Select an option"):
                                                                                                    lis.append(inp12)

                                                                                                    st.subheader("Question 22")
                                                                                                    st.write(questions[13])
                                                                                                    inp13 = st.selectbox("",
                                                                                                                        ['Select an option','None','Python' ,'JavaScript' ,'C++' ,'HTML' ,'TypeScript' ,'CoffeeScript' ,
                                    'SQL', 'PHP', 'Java' ,'F#', 'C' ,'Go', 'Bash/Shell' ,'Julia', 'R' ,'Ruby', 'C#',
                                    'Swift' ,'Clojure' ,'Haskell' ,'Perl' ,'Objective-C' ,'Kotlin' ,'Groovy', 'Lua',
                                    'VBA' ,'Erlang' ,'Scala' ,'Matlab', 'Delphi/Object Pascal' ,'Visual Basic 6',
                                    'Cobol' ,'Rust' ,'Hack', 'VB.NET' ,'CSS', 'Ocaml' ,'HTML/CSS',
                                    'Bash/Shell/PowerShell' ,'Other(s):' ,'Dart' ,'Elixir' ,'WebAssembly']
                                    ,

                                                                                                                        key='13')
                                                                                                    if (inp13 != "Select an option"):
                                                                                                        lis.append(inp13)

                                                                                                        st.subheader("Question 23")
                                                                                                        st.write(questions[14])
                                                                                                        inp14 = st.selectbox("",['Select an option','Bash/Shell', 'SQL', 'Java', 'Python', 'CSS', 'HTML', 'Erlang', 'None', 'PHP',
                                    'C#', 'Go', 'JavaScript', 'Objective-C', 'C++', 'Groovy', 'Haskell',
                                    'TypeScript', 'Swift', 'Hack', 'Scala', 'R', 'Rust', 'Perl', 'Lua',
                                    'CoffeeScript', 'Matlab', 'Ruby', 'Julia', 'VBA', 'F#', 'Visual Basic 6',
                                    'VB.NET', 'Kotlin', 'Delphi/Object Pascal', 'Clojure', 'Cobol', 'Ocaml',
                                    'HTML/CSS', 'C', 'Other(s):', 'Dart', 'Elixir', 'WebAssembly'],key='14')
                                                                                                        if (inp14 != "Select an option"):
                                                                                                            lis.append(inp14)

                                                                                                            # ALL ENTRIES BY USER ARE DONE
                                                                                                            print(lis)

                                                                                                            st.success("Test Completed")
                                                                                                            st.title("RESULTS:")
                                                                                                            result = output(lis)
                                                                                                            print(result)
                                                                                                            st.subheader("Recommended Language you should learn for better Growth")
                                                                                                            st.subheader(result)
                                                                                                            







def ana_two():
    # st.experimental_rerun()
    st.title("Salary Recommendation")
    # st.write("This is the content for subpage two.")
    #
    # st.title("Subpage One Content -- for language")
    # st.write("This is the content for subpage one.")



    questions = ['',
                 'What is your Age?',
                 'You are from which Country?',
                 'The Currency in your Country is?',
                 'Dev type ',
                 'What is your highest education level',

                 'What is your ethnicity?',
                 'What is your gender?',
                 'What are your hobbies?',
                 'Your job satisfaction',
                 'Your job search status',

                 'Job status',
                 'What language you have worked on 1',
                 'What language you have worked on 2',
                 'What language you have worked on 3',
                 'What are the operating systems you are familiar with',

                 'Your profession',
                 'Current Salary type',
                 '',
                 # 'Current Salary type',
                 # 'Current salary usd',
                 'Your undergrad majors was in ?',
                 'Competence level?',
                 
                 'No of years you have been coding for',
                 'No of years you have been coding professionally',
                 'What is the type of Employement do you expect or are in currently',
                 'What are the language desired next year 1 ',
                 'What are the language desired next year 2 ',

                 'What are the language desired next year 3 ',
                 ]

    questions_old = ['Acedamic percentage in Operating Systems.', 'Acedamic percentage in Algorithms.',
                     'Acedamic Percentage in Programming Concepts.',
                     'Acedamic Percentage in Software Engineering.', 'Percentage in Computer Networks.',
                     'Acedamic Percentage in Electronics Subjects.',
                     'Acedamic Percentage in Computer Architecture.', 'Acedamic Percentage in Mathematics.',
                     'Acedamic Percentage in Communication skills',
                     'How many hours of working you will prefer per day?',
                     'How much you will rate yourself in Logical quotient?',
                     'how many hackathons have you participated?', 'How much you will rate yourself in coding skills?',
                     'How much you will rate yourself in public speaking?', 'Can you work long time before system?',
                     'Are you capable of self-learning?', 'Have you done any Extra-courses?',
                     'Have you done any certifications?',
                     'Workshops done?', 'Have you taken any talent tests before?', 'Have you taken olympiads test?',
                     'How are your reading and writing skills?.', 'what is your memory capability score?',
                     'What is your interested subjects?', 'What is your interested career area?',
                     'What will you prefer Job or Higher Studies?',
                     'What type of company do you want to settle in?',
                     'Have you Taken any inputs from seniors or elders?', 'Are you interested in games?',
                     'Which type of Books are you interested?', 'What matters for you most work or salary?',
                     'Are you in a Realtionship?', 'What kind of behaviour you have?',
                     'Are you intrested in Management or Technical job?', 'What will you prefer?',
                     'Are you hard worker or smart worker?',
                     'Have you worked in teams ever?', 'Are you Introvert?']
    flag2 = 1
    st.title("NextStepBot")
    # banner=Image.open("img/21.png")
    # st.image(banner, use_column_width=True)
    st.write(
        "Hi! I'm NextStepBot, your personal career counseling bot. Ask your queries in the text box below and hit enter. If and when you are ready to take our personality test, type \"start test\" and you're good to go!")

    query = get_text()
    if (query == ""):
        ans = "Hi, Dr Mukesh Mohania, I'm NextStepBot. \nHow can I help you?"
        st.text_area("NextStepBot:", value=ans, height=100, max_chars=None)
        speak(ans)

    elif 'start test' in query:
        flag2 = 0
        ans = "Sure, good luck!"
    # elif(flag==0):
    #     #st.write(flag)
    #     ans = "Sure, good luck!"
    #     speak(ans)
    else:
        ans = botans(query)
        st.text_area("NextStepBot:", value=ans, height=100, max_chars=None)
        speak(ans)

    if (flag2 == 0):

        # st.title("Job MATCH IQ TEST:")
        kr2 = st.selectbox("Would you like to begin with the test?", ["Select an Option", "Yes", "No"])
        if (kr2 == "Yes"):

            lis = []
            if (kr2 == "Yes"):
                st.subheader("Question 1")
                st.write(questions[1])
                inp1 = st.text_input("", key='1')
                if ((inp1 != "")):
                    lis.append(int(inp1))
                    
                    
                    st.subheader("Question 2")
                    st.write(questions[21])
                    inp20 = st.text_input("", key='20')
                    if ((inp20 != "")):
                        lis.append(int(inp20))
                        
                        
                        st.subheader("Question 3")
                        st.write(questions[22])
                        inp21 = st.text_input("", key='21')
                        if ((inp21 != "")):
                            lis.append(int(inp21))
                    
                    

                            st.subheader("Question 4")
                            st.write(questions[2])
                            inp2 = st.selectbox("", ['Select an option', 'United Kingdom', 'United States', 'South Africa',
                                                    'Nigeria', 'India',
                                                    'Netherlands', 'Israel', 'Sweden', 'Australia', 'Greece', 'Poland',
                                                    'Belgium',
                                                    'Argentina', 'Russian Federation', 'Indonesia', 'Germany', 'Ireland',
                                                    'France',
                                                    'Ukraine', 'Denmark', 'China', 'Latvia', 'Algeria', 'Colombia', 'Japan',
                                                    'Finland', 'Romania', 'Brazil', 'Bulgaria', 'Canada', 'Portugal', 'Italy',
                                                    'New Zealand', 'Turkey'
                                                                    'Czech Republic', 'Austria', 'Egypt', 'Spain', 'Slovakia',
                                                    'Croatia', 'Mexico',
                                                    'Norway', 'Switzerland', 'Armenia', 'Bangladesh', 'United Arab Emirates',
                                                    'Singapore', 'Dominican Republic', 'Malaysia', 'Sri Lanka', 'Serbia',
                                                    'Philippines', 'Botswana', 'Paraguay', 'Georgia', 'Uruguay', 'Belarus',
                                                    'Lithuania', 'Thailand', 'Afghanistan', 'Estonia', 'Nepal', 'Hungary',
                                                    'Malta',
                                                    'Myanmar', 'Costa Rica', 'Hong Kong (S.A.R.)', 'Bosnia and Herzegovina',
                                                    'Ghana', 'Taiwan', 'Lebanon', 'Peru', 'Kenya', 'Chile', 'Viet Nam',
                                                    'Slovenia',
                                                    'Uzbekistan', 'Republic of Korea', 'El Salvador', 'Cambodia',
                                                    'South Korea',
                                                    'Tunisia', 'Saudi Arabia',
                                                    'The former Yugoslav Republic of Macedonia', 'Morocco', 'Yemen', 'Uganda',
                                                    'United Republic of Tanzania', 'Cuba', 'Ethiopia', 'Iceland', 'Oman',
                                                    'Ecuador', 'Other Country (Not Listed Above)', 'Jordan',
                                                    'Republic of Moldova', 'Honduras', 'Azerbaijan', 'Cyprus',
                                                    'Syrian Arab Republic', 'Nicaragua', 'Kazakhstan', 'Kuwait', 'Cameroon',
                                                    'Luxembourg', 'Albania', 'Bahrain', 'Zimbabwe', 'Guatemala', 'Mozambique',
                                                    'Bolivia', 'Mauritius', 'Montenegro', 'Sudan', 'Maldives', 'Turkmenistan',
                                                    'Panama', 'Lesotho,' 'Somalia', 'Qatar', 'Mongolia', 'Kyrgyzstan',
                                                    'Swaziland',
                                                    'Rwanda', 'Fiji', 'Marshall Islands', 'Iraq', 'Jamaica',
                                                    'Trinidad and Tobago',
                                                    'Libyan Arab Jamahiriya', 'Madagascar', 'Namibia', 'Tajikistan', 'Malawi',
                                                    'Bhutan', "Côte d'Ivoire", 'Andorra', 'Bahamas', 'Gambia', 'Sierra Leone',
                                                    'Togo', 'Zambia', 'Benin', 'Democratic Republic of the Congo',
                                                    'Suriname', 'Senegal', 'Liechtenstein',
                                                    'Barbados', 'Saint Lucia', 'Monaco', 'Guyana', 'Dominica', 'Eritrea',
                                                    'None',
                                                    'Iran', 'Brunei Darussalam', 'Gabon', 'Guinea', 'Angola', 'Timor-Leste',
                                                    'Djibouti', 'Burundi', 'Burkina Faso', 'Haiti',
                                                    'Saint Vincent and the Grenadines', 'San Marino',
                                                    "Lao People's Democratic Republic", 'Seychelles',
                                                    "Democratic People's Republic of Korea", 'Chad', 'Mali', 'Nomadic',
                                                    'Isle of Man', 'Kosovo', 'Niger'], key='2')
                            if (inp2 != "Select an option"):
                                lis.append(inp2)

                                st.subheader("Question 5")
                                st.write(questions[3])
                                inp3 = st.selectbox("", ['Select an option', 'British pounds sterling (£)', 'U.S. dollars ($)',
                                                        'South African rands (R)', 'Euros (€)', 'Swedish kroner (SEK)',
                                                        'Australian dollars (A$)', 'Indian rupees (₹)', 'Polish złoty (zł)',
                                                        'Russian rubles (₽)', 'Danish krone (kr)', 'Chinese yuan renminbi (¥)',
                                                        'Japanese yen (¥)', 'Brazilian reais (R$)', 'Canadian dollars (C$)',
                                                        'Mexican pesos (MXN$)', 'Norwegian krone (kr)', 'Swiss francs',
                                                        'Singapore dollars (S$)', 'Bitcoin (btc)'], key='3')
                                if (inp3 != "Select an option"):
                                    lis.append(inp3)

                                    st.subheader("Question 6")
                                    st.write(questions[4])
                                    inp4 = st.selectbox("",
                                                        ['Select an option', 'Developer', 'Manager', 'Non Developer', 'Student',
                                                        'Non developer'], key='4')
                                    if (inp4 != "Select an option"):
                                        lis.append(inp4)

                                        st.subheader("Question 7")
                                        st.write(questions[5])
                                        inp5 = st.selectbox("", ['Select an option', 'Bachelors', 'Associate', 'No Degree',
                                                                'Masters', 'Professional', 'Doctorate', 'None'], key='5')
                                        if (inp5 != "Select an option"):
                                            lis.append(inp5)

                                            st.subheader("Question 8")
                                            st.write(questions[6])
                                            inp6 = st.selectbox("", ['Select an option', 'White or European descent',
                                                                    'Black or African descent', 'South Asian',
                                                                    'Middle Eastern', 'Hispanic or Latino',
                                                                    'East Asian' 'Native American',
                                                                    'None', 'White or of European descent',
                                                                    'Black or of African descent',
                                                                    'Multiracial', 'Biracial', 'Indigenous',
                                                                    'Southeast Asian'], key='6')
                                            if (inp6 != "Select an option"):
                                                lis.append(inp6)

                                                st.subheader("Question 9")
                                                st.write(questions[7])
                                                inp7 = st.selectbox("", ['Select an option', 'Male', 'Non-binary', 'Female',
                                                                        'None'], key='7')
                                                if (inp7 != "Select an option"):
                                                    lis.append(inp7)

                                                    st.subheader("Question 10")
                                                    st.write(questions[8])
                                                    inp8 = st.selectbox("", ['Select an option', 'Yes', 'No', 'None'], key='8')
                                                    if (inp8 != "Select an option"):
                                                        lis.append(inp8)

                                                        st.subheader("Question 11")
                                                        st.write(questions[9])
                                                        inp9 = st.selectbox("", ['Select an option', 'Moderately dissatisfied',
                                                                                'Moderately satisfied',
                                                                                'Neither satisfied nor dissatisfied',
                                                                                'Slightly satisfied',
                                                                                'Extremely satisfied',
                                                                                'Slightly dissatisfied' 'Extremely dissatisfied',
                                                                                'None', 'Very satisfied', 'Very dissatisfied'],
                                                                            key='9')
                                                        if (inp9 != "Select an option"):
                                                            lis.append(inp9)

                                                            st.subheader("Question 12")
                                                            st.write(questions[10])
                                                            inp10 = st.selectbox("", ['Select an option',
                                                                                    'I am actively looking for a job',
                                                                                    'I’m not actively looking, but I am open to new opportunities',
                                                                                    'I am not interested in new job opportunities' 'None']
                                                                                ,
                                                                                key='10')
                                                            if (inp10 != "Select an option"):
                                                                lis.append(inp10)

                                                                st.subheader("Question 13")
                                                                st.write(questions[11])
                                                                inp11 = st.selectbox("",
                                                                                    ['Select an option', 'None', 'Not seeking',
                                                                                    'Seeking',
                                                                                    'I’m not actively looking, but I am open to new opportunities',
                                                                                    'I am actively looking for a job',
                                                                                    'I am not interested in new job opportunities']
                                                                                    ,
                                                                                    key='11')
                                                                if (inp11 != "Select an option"):
                                                                    lis.append(inp11)

                                                                    #                                                            st.subheader("Question 12")
                                                                    #                                                            st.write(questions[12])
                                                                    #                                                            inp12 = st.selectbox("",['Select an option','Go', 'C#', 'Assembly' ,'C' ,'Matlab', 'Erlang', 'Java', 'Python' ,'PHP',
                                                                    # 'JavaScript', 'C++' ,'SQL' ,'CoffeeScript' ,'Groovy' ,'Ruby', 'Haskell' ,'Swift',
                                                                    # 'Rust', 'Clojure' ,'Julia' ,'F#' ,'Bash/Shell' ,'TypeScript' ,'Objective-C' ,'R',
                                                                    # 'Kotlin', 'Perl' ,'Lua' ,'Scala' ,'Delphi/Object Pascal' ,'HTML' ,'Hack',
                                                                    # 'Ocaml' ,'VB.NET' ,'CSS' ,'VBA', 'Cobol', 'Visual Basic 6', 'None' ,'Elixir',
                                                                    # 'HTML/CSS' ,'Bash/Shell/PowerShell' ,'Dart', 'Other(s):', 'WebAssembly'],key='12')
                                                                    #                                                            if (inp12 != "Select an option"):
                                                                    #                                                                lis.append(inp12)

                                                                

                                                                    st.subheader("Question 14")
                                                                    st.write(questions[15])
                                                                    inp15 = st.selectbox("", ['Select an option',
                                                                                            'Linux-based',
                                                                                            'Windows', 'MacOS',
                                                                                            'BSD/Unix', 'None'],
                                                                                        key='15')
                                                                    if (inp15 != "Select an option"):
                                                                        lis.append(inp15)

                                                                        st.subheader("Question 15")
                                                                        st.write(questions[16])
                                                                        inp16 = st.selectbox("",
                                                                                            ['Select an option',
                                                                                            'None',
                                                                                            'Non developer',
                                                                                            'Developer',
                                                                                            'Novoice', 'Student',
                                                                                            'Ex-Developer']

                                                                                            ,
                                                                                            key='16')
                                                                        if (inp16 != "Select an option"):
                                                                            lis.append(inp16)
                                                                            
                                                                            
                                                                            
                                                                            st.subheader("Question 16")
                                                                            st.write(questions[17])
                                                                            inp17 = st.selectbox("",
                                                                                                [
                                                                                                    'Select an option' ,'Yearly', 'Monthly' ,'Weekly' ,'None']


                                                                                                ,
                                                                                                key='17')
                                                                            if (inp17 != "Select an option"):
                                                                                lis.append(inp17)

                                                                            # st.subheader("Question 17")
                                                                            # st.write(questions[17])
                                                                            # inp17 = st.selectbox("",
                                                                            #                      [
                                                                            #                          'Select an option',
                                                                            #                          'Yearly',
                                                                            #                          'Monthly',
                                                                            #                          'Weekly',
                                                                            #                          'None']
                                                                            #
                                                                            #                      ,
                                                                            #                      key='17')
                                                                            # if (inp17 != "Select an option"):
                                                                            #     lis.append(inp17)
                                                                            #
                                                                            #     st.subheader("Question 18")
                                                                            #     st.write(questions[18])
                                                                            #     inp18 = st.text_input("", key='18')
                                                                            #     if ((inp18 != "")):
                                                                            #         lis.append(int(inp18))

                                                                                st.subheader("Question 17")
                                                                                st.write(questions[19])
                                                                                inp19 = st.selectbox("",
                                                                                                    [
                                                                                                        'Select an option',
                                                                                                        'Other Science',
                                                                                                        'Computer Science',
                                                                                                        'Arts and Science',
                                                                                                        'Engineering',
                                                                                                        'No major',
                                                                                                        'Business',
                                                                                                        'Info Systems',
                                                                                                        'Web Design/Dev',
                                                                                                        'Math/Stat',
                                                                                                        'None',
                                                                                                        'No Major']

                                                                                                    ,
                                                                                                    key='19')
                                                                                if (
                                                                                        inp19 != "Select an option"):
                                                                                    lis.append(inp19)

                                                                                    

                                                                                

                                                                                    st.subheader(
                                                                                        "Question 18")
                                                                                    st.write(
                                                                                        questions[20])
                                                                                    inp22 = st.selectbox(
                                                                                        "", [
                                                                                            'Select an option',
                                                                                            'None' 'Average',
                                                                                            'A little below average',
                                                                                            'A little above average',
                                                                                            'Far above average',
                                                                                            'Far below average']
                                                                                        ,
                                                                                        key='22')
                                                                                    if (
                                                                                            inp22 != "Select an option"):
                                                                                        lis.append(
                                                                                            inp22)
                                                                                        
                                                                                        
                                                                                        
                                                                                        st.subheader(
                                                                                            "Question 19")
                                                                                        st.write(
                                                                                            questions[
                                                                                                23])
                                                                                        inp23 = st.selectbox(
                                                                                            "", [
                                                                                                'Select an option',
                                                                                                'Full-time',
                                                                                                'Part-time',
                                                                                                'Self-employed',
                                                                                                'None',
                                                                                                'Not employed',
                                                                                                'Student',
                                                                                                'Not employed, and not looking for work',
                                                                                                'Retired'],
                                                                                            key='23')
                                                                                        if (
                                                                                                inp23 != "Select an option"):
                                                                                            lis.append(
                                                                                                inp23)

                                                                                            st.subheader(
                                                                                                "Question 20")
                                                                                            st.write(
                                                                                                questions[
                                                                                                    24])
                                                                                            inp24 = st.selectbox(
                                                                                                "", [
                                                                                                    'Select an option','Go', 'C#', 'Assembly', 'C', 'Matlab', 'Erlang', 'Java', 'Python', 'PHP',
'JavaScript', 'C++', 'SQL', 'CoffeeScript', 'Groovy', 'Ruby', 'Haskell', 'Swift',
'Rust', 'Clojure', 'Julia', 'F#', 'Bash/Shell', 'TypeScript', 'Objective-C', 'R',
'Kotlin', 'Perl', 'Lua', 'Scala', 'Delphi/Object Pascal', 'HTML', 'Hack',
'Ocaml', 'VB.NET', 'CSS', 'VBA', 'Cobol', 'Visual Basic 6', 'None', 'Elixir',
'HTML/CSS', 'Bash/Shell/PowerShell', 'Dart', 'Other(s):', 'WebAssembly'
]
                                                                                                ,
                                                                                                key='24')
                                                                                            if (
                                                                                                    inp24 != "Select an option"):
                                                                                                lis.append(
                                                                                                    inp24)

                                                                                                st.subheader(
                                                                                                    "Question 21")
                                                                                                st.write(
                                                                                                    questions[
                                                                                                        25])
                                                                                                inp25 = st.selectbox(
                                                                                                    "",
                                                                                                    [
                                                                                                        'Select an option','Go', 'C#', 'Assembly', 'C', 'Matlab', 'Erlang', 'Java', 'Python', 'PHP',
'JavaScript', 'C++', 'SQL', 'CoffeeScript', 'Groovy', 'Ruby', 'Haskell', 'Swift',
'Rust', 'Clojure', 'Julia', 'F#', 'Bash/Shell', 'TypeScript', 'Objective-C', 'R',
'Kotlin', 'Perl', 'Lua', 'Scala', 'Delphi/Object Pascal', 'HTML', 'Hack',
'Ocaml', 'VB.NET', 'CSS', 'VBA', 'Cobol', 'Visual Basic 6', 'None', 'Elixir',
'HTML/CSS', 'Bash/Shell/PowerShell', 'Dart', 'Other(s):', 'WebAssembly'
]
                                                                                                    ,
                                                                                                    key='25')
                                                                                                if (
                                                                                                        inp25 != "Select an option"):
                                                                                                    lis.append(
                                                                                                        inp25)

                                                                                                    st.subheader(
                                                                                                        "Question 22")
                                                                                                    st.write(
                                                                                                        questions[
                                                                                                            26])
                                                                                                    inp26 = st.selectbox(
                                                                                                        "",
                                                                                                        [
                                                                                                            'Select an option','Go', 'C#', 'Assembly', 'C', 'Matlab', 'Erlang', 'Java', 'Python', 'PHP',
'JavaScript', 'C++', 'SQL', 'CoffeeScript', 'Groovy', 'Ruby', 'Haskell', 'Swift',
'Rust', 'Clojure', 'Julia', 'F#', 'Bash/Shell', 'TypeScript', 'Objective-C', 'R',
'Kotlin', 'Perl', 'Lua', 'Scala', 'Delphi/Object Pascal', 'HTML', 'Hack',
'Ocaml', 'VB.NET', 'CSS', 'VBA', 'Cobol', 'Visual Basic 6', 'None', 'Elixir',
'HTML/CSS', 'Bash/Shell/PowerShell', 'Dart', 'Other(s):', 'WebAssembly'
]
                                                                                                        ,
                                                                                                        key='26')
                                                                                                    if (
                                                                                                            inp26 != "Select an option"):
                                                                                                        lis.append(
                                                                                                            inp26)
                                                                                                        
                                                                                                        
                                                                                                        
                                                                                                        st.subheader("Question 23")
                                                                                                        st.write(questions[12])
                                                                                                        inp12 = st.selectbox("", ['Select an option', 'JavaScript',
                                                                                                                                'C#', 'C', 'Java', 'Assembly',
                                                                                                                                'Python', 'C++', 'PHP', 'SQL',
                                                                                                                                'Erlang', 'Go', 'Ruby', 'Perl',
                                                                                                                                'Objective-C', 'Swift',
                                                                                                                                'CoffeeScript', 'Groovy',
                                                                                                                                'Hack', 'F#', 'Haskell',
                                                                                                                                'Clojure', 'R', 'Ocaml',
                                                                                                                                'Delphi/Object Pascal', 'VBA',
                                                                                                                                'Lua', 'Bash/Shell', 'VB.NET',
                                                                                                                                'Scala', 'Matlab', 'Julia',
                                                                                                                                'HTML', 'Rust',
                                                                                                                                'Kotlin', 'TypeScript', 'Cobol',
                                                                                                                                'Visual Basic 6', 'CSS', 'None',
                                                                                                                                'HTML/CSS',
                                                                                                                                'Bash/Shell/PowerShell', 'Elixir',
                                                                                                                                'Dart', 'Other(s):',
                                                                                                                                'WebAssembly'],

                                                                                                                            key='12')
                                                                                                        if (inp12 != "Select an option"):
                                                                                                            lis.append(inp12)

                                                                                                            st.subheader("Question 24")
                                                                                                            st.write(questions[13])
                                                                                                            inp13 = st.selectbox("",
                                                                                                                                ['Select an option', 'None',
                                                                                                                                'Python', 'JavaScript', 'C++',
                                                                                                                                'HTML', 'TypeScript',
                                                                                                                                'CoffeeScript',
                                                                                                                                'SQL', 'PHP', 'Java', 'F#', 'C',
                                                                                                                                'Go', 'Bash/Shell', 'Julia', 'R',
                                                                                                                                'Ruby', 'C#',
                                                                                                                                'Swift', 'Clojure', 'Haskell',
                                                                                                                                'Perl', 'Objective-C', 'Kotlin',
                                                                                                                                'Groovy', 'Lua',
                                                                                                                                'VBA', 'Erlang', 'Scala',
                                                                                                                                'Matlab', 'Delphi/Object Pascal',
                                                                                                                                'Visual Basic 6',
                                                                                                                                'Cobol', 'Rust', 'Hack', 'VB.NET',
                                                                                                                                'CSS', 'Ocaml', 'HTML/CSS',
                                                                                                                                'Bash/Shell/PowerShell',
                                                                                                                                'Other(s):', 'Dart', 'Elixir',
                                                                                                                                'WebAssembly']
                                                                                                                                ,

                                                                                                                                key='13')
                                                                                                            if (inp13 != "Select an option"):
                                                                                                                lis.append(inp13)

                                                                                                                st.subheader("Question 25")
                                                                                                                st.write(questions[14])
                                                                                                                inp14 = st.selectbox("", ['Select an option',
                                                                                                                                        'Bash/Shell', 'SQL',
                                                                                                                                        'Java', 'Python', 'CSS',
                                                                                                                                        'HTML', 'Erlang', 'None',
                                                                                                                                        'PHP',
                                                                                                                                        'C#', 'Go', 'JavaScript',
                                                                                                                                        'Objective-C', 'C++',
                                                                                                                                        'Groovy', 'Haskell',
                                                                                                                                        'TypeScript', 'Swift',
                                                                                                                                        'Hack', 'Scala', 'R',
                                                                                                                                        'Rust', 'Perl', 'Lua',
                                                                                                                                        'CoffeeScript', 'Matlab',
                                                                                                                                        'Ruby', 'Julia', 'VBA',
                                                                                                                                        'F#', 'Visual Basic 6',
                                                                                                                                        'VB.NET', 'Kotlin',
                                                                                                                                        'Delphi/Object Pascal',
                                                                                                                                        'Clojure', 'Cobol',
                                                                                                                                        'Ocaml',
                                                                                                                                        'HTML/CSS', 'C',
                                                                                                                                        'Other(s):', 'Dart',
                                                                                                                                        'Elixir', 'WebAssembly'],
                                                                                                                                    key='14')
                                                                                                                if (inp14 != "Select an option"):
                                                                                                                    lis.append(inp14)
                                                                                                        


                                                                                                                    # ALL ENTRIES BY USER ARE DONE
                                                                                                                    print(lis)

                                                                                                                    st.success(
                                                                                                                        "Test Completed")
                                                                                                                    st.title(
                                                                                                                        "RESULTS:")
                                                                                                                    result2 = output2(lis)+1
                                                                                                                    print(result2)
                                                                                                                    st.subheader("Expected Salary according to the details provided")
                                                                                                                    st.subheader(dataset1['SalaryUSD'][result2[0]+1])
                                                                                                                


def output(answers):
    #-----------------------------Processing user Inpute----------------#
    #---------------Applying OneHot & Lable  Encoding-----------#
    from sklearn.preprocessing import LabelEncoder, OneHotEncoder
    labelencoder = LabelEncoder()

    #---------------conversion of all categorial column values to vector/numerical--------#
    for i in range(4,len(answers)-1):
        answers[i:] = labelencoder.fit_transform(answers[i:])

    #--------------normalizing the non-categorial column values---------#
    from sklearn.preprocessing import Normalizer
    answers1 = answers[:4]
    # print(answers1) 
    answers1_2d = np.reshape(answers1, (1, -1))
    # print(answers1_2d)
    normalized_data = Normalizer().fit_transform(answers1_2d)
    # print(normalized_data)

    answers2 = answers[4:]
    answers2_2d = np.reshape(answers2, (1, -1))
    # print(answers2_2d.shape)
    dff1 = np.append(normalized_data,answers2_2d,axis=1)
    # dff1.shape

    data = dataset.iloc[:,:-1].values
    label = dataset.iloc[:,-1].values

    #------------------Encoding Final Output column Values------------#
    label = labelencoder.fit_transform(label)
    # print(len(label))
    y=pd.DataFrame(label,columns=['LanguageDesireNextYear1'])

    # -----------Manually loading--------------#
    # load the model from disk
    import pickle
    svc_clf = pickle.load(open('newmodels/model.h5', 'rb'))
    #--------doing prediction-----#
    svm_y_pred = svc_clf.predict(dff1)   
    print(svm_y_pred)

    decoded_labels = labelencoder.inverse_transform(svm_y_pred)
    print(decoded_labels)
    return decoded_labels


def output2(answers):
    #-----------------------------Processing user Inpute----------------#
    #---------------Applying OneHot & Lable  Encoding-----------#
    from sklearn.preprocessing import LabelEncoder, OneHotEncoder
    labelencoder = LabelEncoder()

    #---------------conversion of all categorial column values to vector/numerical--------#
    for i in range(3,len(answers)-1):
        answers[i:] = labelencoder.fit_transform(answers[i:])

    #--------------normalizing the non-categorial column values---------#
    from sklearn.preprocessing import Normalizer
    answers1 = answers[:3]
    # print(answers1) 
    answers1_2d = np.reshape(answers1, (1, -1))
    # print(answers1_2d)
    normalized_data = Normalizer().fit_transform(answers1_2d)
    # print(normalized_data)

    answers2 = answers[3:]
    answers2_2d = np.reshape(answers2, (1, -1))
    # print(answers2_2d.shape)
    dff1 = np.append(normalized_data,answers2_2d,axis=1)

    data = dataset1.iloc[:,:-1].values
    #label = dataset1.iloc[:,-1].values

    #------------------Encoding Final Output column Values------------#
    #label = labelencoder.fit_transform(label)
    # print(len(label))
    y=dataset1["SalaryUSD"]

    # -----------Manually loading--------------#
    # load the model from disk
    import pickle
    svc_clf = pickle.load(open('newmodels/model2_salary.h5', 'rb'))
    #--------doing prediction-----#
    svm_y_pred = svc_clf.predict(dff1)   
    print(svm_y_pred)

    #decoded_labels = labelencoder.inverse_transform(svm_y_pred)
    print("salary=",dataset1['SalaryUSD'][svm_y_pred[0]+1])
    return svm_y_pred



def botans(query):
    # basic conversation
    for key, value in ANS_QUES_MAP.items():
        if query in value:
            return key

def speak(audio):
    """
    Speaks a sentence.
    Param - audio (string)
    """
    if engine._inLoop:
        engine.endLoop()
    engine.say(audio)
    engine.runAndWait()
    # t3 = threading.Thread(target=engine.runAndWait)
    # t3.start()

def get_text():
    x = st.text_input("You : ")
    x=x.lower()
    return x

def main():
    st.set_page_config(page_title="Recommendation_System", page_icon="📊")

    st.markdown("# Recommendation System ")
    st.sidebar.header("Recommendation System")

    st.write(
    """Please Select whichever Recommendation  you want to see from the given option"""
    )
    
    # Add navigation to subpages
    subpage_selection = st.radio("Select a Anaylsis:", ["Language Recommendation", "Salary Recommendation"])

    if subpage_selection == "Language Recommendation":
        ana_one()
    elif subpage_selection == "Salary Recommendation":
        ll = [20, 2, 2, 'India', 'Swedish kroner (SEK)', 'Non Developer', 'Masters', 'Hispanic or Latino', 'Male', 'No', 'Extremely satisfied', 'I’m not actively looking, but I am open to new opportunities', 'I am actively looking for a job', 'MacOS', 'Novoice', 'Monthly', 'Engineering', 'A little above average', 'None', 'C', 'Assembly', 'C', 'Java', 'C++', 'HTML']
        output2(ll)
        ana_two()
        
if __name__ == "__main__":
    main()