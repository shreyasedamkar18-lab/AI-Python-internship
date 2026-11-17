
import streamlit as st
import re

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="📚",
    layout="wide"
)

st.title("📚 AI Study Assistant")
st.write("Your personal study assistant.")

option = st.selectbox(
    "Select a feature:",
    [
        "Explain a Topic",
        "Summarize Notes",
        "Generate Quiz Questions"
    ]
)

if option == "Explain a Topic":
    st.header("📖 Explain a Topic")

    topic = st.text_input("Enter a topic:")

    level = st.selectbox(
        "Choose your learning level:",
        ["Beginner", "Intermediate", "Advanced"]
    )

    
if st.button("Explain Topic"):
    if topic.strip():

        explanations = {
            "artificial intelligence":
                "Artificial Intelligence (AI) is a technology "
                "that enables computers to perform tasks that "
                "normally require human intelligence.",

            "machine learning":
                "Machine Learning is a branch of AI that allows "
                "computers to learn patterns from data and improve "
                "their performance without being explicitly "
                "programmed for every task.",

            "python":
                "Python is a popular programming language known "
                "for its simple syntax. It is used in web development, "
                "data analysis, automation, and artificial intelligence."
        }

        explanation = explanations.get(topic.strip().lower())

        st.subheader("Your Topic Explanation")
        st.write(f"**Learning Level:** {level}")

        if explanation:
            st.success(explanation)
        else:
            st.info(
                "No prepared explanation is available for this topic. "
                "Try Artificial Intelligence, Machine Learning, or Python."
            )

    else:
        st.warning("Please enter a topic.")



elif option == "Summarize Notes":
    st.header("📝 Summarize Your Notes")

    notes = st.text_area(
        "Paste your study notes here:",
        height=200
    )

    if st.button("Summarize Notes"):
        if notes.strip():
            sentences = re.split(r'(?<=[.!?])\s+', notes.strip())

            words = re.findall(r'\b[a-zA-Z]{3,}\b', notes.lower())

            stop_words = {
                "the", "and", "for", "are", "was", "were",
                "this", "that", "with", "from", "have", "has"
            }

            keywords = [
                word for word in words
                if word not in stop_words
            ]

            from collections import Counter

            word_frequency = Counter(keywords)

            def sentence_score(sentence):
                sentence_words = re.findall(
                    r'\b[a-zA-Z]{3,}\b',
                    sentence.lower()
                )
                return sum(word_frequency[word] for word in sentence_words)

            ranked_sentences = sorted(
                sentences,
                key=sentence_score,
                reverse=True
            )

            summary = " ".join(ranked_sentences[:3])

            st.subheader("Your Summary:")
            st.write(summary)
        else:
            st.warning("Please enter your notes.")



elif option == "Generate Quiz Questions":
    st.header("❓ Generate Quiz Questions")

    topic = st.text_input("Enter a quiz topic:")

    if st.button("Generate Quiz"):
        if topic.strip():
            st.subheader("Practice Questions")

            questions = [
                f"What is {topic}?",
                f"Explain the importance of {topic}.",
                f"Give an example of {topic}."
            ]

            for i, question in enumerate(questions, 1):
                st.write(f"{i}. {question}")
        else:
            st.warning("Please enter a topic.")
