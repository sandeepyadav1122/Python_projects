# CSV and Excel File Viewer

This is a simple and advanced Streamlit application that allows users to upload, view, and analyze CSV and Excel files. The app provides various data exploration tools, including descriptive statistics, visualizations, and a Pandas Profiling report.

## Features

- **File Upload**: Supports CSV and Excel file formats.
- **Data Preview**: Displays the first 10 rows of the uploaded dataset.
- **Descriptive Statistics**: Provides summary statistics of the dataset.
- **Data Visualization**: Allows users to generate histograms, boxplots, line charts, and scatter plots.
- **Correlation Matrix**: Displays the correlation matrix of the dataset.
- **Missing Values**: Shows the count of missing values in each column.
- **Pandas Profiling Report**: Generates an in-depth profiling report of the dataset.
- **Download Options**: Users can download the dataset in CSV or Excel format.

## Installation

To run this application locally, follow these steps:

1. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Streamlit application**:
    ```bash
    streamlit run app.py
    ```

## Usage

- Open your web browser and go to `http://localhost:8501` to access the app.
- Upload a CSV or Excel file using the file uploader.
- Explore your data with the provided tools and download the modified data if needed.

## Screenshots

### Home Page
![Home Page](screenshots/home_page.png)

### Data Preview
![Data Preview](screenshots/data_preview.png)

### Descriptive Statistics
![Descriptive Statistics](screenshots/descriptive_statistics.png)

### Data Visualization
![Data Visualization](screenshots/data_visualization.png)

## Acknowledgments

- [Streamlit](https://www.streamlit.io/) for the awesome framework.
- [Pandas](https://pandas.pydata.org/) for data manipulation and analysis.
- [Matplotlib](https://matplotlib.org/) for data visualization.
- [Pandas Profiling](https://pandas-profiling.github.io/pandas-profiling/docs/master/index.html) for generating detailed data reports.
