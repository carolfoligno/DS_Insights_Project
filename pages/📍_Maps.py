import pandas as pd
import streamlit as st
import Home as ho
# from streamlit_folium import folium_static
from streamlit_folium import st_folium
import folium
from folium.plugins import MarkerCluster




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
        page_icon='📍',
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
        df = data.copy()
        df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
        x = st.checkbox('Shows Map: ')
        if x:
            map(df)

