import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import base64
import numpy as np
from pandas_profiling import ProfileReport
from io import BytesIO

# Set page title
st.title('CSV and Excel File Viewer')

# Cache uploaded file
@st.cache_data
def load_data(uploaded_file):
    if uploaded_file.name.endswith('.csv'):
        return pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('.xls') or uploaded_file.name.endswith('.xlsx'):
        return pd.read_excel(uploaded_file)
    else:
        raise ValueError("Invalid file format. Please upload a CSV or Excel file.")

# Generate download link
def generate_download_link(df, file_format='csv'):
    if file_format == 'csv':
        csv_file = df.to_csv(index=False)
        b64 = base64.b64encode(csv_file.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="data.csv">Download CSV File</a>'
    elif file_format == 'excel':
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df.to_excel(writer, index=False, sheet_name='Sheet1')
        writer.save()
        processed_data = output.getvalue()
        b64 = base64.b64encode(processed_data).decode()
        href = f'<a href="data:file/xlsx;base64,{b64}" download="data.xlsx">Download Excel File</a>'
    else:
        raise ValueError("Unsupported file format for download.")
    
    return href

# Upload file
uploaded_file = st.file_uploader("Choose a file", type=['csv', 'xls', 'xlsx'])

if uploaded_file is not None:
    try:
        # Load data
        df = load_data(uploaded_file)

        # Show dataframe
        st.write('## Data Preview')
        st.dataframe(df.head(10))

        # Show descriptive statistics
        st.write('## Descriptive Statistics')
        st.write(df.describe())

        # Plot data
        st.write('## Data Visualization')
        columns = st.multiselect('Select columns for plotting', df.columns.tolist())
        plot_type = st.selectbox('Select plot type', ['Histogram', 'Boxplot', 'Line', 'Scatter'])

        if columns:
            for column in columns:
                plt.figure(figsize=(10, 6))
                plt.title(f'{column} - {plot_type}')
                if plot_type == 'Histogram':
                    plt.hist(df[column], bins=30, edgecolor='black')
                elif plot_type == 'Boxplot':
                    plt.boxplot(df[column].dropna(), vert=False)
                elif plot_type == 'Line':
                    plt.plot(df[column])
                elif plot_type == 'Scatter' and len(columns) > 1:
                    st.warning("Scatter plot requires two columns.")
                    break
                st.pyplot(plt)

        # Download data options
        st.write('## Download Data')
        download_format = st.selectbox('Select download format', ['CSV', 'Excel'])
        if st.button('Generate Download Link'):
            href = generate_download_link(df, file_format=download_format.lower())
            st.markdown(href, unsafe_allow_html=True)

        # Additional functionality
        with st.expander('Additional Data Insights'):
            st.write('### Data Summary')
            buffer = BytesIO()
            df.info(buf=buffer)
            s = buffer.getvalue().decode('utf-8')
            st.text(s)
            
            st.write('### Correlation Matrix')
            st.write(df.corr())

            st.write('### Missing Values')
            st.write(df.isnull().sum())

        # Pandas Profiling
        with st.expander('Pandas Profiling Report'):
            profile = ProfileReport(df, title='Pandas Profiling Report', explorative=True)
            st_profile_report = profile.to_html()
            st.components.v1.html(st_profile_report, height=800, scrolling=True)

    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.write("Please upload a file to get started.")
