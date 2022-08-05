import streamlit as st
import pandas as pd
from PIL import Image



@st.cache
def get_data():
    data = pd.read_csv('kc_house_data.csv')

    return data

@st.cache
def chance_data(data):
    # cleaning data
    df = data.copy()
    df = df.drop(['sqft_living15', 'sqft_lot15'], axis=1)
    df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
    df.columns = ['ID', 'DATE', 'PRICE', 'BEDROOMS', 'BATHROOMS',
                  'LIVING SQFT', 'LOT SQFT', 'FLOORS', 'WATERFRONT', 'VIEW', 'CONDITION', 'GRADE',
                  'ABOVE SQFT', 'BASEMENT SQFT', 'YEAR BUILT', 'YEAR RENOVATED', 'ZIPCODE', 'LATITUDE',
                  'LONGITUDE']

    return df


if __name__ == '__main__':
    st.set_page_config(
        page_title='Home',
        page_icon='🏘',
        layout='wide'

    )
    data = get_data()
    data = chance_data(data)
    with st.spinner("Loading Home... "):
        st.sidebar.title("Project")
        st.sidebar.info(
            "This is a project carried out through the teachings of the course 'Python do ZERO ao DS'. "
            "Available on [GitHub](https://github.com/). "

        )
        st.sidebar.title("About")
        st.sidebar.info(
            """
            This project is a Descriptive Analysis of Seattle property sales data for 
            the purpose of answering the CEO's questions and gaining insights.
    """
        )

        st.markdown("<h1 style='text-align: center; color: darkred;'>HOUSE ROCKET COMPANY</h1>", unsafe_allow_html = True)
        st.markdown("<h2 style='text-align: center; color: grey;'>Welcome to property buy and sell company</h2>", unsafe_allow_html = True)

        c1,c2,c3 = st.columns([1,1,1])
        with c1:
            st.write('')
        with c2:
            st.image(Image.open('imagem.png'))
        with c3:
            st.write('')
        st.markdown('')
        st.markdown('')
        st.markdown('')
        st.write('''House Rocket is a digital platform whose business
        model is the purchase and sale of real estate using technology.''')
        st.write('''

        Their main strategy is to buy good homes in great locations at low 
        prices and then resell them later at higher prices. 
        The greater the difference between buying and selling, 
        the greater the company's profit and therefore the greater its revenue.
        ''')


        data = get_data()
        df = chance_data(data)
        # check button
        x = st.checkbox('Shows Dataset of Properties for Sale in Seattle ')
        if x:
            st.header('Property Data on Sells in Seattle ')
            st.dataframe(df, width=2000)