import streamlit as st

st.set_page_config(page_title="Мій Супер-Додаток", 
                   page_icon="https://static.wikia.nocookie.net/findthechomiks-fanon/images/9/9d/KYS.png", 
                   layout="wide")

st.title("Ласкаво просимо до мого додатку")

tab1, tab2 = st.tabs(["Про мене", "Мій інструмент"])

with tab1:
    st.header("Знайомство з автором")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("shutterstock_2331893385.jpg", caption="Я", width=400)
    with col2:
        st.subheader("Привіт, я мабутній Python Developer")
        st.write("Я навчаюсь в Малій Компютерній Академії IT STEP. Створюю круті веб-додатки та вивчаю Streamlit")
        with st.container():
            st.info("Контакти для звя`зку") # st.error() st.warning() st.success
            st.markdown("- GitHub: [Мій профіль](https://github.com)")
            st.markdown("- E-Mail: student@itstep.org")

with tab2:
    st.info("Ця вкладка у розробці")
            
            
            