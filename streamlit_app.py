import sys
import streamlit as st
import numpy as np
#import matplotlib as mpl
from src.main_co2_calculator import main_CO2_calculator
from src.main_co2_calculator_EPD import main_CO2_calculator_EPD
st.set_page_config(page_title='Piles & panels', layout="wide", page_icon="⚙️")


if __name__ == '__main__':
    # Sidebar
    st.sidebar.markdown('# Form selection')
    select_options = [ 'CO2 Evaluator', 'CO2 Evaluator EPD Test', ]

    select_event = st.sidebar.selectbox('Select one of the forms', select_options, key='selected_form', index=0)

    if select_event == 'CO2 Evaluator':
        main_CO2_calculator(st, parameters=None)

    elif select_event == 'CO2 Evaluator EPD Test':
        main_CO2_calculator_EPD(st, parameters=None)

    else:
        pass


    # Version notes
    st.sidebar.header('Version and used packages')
    st.sidebar.write('CO2Calculator=bjg.05.2023')
    st.sidebar.write('python=' + sys.version[:6] + ', streamlit=' + st.__version__)
    st.sidebar.write('numpy=' + np.__version__ )


    st.sidebar.header('Development notes')
    st.sidebar.write("""Code devopment is based on Python with continuous integration """)

    st.sidebar.header('Contact')
    st.sidebar.write('BST-GBT-BK\Ragadeep Bojja')
    st.sidebar.write('ragadeep.bojja@bauer.de')