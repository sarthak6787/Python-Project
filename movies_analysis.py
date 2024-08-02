import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

try:
    df = pd.read_csv('movies.csv')
except FileNotFoundError:
    st.error('File not found. Please ensure the "movies.csv" file is in the correct directory.')
    st.stop()
except pd.errors.EmptyDataError:
    st.error('File is empty. Please provide a valid "movies.csv" file.')
    st.stop()
except Exception as e:
    st.error(f'An unexpected error occurred: {e}')
    st.stop()

# Streamlit app
st.write('EDA of Movie Analysis')

try:
    # Printing the DataFrame
    st.subheader('Original dataset')
    st.write(df)
    st.write(df.shape)

    # Null values
    st.subheader("After handling missing values")
    df.dropna(inplace=True)
    st.write(df)
    st.write(df.shape)

    # Duplicates
    st.subheader("After handling duplicates")
    df.drop_duplicates(inplace=True)
    st.write(df)
    st.write(df.shape)

    # Example of EDA with Streamlit
    st.subheader('Bar Chart Example')
    x_column = st.selectbox('Select X-axis column', df.columns, index=2)

    if x_column == 0:
        st.error('Please select a different column for the X-axis.')
    else:
        # Bar chart
        st.subheader('Bar Chart')
        st.bar_chart(df[x_column].head(10), color='#ff69b4')

        # Line chart
        st.subheader('Line Chart')
        st.line_chart(df[x_column].head(60))

        # Scatter plot
        st.subheader('Scatter Plot')
        st.scatter_chart(df[x_column].head(60))


        # Area chart
        st.subheader('Area Chart')
        st.area_chart(df[x_column].head(60))

        # Pie chart using matplotlib
        st.subheader("Pie chart using matplotlib")
        plt.figure(figsize=[10, 10])
        plt.pie(df[x_column].head(10).value_counts().values,
                autopct='%1.1f%%',
                labels=df[x_column].head(10).value_counts().index,
                colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'])
        st.pyplot(plt)

except AttributeError as e:
    st.error(f'Attribute error: {e}')
except TypeError as e:
    st.error(f'Type error: {e}')
except Exception as e:
    st.error(f'An unexpected error occurred: {e}')
    

