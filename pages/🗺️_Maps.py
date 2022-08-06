import pandas as pd
import streamlit as st
import Home as ho
import numpy as np
# from streamlit_folium import folium_static
from streamlit_folium import st_folium
import folium
from folium.plugins import MarkerCluster


def profit_df(data):

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

    return df1

def top_spring(data):

    data = data.loc[data['season'] == 'spring',:]
    data.sort_values(by='profit', ascending=False)

    return data

def top_winter(data):

    data = data.loc[data['season'] == 'winter', :]
    data.sort_values(by='profit', ascending=False)

    return data

def map(data):

    map_density = folium.Map(location=[data['lat'].mean(), data['long'].mean()],
                                 default_zoom_start=15)
    # adicinando os pontos no mapa
    marker_cluster = MarkerCluster().add_to(map_density)
    for name, row in data.iterrows():
        folium.Marker([row['lat'], row['long']],
                          popup=f'Sold $ {row["price"]}, \n'
                                f'Features: {row["date"]}, \n'
                                f'sqft: {row["sqft_living"]}, \n'
                                f'{row["bedrooms"]} bedrooms, \n'
                                f'{row["bathrooms"]} bathrooms, \n'
                                f'year built: {row["yr_built"]} \n').add_to(marker_cluster)

    # para plotar o floium no streamlit utilizei no with
    st_folium(map_density)

    return None


if __name__ == '__main__':
    st.set_page_config(
        page_title='Map',
        page_icon='🗺️',
        layout='wide'

    )
    with st.spinner("Loading Maps... "):
        st.header('MAP')
        st.subheader('Region Overview')
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
        data = ho.get_data()
        df1 = profit_df(data)
        df_winter = top_winter(df1)
        df_winter = df_winter.head(10)
        df_spring = top_spring(df1)
        df_spring = df_spring.head(10)

        x = st.checkbox('Shows Map: ')
        if x:
            c1, c2 = st.columns(2)
            with c1:
                st.write('Top 10 - Property for Sale in Spring')
                map(df_spring)
            with c2:
                st.write('Top 10 - Property for Buy in Winter')
                map(df_winter)

