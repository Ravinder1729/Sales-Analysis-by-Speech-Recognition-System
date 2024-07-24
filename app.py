import streamlit as st
import openai
from st_audiorec import st_audiorec
import tempfile
import mysql.connector
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt

# Load API key from file
with open("D:\\pago\\key\\key") as f:
    key = f.read().strip()

# Set OpenAI API key
openai.api_key = key

# Initialize audio recorder
#st.title("🎙️Sales Analysis by Speech Recognition System🤖")
st.markdown(
    """
    <h1 style='color: green;'>🎙️ Sales Analysis by Speech Recognition System 🤖</h1>
    """,
    unsafe_allow_html=True
)
audio = st_audiorec()

if audio:
    # Create a temporary file to store the audio data
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
        temp_file.write(audio)
        temp_file.seek(0)
        
        # Open the temporary file in binary mode for transcription
        with open(temp_file.name, "rb") as audio_file:
            # Transcribe audio using OpenAI's Whisper model
            transcript = openai.Audio.transcribe(
                file=audio_file,
                model="whisper-1",
                response_format="verbose_json",
                timestamp_granularities=["word"]
            )
        
        # Display transcript
        transcript_text = transcript.get('text', 'No transcript available')
        st.write(transcript_text)
        
        # SQL Query Generation
        #if st.button("Generate SQL Query"):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": """You are a helpful AI assistant. My table name is 'sales' and columns are: 
                'Invoice ID', 'Branch', 'City', 'Customer type', 'Gender', 'Product line', 'Unit price', 'Quantity', 'Tax 5%', 
                'Total', 'Date', 'Time', 'Payment', 'cogs', 'gross margin percentage', 'gross income', 'Rating'. 
                Please remember the user always speaks in English. Please convert the given prompt into an SQL query without any syntax errors."""},
                {"role": "user", "content": transcript_text}
            ]
        )

        if response.choices:
            sql_query = response.choices[0].message['content'].strip()
            st.write("Generated SQL Query:")
            st.write(sql_query)
            
            # Establishing MySQL database connection
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Ravinder@1729",
                database='pago'
            )
            mycursor = mydb.cursor(buffered=True)
            
            # Executing the SQL query
            mycursor.execute(sql_query)
            mydb.commit()
            
            # Fetching and displaying the results
            results = mycursor.fetchall()
            df = pd.DataFrame(results, columns=mycursor.column_names)
            st.dataframe(df)
            
            # Cleanup
            mycursor.close()
            mydb.close()

        dataFrame = pd.read_csv(r"C:\Users\ravin\Downloads\archive (10)\supermarket_sales - Sheet1.csv")

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": """You are a helpful AI assistant. 
                    Please generate Plotly visualization code from the user's dataFrame without any syntax errors. The data columns are:
                    ['Invoice ID', 'Branch', 'City', 'Customer type', 'Gender', 'Product line', 'Unit price', 'Quantity', 'Tax 5%', 'Total', 'Date', 'Time', 'Payment', 'cogs', 'gross margin percentage', 'gross income', 'Rating']. 
                    Only generate Python code and do not use triple quotes."""},
                {"role": "user", "content": transcript_text}
            ]
        )

        if response.choices:
            plotly_code = response.choices[0].message['content']
            #st.write("Generated Plotly Code:")
            #st.code(plotly_code)

            # Prepare a context for the execution of the generated code
            exec_context = {
                "df": dataFrame,
                "px": px,
                "go": go,
                "st": st
            }

            # Execute the generated Plotly code
            try:
                exec(plotly_code, exec_context)
            except Exception as e:
                st.error(f"Error in executing Plotly code: {e}")
