import streamlit as st
import helper as h
import altair as alt
###configs
st.set_page_config(layout="wide", page_title="Weight Tracker")

###vars

###widgets

def main_chart():
    min_y = round(st.session_state['weight_history']['weight'].min()) - 1
    max_y = round(st.session_state['weight_history']['weight'].max()) + 1
    chart = alt.Chart(st.session_state['weight_history']).mark_line().encode(
        x=alt.X('date', axis=alt.Axis(title='Date')),
        y=alt.Y('weight', scale=alt.Scale(domain=(min_y, max_y)), axis=alt.Axis(title='Weight'))
    )
    st.write('Weight history chart:')
    st.altair_chart(chart, use_container_width=True)

def widget_get_data():
    st.write('Upload your file or create a new one:')
    uploaded_file = st.file_uploader('',type={"csv"})
    if uploaded_file is not None:
        st.session_state['weight_history'] = h.get_csv(uploaded_file)
    #if st.button('Create a new file'):
    #    st.session_state['weight_history'] = h.make_new()
    if st.button('Create a random weight history'):
        st.session_state['weight_history'] = h.sample_weight(50, 150, 400)
    
def widget_reset_data():
    if st.button('Reset table data'):
        try:
            del st.session_state['weight_history']
        except:
            st.write('No data to remove.')

###sidebar

with st.sidebar:
    widget_get_data()
    widget_reset_data()

#page content

st.title("Weight Tracker")

if 'weight_history' in st.session_state:
    #st.line_chart(st.session_state['weight_history'], x = 'date')
    main_chart()
