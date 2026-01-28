import streamlit as st

# Page config
st.set_page_config(page_title="My Portfolio", page_icon="🌟")

# Sidebar
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["Home", "About", "Projects", "Contact"])

st.sidebar.markdown("### 🌐 Connect with me")
st.sidebar.markdown("[GitHub](https://github.com/yourusername)")
st.sidebar.markdown("[LinkedIn](https://linkedin.com/in/yourusername)")

# Home
if menu == "Home":
    st.title("Technologyyyyaaaa!!")
    st.subheader("Aspiring Full Stack Developer")
    st.write("Welcome to my Streamlit portfolio!")

# About
elif menu == "About":
    st.header("📌 About Me")
    st.write("""
    - Beginner Full Stack Developer  
    - Learning Python, C, Streamlit  
    - Interested in Web & App Development  
    """)
    st.subheader("⚡ Skills")
    st.progress(70)  # Python
    st.progress(50)  # C
    st.progress(40)  # Streamlit

# Projects
elif menu == "Projects":
    st.header("🛠 Projects")
    with st.expander("🔹 Student Feedback System"):
        st.write("A web app to collect and analyze student feedback.")
    with st.expander("🔹 Travel Content App"):
        st.write("An app to share travel blogs and photos.")
    with st.expander("🔹 GitHub Portfolio Website"):
        st.write("A personal portfolio hosted on GitHub Pages.")

# Contact
elif menu == "Contact":
    st.header("📞 Contact Me")
    email = st.text_input("Enter your email")
    msg = st.text_area("Your message")

    if st.button("Send"):
        if email and msg:
            st.success("Message sent successfully ✅")
        else:
            st.error("Please fill in all fields ❌")