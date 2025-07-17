import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
with col1:
    st.image("images/photo.jpg", width=650, use_container_width=False)

with col2:
    st.markdown(
        """
        <div style='text-align: center;'>
            <h1>Conache Antonio Mihaita<br><br></h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    content = """
    - I am passionate and driven person with a strong commitment to continuous learning and personal growth. 
    - I want to contribute as a collaborative team player who thrives in dynamic environments. 
    - I am applying critical thinking and a problem-solving mindset to overcome challenges and deliver results. 
    - I am always seeking new opportunities to expand skills both on and off the job, and committed to growing and evolving.
    """
    st.info(content)

st.markdown(
    """
    <div style='text-align: center;'>
        <h3><br>Below there are some of my apps that are included in my Python portfolio: <br></h3>
    </div>
    """,
    unsafe_allow_html=True
)

col3, col5, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=",")

with col3:
    for index, row in df[:2].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"{row['url']}")

with col4:
    for index, row in df[2:3].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"{row['url']}")