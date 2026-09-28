import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Streamlit Simple App')
page = st.sidebar.radio('Pilih Halaman', ['Dataset', 'Visualisasi'])

if page == 'Dataset':
    st.header("Halaman Dataset")
    data = pd.read_csv("pddikti_example.csv")
    st.write(data)

elif page == "Visualisasi":
    st.header("Halaman Visualisasi")

    data = pd.read_csv("pddikti_example.csv")

    selected_university = st.selectbox('Pilih Universitas', data['universitas'].unique())
    filtered_data = data[data['universitas'] == selected_university]

    fig, ax = plt.subplots(figsize=(12, 6))

    for prog_studi in filtered_data['program_studi'].unique():
        subset = filtered_data[filtered_data['program_studi'] == prog_studi]

        subset = subset.sort_values(by="id", ascending=False)
        
        ax.plot(subset['semester'], subset['jumlah'], label=prog_studi)

    ax.set_title(f"Visualisasi Data untuk {selected_university}")
    ax.set_xlabel('Semester')
    plt.xticks(rotation=90)  
    ax.set_ylabel('Jumlah')
    ax.legend()

    st.pyplot(fig)