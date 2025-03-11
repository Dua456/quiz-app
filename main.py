import streamlit as st  # for the web interface
import random  # for randomizing the questions
import time  # for the timer

# Set page configuration
st.set_page_config(page_title="Quiz Application", page_icon="📝", layout="centered")

# Apply custom styling
st.markdown(
    """
    <style>
        .stApp {
            background-color: black;
            color: white;
            font-family: Arial, sans-serif;
        }
        .stTitle {
            text-align: center;
            color: #4A90E2;
        }
        .stButton>button {
            background-color: #4A90E2;
            color: white;
            border-radius: 10px;
            font-size: 18px;
            padding: 10px;
            width: 50%;
            margin: auto;
            display: block;
        }
        .stRadio label,.stRadio div {
            font-size: 18px;
            color: white ;
        }
        .stSuccess {
            background-color: #28a745;
            color: white;
            padding: 10px;
            text-align: center;
            border-radius: 5px;
        }
        .stError {
            background-color: #dc3545;
            color: white;
            padding: 10px;
            text-align: center;
            border-radius: 5px;
        }
        .quiz-completed {
            color: #FFD700;
            text-align: center;
            font-size: 22px;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title of the Application
st.markdown("<h1 class='stTitle'>📝 Quiz Application</h1>", unsafe_allow_html=True)

# Define quiz questions, options, and answers
questions = [
    {"question": "What is the capital of Pakistan?", "options": ["Lahore", "Karachi", "Islamabad", "Peshawar"], "answer": "Islamabad"},
    {"question": "Who is the founder of Pakistan?", "options": ["Allama Iqbal", "Liaquat Ali Khan", "Muhammad Ali Jinnah", "Benazir Bhutto"], "answer": "Muhammad Ali Jinnah"},
    {"question": "Which is the national language of Pakistan?", "options": ["Punjabi", "Urdu", "Sindhi", "Pashto"], "answer": "Urdu"},
    {"question": "What is the currency of Pakistan?", "options": ["Rupee", "Dollar", "Taka", "Riyal"], "answer": "Rupee"},
    {"question": "Which city is known as the City of Lights in Pakistan?", "options": ["Lahore", "Islamabad", "Faisalabad", "Karachi"], "answer": "Karachi"},
    {"question": "Which is the largest province of Pakistan by area?", "options": ["Punjab", "Sindh", "Balochistan", "KPK"], "answer": "Balochistan"},
    {"question": "Which sea borders Pakistan?", "options": ["Red Sea", "Caspian Sea", "Arabian Sea", "Mediterranean Sea"], "answer": "Arabian Sea"},
    {"question": "Who wrote the national anthem of Pakistan?", "options": ["Faiz Ahmed Faiz", "Allama Iqbal", "Hafeez Jalandhari", "Ahmed Faraz"], "answer": "Hafeez Jalandhari"},
    {"question": "Which year did Pakistan become independent?", "options": ["1945", "1947", "1950", "1952"], "answer": "1947"},
    {"question": "Which is the national flower of Pakistan?", "options": ["Rose", "Jasmine", "Sunflower", "Tulip"], "answer": "Jasmine"},
    {"question": "Which is the highest mountain in Pakistan?", "options": ["K2", "Nanga Parbat", "Mount Everest", "Rakaposhi"], "answer": "K2"},
    {"question": "Who was the first Prime Minister of Pakistan?", "options": ["Liaquat Ali Khan", "Zulfikar Ali Bhutto", "Benazir Bhutto", "Pervez Musharraf"], "answer": "Liaquat Ali Khan"},
    {"question": "What is the national animal of Pakistan?", "options": ["Tiger", "Lion", "Markhor", "Elephant"], "answer": "Markhor"},
    {"question": "Which is the longest river in Pakistan?", "options": ["Chenab", "Jhelum", "Indus", "Ravi"], "answer": "Indus"},
    {"question": "What is the name of the parliament of Pakistan?", "options": ["Senate", "National Assembly", "Majlis-e-Shura", "House of Lords"], "answer": "Majlis-e-Shura"}
]

# Initialize session state
if "current_index" not in st.session_state:
    st.session_state.current_index = 0
    st.session_state.correct_answers = 0
    random.shuffle(questions)

# Check if quiz is finished
if st.session_state.current_index < len(questions):
    question = questions[st.session_state.current_index]
    st.subheader(f"Question {st.session_state.current_index + 1}: {question['question']}")
    selected_option = st.radio("Choose your answer", question["options"], key=f"answer_{st.session_state.current_index}")
    
    if st.button("Submit Answer"):
        if selected_option == question["answer"]:
            st.markdown(
                f"<div class='stSuccess'>✅ Correct! Well done! 🎉 {question['answer']} is the correct answer.</div>",
                unsafe_allow_html=True,
            )
            st.session_state.correct_answers += 1
        else:
            st.markdown(
                f"<div class='stError'>❌ Incorrect! The correct answer is {question['answer']}.</div>",
                unsafe_allow_html=True,
            )
        
        st.session_state.current_index += 1
        time.sleep(2)
        st.rerun()
else:
    st.markdown(
        f"<div class='quiz-completed'>🎉 Quiz Completed! You answered {st.session_state.correct_answers} out of {len(questions)} questions correctly! 🎯</div>",
        unsafe_allow_html=True,
    )
