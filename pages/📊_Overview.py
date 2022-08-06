import pandas as pd
import numpy as np
import streamlit as st
import Home as ho
import plotly.express as px

@st.cache

def overview_metrics(data):
    # STREAMLIT
    data_f = data.copy()

    # meio de colocar duas tabelas uma do lado da outra no streamlit


    data_f['price_m2'] = data_f['price'] / data_f['sqft_lot']

    # metricas
    df1 = data_f[['id', 'zipcode']].groupby('zipcode').count().reset_index()
    df2 = data_f[['price', 'zipcode']].groupby('zipcode').mean().reset_index()
    df3 = data_f[['sqft_living', 'zipcode']].groupby('zipcode').mean().reset_index()
    df4 = data_f[['price_m2', 'zipcode']].groupby('zipcode').mean().reset_index()

    # merge as metricas
    m1 = pd.merge(df1, df2, on='zipcode', how='inner')
    m2 = pd.merge(m1, df3, on='zipcode', how='inner')
    df = pd.merge(m2, df4, on='zipcode', how='inner')

    # nomeando as colunas do dataframe das metricas
    df.columns = ['ZIPCODE', 'TOTAL HOUSES', 'PRICE', 'LIVING M2',
                  'PRICE/M2']

    return df

def filter(df, f_region, f_atributes):

    if (f_region != []) and (f_atributes != []):
        df = df.loc[df['ZIPCODE'].isin(f_region), f_atributes]
    elif (f_region != []) and (f_atributes == []):
        df = df.loc[df['ZIPCODE'].isin(f_region), :]
    elif (f_region == []) and (f_atributes != []):
        df = df.loc[:, f_atributes]
    else:
        df = df.copy()

    return df



def overview_descriptive(data):
    data_f = data.copy()
    # Statistic descriptive
    # selecionar apenas as colunas int64 e float64
    num_attributes = data_f.select_dtypes(include=['int64', 'float64'])
    num_attributes = num_attributes.drop(['yr_built','yr_renovated', 'zipcode', 'lat', 'long', 'sqft_living15', 'sqft_lot15' ],axis=1)
    # calculando as metricas
    media = pd.DataFrame(num_attributes.apply(np.mean))
    mediana = pd.DataFrame(num_attributes.apply(np.median))
    std = pd.DataFrame(num_attributes.apply(np.std))
    max_ = pd.DataFrame(num_attributes.apply(np.max))
    min_ = pd.DataFrame(num_attributes.apply(np.min))

    df1 = pd.concat([media, mediana, std, max_, min_], axis=1).reset_index()
    df1.columns = ['ATTRIBUTES', 'MEAN', 'MEDIAN', 'STD', 'MAX', 'MIN']


    return df1

if __name__ == '__main__':
    st.set_page_config(
        page_title='Overview',
        page_icon='📊',
        layout='wide'

    )
    with st.spinner("Loading Overview... "):
        st.header('Overview')
        st.markdown('Data Analysis')
        data = ho.get_data()
        df = overview_metrics(data)
        # make filters
        f_atributes = st.sidebar.multiselect('Enter columns', df.columns)
        f_region = st.sidebar.multiselect('Enter zipcode',
                                          df['ZIPCODE'].unique())
        df = filter(df, f_region, f_atributes)
        st.markdown("<h2 style='text-align: center; color: grey;'>Metrics by Zipcode</h2>", unsafe_allow_html=True)

        c1,c2,c3 = st.columns([1,2,1])
        with c1:
            st.write('')
        with c2:
            st.dataframe(df, height=600, width=2000)
        with c3:
            st.write('')


        df1 = overview_descriptive(data)
        st.header('Descriptive Analysis')
        st.dataframe(df1, height=600)