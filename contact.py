import streamlit as st


# Function to load local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Load the CSS before any other content


# Rest of your code
def contact():
    with st.container():
        st.write("---")
        st.header("Get In Touch With Me!")
        st.write("##")

        # Documentation: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
        <form action="https://formsubmit.co/bangadegaurav@gmail.com" method="POST">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
    """

    # Create a two-column layout
    left_column, right_column = st.columns(2)

    # Display the HTML form in the left column
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
        local_css("form.css")
    # Keep the right column empty
    with right_column:
        st.empty()


if __name__ == "__main__":
    contact()
