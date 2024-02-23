import streamlit as st
import time
import numpy as np


# def ana_0():
    # st.title("Select")
    # st.image("img\men_women_income.png")
    # st.write("There is a little bit of difference between Gender and income they received respectively. Men tend to receive more salary than women from the above analysis.")


# def ana_one():
#     st.title("To find whether there is any difference between men and women's income from latest stack overflow survey")
#     time.sleep(3)
#     st.image("img\men_women_income.png")
#     st.write("There is a little bit of difference between Gender and income they received respectively. Men tend to receive more salary than women from the above analysis.")

def ana_two():
    st.title("Ethnicity")
    time.sleep(3)
    st.image("img\ethinicity_participation.png")
    st.image("img\ethnicity_2.png")
    st.write("Consistent with the data from all three year, we still see evidence that people of color are underrepresented among professional developers. About 63% of the respondents were of White or european descend")

def ana_3():
    st.title("Distribution of respondents based on country ")
    time.sleep(3)
    st.image("img\geographical.png")
    st.write("We have used Plotly to create choropleth map to show the distribution of respondents across countries.")

def ana_4():
    st.title("Salary distribution among top ten countries")
    time.sleep(3)
    st.image("img\download.png")
    st.write("Overall, the country which has the highest mean annual salary is the United States of America(240,000) Dollars. The second highest country which provides the highest mean salary is Australia(164,926) Dollars. Though India has a higher number of respondents, it has the lowest mean salary of $25,213.We can understand that the mean salary of a developed country is much higher than that of a developing country.")

def ana_5():
    st.title("Impact of education level on salary")
    time.sleep(3)
    st.image("img\impact_of_education_level_on_salary.png")
    st.write("As we can see, the respondents who have done Doctorate have the highest mean salary among all other education levels. Secondly, the respondents who have done Bachelors degree have more salary than that of Masters degree holders. This may be due to years of professional coding experience and due to the higher number of respondents in that category than that of Masters degree(No of respondents in Bachelor degree is 35659 and number of respondents in masters degree is 16940) The most interesting is that the respondents who do not have any degree have a mean salary of $90k. This shows the improvement in online learning and advancement of technology that is shifting the company from relying on University degrees.")
def ana_6():
    st.title("Distribution of respondents based on age")
    time.sleep(3)
    st.image(r"img\respondant.png")
    st.write("About 70% of the developers are under 35 years of age. Only 5% of the respondents were about 50 years of age.")

# def ana_7():
#     st.title("Impact on the increase in popularity of a language in the current-year due to developer’s interest in the previous year.")
#     time.sleep(3)
#     st.image("img\programming_language_worked_respondant.jpg")
#     st.write("The most language that worked in 2021 and 2022 is JavaScript.In 2021, people worked slightly in javascript compare to 2021. The 2nd highest working language is HTML/CSS. For HTML/CSS the percentage is slightly low in 2022. There are some language people worked in only one year. Elixir, Clojure, F#, Web assembly are those languages that people used in 2021. Respondent started to use Perl, Haskell, Julia in 2022 on a small scale.")
# def ana_8():
#     st.title("Programming language desired to work")
#     time.sleep(3)
#     st.image("img\programming_language_desire_to_work.jpg")
#     st.write("In 2021, respondents said that they wanted to work in javascript is around more than 10 % and the fewer respond have a desire to work on VBA next year. People started to work in Haskell, Julia, and pearl in 2021 though the amount was less around 5% of people have the desire to work in those languages in 2022. Here, phyton is the 2nd one in which people have the desire to work in both 2021 and 2022.")
def ana_9():
    st.title("Distribution of surveyors based on their developer role.")
    time.sleep(3)
    st.image("img\developer_types_percentage.jpg")
    st.write("Most of the respondents were either back-end or full-stack developers. For those who are working as marketing and sales professionals, their percentage is lowest compare to others.")
# def ana_10():
#     st.title("")
#     time.sleep(3)
#     st.image("img\education_impact.png")
#     st.image("img\edlevel.png")
#     st.image("img\dependents.png")
#     st.write("After exploring the 2021 dataset, we have found that we cannot answer this question since male and female observations are significantly unbalanced.")

def ana_11():
    st.title("Gender Distribution")
    time.sleep(3)
    st.image("img\gender_distribution.jpg")
    st.write("We have plotted the gender distribution of Male and females in the top five counties. It is evident that the number of female respondents is lower in  both developed and developing countries.")

def ana_12():
    st.title("Where are the most data scientist come from in 2021?")
    time.sleep(3)
    st.image("img\countries_data_scientist.jpg")
    st.write("There are 5,788 data scientists who responded to the Stackoverflow survey in 2021. Most data scientists are from the US with 1,550 people and it is 3 times higher than data scientists from India. Followed by Germany and the UK with 427 and 339 people respectively. The rest are Canada, France, Netherlands, Brazil, Russia, and Australia which have less than 200 data scientists.")

def ana_13():
    st.title("Which countries pay the most to Data Scientists in 2021?")
    time.sleep(3)
    st.image("img\highest_datascientist.jpg")
    st.write("In 2021, the top three countries which have a highest mean annual salary of a data scientist are Ireland (275,851), Luxembourg (272,769), and the USA (265,211). Apart from that, the mean salary of the rest of the countries is less than (200,000) per year. Japan provides the highest mean annual salary among Asian countries (118,969)Figures in Dollars $")

def ana_14():
    st.title("Most popular languages")
    time.sleep(3)
    st.image("img\programming_language_respondant.jpg")
    st.write("The most language the developers use between 2020 to 2022 is JavaScript(14%). The second and third highest working language is HTML/CSS(13%) and SQL(11%). JavaScript and SQL had the same steady increasing trend over the three years. The percentage of HTML/CSS was slightly increased from 2020 to 2021. However, it dropped to the same level as 2020 in 2022. Python was responsible for about 9% in 2020. After then, it decreased to 8% in 2021 and it rose 1% in 2022.")

def main():
    st.set_page_config(page_title="Analysis", page_icon="📈")
    # Custom CSS for enhanced styling
    # st.markdown("""
    #     <style>
    #         body {
    #             background-color: #f7f7f7;
    #             font-family: 'Arial', sans-serif;
    #             color: #333;
    #         }

    #         .stApp {
    #             max-width: 1200px;
    #             margin: 0 auto;
    #         }

    #         .sidebar .sidebar-content {
    #             background-color: #2c3e50;
    #             color: #fff;
    #             padding: 20px;
    #             box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    #             border-radius: 10px;
    #         }

    #         .sidebar .stButton {
    #             background-color: #3498db;
    #             color: #fff;
    #             padding: 10px;
    #             border-radius: 5px;
    #             cursor: pointer;
    #             box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    #         }

    #         .stSelectbox {
    #             width: 100%;
    #             padding: 10px;
    #             border: 1px solid #ddd;
    #             border-radius: 5px;
    #             background-color: #fff;
    #             color: #333;
    #             box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    #         }

    #         .stSelectbox:hover {
    #             border-color: #3498db;
    #         }
    #     </style>
    # """, unsafe_allow_html=True)


    st.markdown("# Analysis")
    st.sidebar.header("Analysis")

    st.write(
        """Please Select whichever analysis you want to see from the given option"""
    )

    # Add navigation to subpages with dropdown
    subpage_selection = st.selectbox("Select an Analysis:", ["Select", "Ethnicity", "Distribution of respondents based on country ", "Salary distribution among top ten countries", "Impact of education level on salary",
                        "Distribution of respondents based on age","Distribution of surveyors based on their developer role.","Gender Distribution",
                        "Where are the most data scientist come from in 2021?","Which countries pay the most to Data Scientists in 2021?","Most popular languages"])

    # if subpage_selection == "Select":
    #     ana_0()    
    if subpage_selection == "To find whether there is any difference between men and women's income from latest stack overflow survey":
        ana_one()
    elif subpage_selection == "Ethnicity":
        ana_two()
    elif subpage_selection == "Distribution of respondents based on country ":
        ana_3()
    elif subpage_selection == "Salary distribution among top ten countries":
        ana_4()
    elif subpage_selection == "Impact of education level on salary":
        ana_5()
    elif subpage_selection == "Distribution of respondents based on age":
        ana_6()
    # elif subpage_selection == "Impact on the increase in popularity of a language in the current-year due to developer’s interest in the previous year.":
    #     ana_7()
    # elif subpage_selection == "Programming language desired to work":
    #     ana_8()
    elif subpage_selection == "Distribution of surveyors based on their developer role.":
        ana_9()
    # elif subpage_selection == "":
    #     ana_10()
    elif subpage_selection == "Gender Distribution":
        ana_11()
    elif subpage_selection == "Where are the most data scientist come from in 2021?":
        ana_12()
    elif subpage_selection == "Which countries pay the most to Data Scientists in 2021?":
        ana_13()
    elif subpage_selection == "Most popular languages":
        ana_14()

if __name__ == "__main__":
    main()
