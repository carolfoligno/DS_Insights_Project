import pandas as pd
import streamlit as st
import Home as ho
import plotly.express as px
import plotly.graph_objects as go


@st.cache
def chance_data(data):
    # cleaning data
    data = data.drop(['sqft_living15','sqft_lot15' ],axis=1)
    data['date'] = pd.to_datetime(data['date']).dt.strftime('%Y-%m-%d')
    data = pd.set_option('display.float_format', lambda x: '%.2f' % x)

    return data


def hypo1(data):

    st.subheader('Hypothesis 1: Usually real state with waterfront view are 30% more expensive at average.')
    data_f = data.copy()
    data_f['waterview'] = data_f['waterfront'].apply(lambda x: 'yes' if x == 1 else 'no')
    h1 = data_f[['waterview', 'price']].groupby('waterview').mean().reset_index()
    # variação percentual entre os preços:
    # (preço final / preço inicial -1 )*100
    x = (h1.loc[1, 'price'] / h1.loc[0, 'price'] - 1) * 100
    st.write(f'False, in fact real state with waterfront view are {x:.2f}% more expensive at average.')
    st.dataframe(h1)

    # PLOT
    fig = px.bar(h1, x='waterview', y='price',
                title='Waterfornt View Average Price',
               color_discrete_sequence=['darkorange'], height=700)
    st.plotly_chart(fig, use_container_width=True)

    return None


def hypo2(data):

    st.subheader('Hypothesis 2: Real state with year of construction less than 1955 are 50% cheaper in average')
    data_f = data.copy()
    df1 = data_f[['price', 'yr_built']].groupby('yr_built').mean().reset_index()
    h2 = df1.loc[df1['yr_built'] < 1955, :]
    h2['median_all_yr'] = data_f['price'].mean()
    # st.dataframe(h2)
    # plot
    fig = px.line(h2, x="yr_built", y="price", title='Year Built 1900-1955 Average')
    # add uma linha da média geral
    fig1 = fig.add_traces(go.Scatter(x=h2.yr_built, y=h2.median_all_yr, mode='lines', name='Mean of price'))
    st.plotly_chart(fig1, use_container_width=True)

    return None


def hypo3(data):

    st.subheader('Hypothesis 3: Real state without basement, have a greater sqft lot about 40% at average.')
    data_f = data.copy()
    data_f['basement'] = data_f['sqft_basement'].apply(lambda x: 'no' if x == 0 else 'yes')
    # calcular a mediana (para tirar os outliers e descobrir a mediana do tamanho do lot com e sem o porão)
    df = data_f[['basement', 'sqft_lot']].groupby('basement').median().reset_index()
    # variação percentual entre os preços:
    # (preço final / preço inicial -1 )*100
    x = (df.loc[1, 'sqft_lot'] / df.loc[0, 'sqft_lot'] - 1) * 100
    st.write(f'False, properties without basement in median are almost {x*-1:.2f}% larger than properties with.')
    # PLOT
    fig = px.bar(df, x='basement', y='sqft_lot', title='Median of Properties with or without basement',
                 color_discrete_sequence=['purple'])
    st.plotly_chart(fig, use_container_width=True)

    return None


def hypo4(data):

    st.subheader('Hypothesis 4: The price growth YoY of real state is 10%.')
    data_f = data.copy()
    # new feature
    data_f['years'] = pd.to_datetime(data_f['date']).dt.strftime('%Y')
    # suprimir a notação cientifica dos dados
    pd.set_option('display.float_format', lambda x: '%.2f' % x)
    df = data_f[['price', 'years']].groupby('years').mean().reset_index()
    # variação percentual entre os preços:
    # (preço final / preço inicial -1 )*100
    x = (df.loc[1, 'price'] / df.loc[0, 'price'] - 1) * 100
    st.write(f'False instead has an increase of {x:.2f} YoY.')
    # plot
    fig = px.bar(df, x='years', y='price', title='Growth YoY Average Price',
                 color_discrete_sequence=['darkorange'])
    st.plotly_chart(fig, use_container_width=True)

    return None


def hypo5(data):

    st.subheader('Hypothesis 5: Real state with 3 bathrooms have a price growth MoM of 15%.')
    st.write(f'False, see MoM percentage table')
    data_f = data.copy()
    data_f['month'] = pd.to_datetime(data_f['date']).dt.strftime('%Y-%m')
    df = data_f.loc[data_f['bathrooms'] == 3, :]
    df_plot = df[['price', 'month']].groupby('month').mean().reset_index()
    # variação percentual entre os preços:
    # (preço final / preço inicial -1 )*100
    ls = []
    for i in range(len(df_plot) - 1):
        x = (df_plot.loc[i + 1, 'price'] / df_plot.loc[i, 'price'] - 1) * 100
        ls.append(x)
    df1 = pd.DataFrame(ls, columns=['value MoM'])
    st.dataframe(df1)
    # plot
    fig = px.line(df_plot, x="month", y="price", title='Growth MoM Average Price of Properties with 3 bathrooms')
    st.plotly_chart(fig, use_container_width=True)

    return None


if __name__ == '__main__':
    st.set_page_config(
        page_title='Insights',
        layout='wide'

    )

    st.header('DATA INSIGHTS')
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
""")
    data = ho.get_data()
    hypo1(data)
    hypo2(data)
    hypo3(data)
    hypo4(data)
    hypo5(data)
