import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title='Data Dashboard', layout='wide')

st.title('📊 Interactive Data Dashboard')

# File Upload
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Data Preview")
    st.dataframe(df.head())
    
    # Basic Statistics
    st.write("### Basic Statistics")
    st.write(df.describe())
    
    # Select Numeric Columns for Visualization
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    
    if numeric_cols:
        col1, col2 = st.columns(2)
        
        with col1:
            selected_col = st.selectbox("Select a column for Histogram", numeric_cols)
            fig, ax = plt.subplots()
            ax.hist(df[selected_col], bins=20, color='skyblue', edgecolor='black')
            st.pyplot(fig)
        
        with col2:
            st.write("### Correlation Matrix")
            if not numeric_cols:
                st.warning("No numeric columns available for correlation matrix.")
            else:
                st.write(df[numeric_cols].corr().fillna(0))
    
    # Data Filtering
    st.write("### Data Filtering")
    filter_column = st.selectbox("Select column to filter", df.columns)
    unique_values = df[filter_column].unique()
    selected_value = st.selectbox("Select value", unique_values)
    filtered_data = df[df[filter_column] == selected_value]
    st.write(filtered_data)
    
    # Anomaly Detection (Z-score Method)
    st.write("### Anomaly Detection")
    anomaly_col = st.selectbox("Select numeric column for anomaly detection", numeric_cols)
    threshold = st.slider("Select Z-score threshold", 1.0, 4.0, 3.0)
    
    df['Z-score'] = np.abs((df[anomaly_col] - df[anomaly_col].mean()) / df[anomaly_col].std())
    anomalies = df[df['Z-score'] > threshold]
    st.write("Detected Anomalies:", anomalies)

    # Download Filtered Data
    st.download_button("Download Filtered Data", filtered_data.to_csv(index=False), "filtered_data.csv", "text/csv")
