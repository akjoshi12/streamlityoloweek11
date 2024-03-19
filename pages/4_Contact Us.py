import streamlit as st

st.header("📬 Contact Us")
st.write("We'd love to hear from you! Whether you have a question, feedback, or just want to say hello, please don't hesitate to reach out. Fill out the form below or email us directly at contact-thirdeye@gmail.com.")
    
with st.form("contact_form"):
    name = st.text_input("Name", placeholder="Your Name")
    email = st.text_input("Email", placeholder="Your Email Address")
    message = st.text_area("Message", placeholder="Your Message Here")
        
    submit_button = st.form_submit_button("Send Message")
        
    if submit_button:
        # Here you would include the logic to handle the form data, such as sending an email
        # This is a placeholder to simulate form submission
        st.success(f"Thank you, {name}, for reaching out! We'll get back to you soon.")
