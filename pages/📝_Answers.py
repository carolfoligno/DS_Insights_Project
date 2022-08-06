import pandas as pd
import numpy as np
import streamlit as st
import Home as ho
import plotly.express as px
import plotly.graph_objects as go

@st.cache
def question_1(data, filter):

    # questão 01
    # agrupando em um dataframe as medianas agrupados por zipcode
    data_f = data.copy()
    df = data_f[['price', 'zipcode']].groupby('zipcode').median().reset_index()
    # mudando os nomes das colunas
    df.columns = ['zipcode', 'median_price']
    # merge os dados df com data
    df2 = pd.merge(data_f, df, how='inner', on="zipcode")
    df2['status'] = np.where((df2['price'] < df2['median_price']) &
                             (df2['condition'] >= 3),
                             'buy', "don't buy")
    # criando um dataframe para o relatório
    data_1 = df2[['id', 'zipcode', 'price', 'median_price', 'condition', 'status']]
    data_1.columns = ['ID', 'ZIPCODE', 'SALE PRICE', 'MEDIAN PRICE', 'CONDITION', 'STATUS']

    #colocando o filtro no dataframe
    if (filter == []):
        data_1 = data_1.copy()
    else:
        data_1 = data_1.loc[data_1['ZIPCODE'].isin(filter), :]


    return data_1

def question_2(data, filter):

    # questão 02
    # convertendo 'date'
    df2 = data.copy()
    df2['date'] = pd.to_datetime(data['date']).dt.strftime('%Y-%m-%d')
    df2['monthy'] = pd.to_datetime(df2['date']).dt.strftime('%m')
    # criando nova coluna de temporadas
    df2['season'] = df2['monthy'].apply(lambda x: 'spring' if (x == '03') | (x == '04') | (x == '05') else
        'summer' if (x == '06') | (x == '07') | (x == '08') else
        'fall' if (x == '09') | (x == '10') | (x == '11') else
        'winter' if (x == '12') | (x == '01') | (x == '02') else 'NA')

    # mediana de preços agrupado por zipcode e season
    df3 = df2[['price', 'zipcode', 'season']].groupby(['zipcode', 'season']).median().reset_index()
    df3.columns = ['zipcode', 'season', 'median_price']
    # merge dos dataframes
    df1 = pd.merge(df2, df3, how='inner', on=['zipcode', 'season'])
    # preço de vendas
    df1['price_sale'] = np.where(df1['price'] > df1['median_price'],
                                 df1['price'] * 1.3,
                                 df1['price'] * 1.1)
    # lucro
    df1['profit'] = df1['price_sale'] - df1['price']
    # criando o relatório
    data_2 = df1[['id', 'zipcode', 'season', 'median_price', 'price', 'price_sale', 'profit']]
    data_2.columns = ['ID', 'ZIPCODE', 'SEASON', 'MEDIAN PRICE', 'BUY PRICE', 'SALE PRICE', 'PROFIT']
    # criando filtros
    # f_zip = st.multiselect('Enter the zipcode: ',set(data_2['ZIPCODE'].unique()))
    c1, c2, c3, c4, c5 = st.columns(5)
    button_spring = c1.button('Spring')
    button_summer = c2.button('Summer')
    button_fall = c3.button('Fall')
    button_win = c4.button('Winter')
    button_reset = c5.button('Restart')

    if (filter != []) & button_spring:
        data_2 = data_2.loc[(data_2['ZIPCODE'].isin(filter)) & (data_2['SEASON'] == 'spring'), :]
    elif (filter != []) & button_summer:
        data_2 = data_2.loc[(data_2['ZIPCODE'].isin(filter)) & (data_2['SEASON'] == 'summer'), :]
    elif (filter != []) & button_fall:
        data_2 = data_2.loc[(data_2['ZIPCODE'].isin(filter)) & (data_2['SEASON'] == 'fall'), :]
    elif (filter != []) & button_win:
        data_2 = data_2.loc[(data_2['ZIPCODE'].isin(filter)) & (data_2['SEASON'] == 'winter'), :]
    elif (filter == []) & button_spring:
        data_2 = data_2.loc[data_2['SEASON'] == 'spring', :]
    elif (filter == []) & button_summer:
        data_2 = data_2.loc[data_2['SEASON'] == 'summer', :]
    elif (filter == []) & button_fall:
        data_2 = data_2.loc[data_2['SEASON'] == 'fall', :]
    elif (filter == []) & button_win:
        data_2 = data_2.loc[data_2['SEASON'] == 'winter', :]
    elif (filter == []) & button_reset or (filter != []) & button_reset:
        data_2 = data_2.copy()
    elif (filter != []):
        data_2 = data_2.loc[data_2['ZIPCODE'].isin(filter), :]
    else:
        data_2 = data_2.copy()

    return data_2

def map_plot(data):
    # plot graficos
    df2 = data.copy()
    df2['date'] = pd.to_datetime(data['date']).dt.strftime('%Y-%m-%d')
    df2['monthy'] = pd.to_datetime(df2['date']).dt.strftime('%m')
    # criando nova coluna de temporadas
    df2['season'] = df2['monthy'].apply(lambda x: 'spring' if (x == '03') | (x == '04') | (x == '05') else
    'summer' if (x == '06') | (x == '07') | (x == '08') else
    'fall' if (x == '09') | (x == '10') | (x == '11') else
    'winter' if (x == '12') | (x == '01') | (x == '02') else 'NA')

    data_plot = df2[['price', 'season']].groupby( 'season').median().reset_index()
    data_plot['median_all_yr'] = data_plot['price'].mean()
    # st.dataframe(data_plot)
    # plot
    fig = px.bar(data_plot, x="season", y="price", title='Season Average Price')
    # add uma linha da média geral
    fig1 = fig.add_traces(go.Scatter(x=data_plot.season, y=data_plot.median_all_yr, mode='lines', name='Mean of price'))
    st.plotly_chart(fig1, use_container_width=True)

    return None

def results(data):
    data = data[['SEASON', 'PROFIT']].groupby('SEASON').mean().reset_index()

    return data

if __name__ == '__main__':
    st.set_page_config(
        page_title='Answers',
        page_icon='📝',
        layout='wide'

    )
    with st.spinner("Loading Answers... "):

        st.header('DATA INSIGHTS')
        st.header('Business Questions')
        st.subheader('1. Which is the real state that House Rocket should buy and at what price?')
        st.markdown('The criteria taken to classify a property as good for purchase were: '
                    'its price below average and its condition greater than or equal to 3.')

        data = ho.get_data()

        f_zipcode = st.sidebar.multiselect('Enter zipcode',data['zipcode'])

        data_q1 = question_1(data, f_zipcode)
        st.write('Data Report')
        st.dataframe(data_q1)

        st.subheader('2. Once bought the real state, when is the best moment to sell and at what price?')
        data_q2 = question_2(data, f_zipcode)
        st.dataframe(data_q2)
        st.write('Results')
        d_result = results(data_q2)
        st.dataframe(d_result)
        map_plot(data)