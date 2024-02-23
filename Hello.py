import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="NextBot - Your IT Companion",
    page_icon="👋",
)

# Larger and bold text using Markdown
st.title("Welcome to NextBot! 👋")

# Stylish sidebar
st.sidebar.success("Select what you want to do.")

# Center-align and make the specified line the size of the title
st.markdown(
    """
    <div style="text-align: center; font-size: 2em; margin-bottom: 20px; color: #3498db;">

    **Select a demo from the sidebar** to see some Analysis or if you want to get a Recommendation.

    </div>
    """,
    unsafe_allow_html=True
)

# Introduction section with improved styling
st.markdown(
    """
    <div style="font-size: 1.2em; line-height: 1.6; text-align: justify;">

    The **NextBot** is a personalized recommendation system tailored to IT professionals and students. 

    In the fast-paced world of technology, staying updated with relevant skills, tools, and resources is challenging. 
    This recommendation system aims to solve this problem by providing curated suggestions for programming languages, salary, and job satisfaction, helping users make informed decisions about their professional growth.

    We also have some analysis of the Stack Overflow Developer Survey for the years 2020, 2021, and 2022. 
    From proper analysis, we would answer real-world questions. For instance, we can find the most popular language that developers use. 
    We can also find the developer role that pays the highest salary.

    - **Made By:** Group 60
      - Ujjwal Godara
      - Rahul Kumar
      - Sourabh Sejwal
      - Anupam Narayan

    **IIA Course**
    **Instructor:** Mukesh Mohania

    </div>
    """,
    unsafe_allow_html=True
)

# Add some padding and background color to the footer
st.markdown(
    """
    <div style="background-color: #f2f2f2; padding: 10px; border-radius: 10px; margin-top: 20px; text-align: center; font-size: 0.9em; color: #666;">

    Explore the world of IT with NextBot! 🚀

    </div>
    """,
    unsafe_allow_html=True
)
