# Sales Analysis by Speech Recognition System

## Project Overview
 This project leverages speech recognition and natural language processing to enable voice-based sales analysis. Users can provide voice commands to query a sales database and generate visualizations of the data. The project uses Streamlit for the web interface, OpenAI's Whisper model for transcription, and GPT-3.5-turbo for generating SQL queries and Plotly visualization code.
## Table of Contents
### Project Overview
### Sales
### Features
### Setup Instructions
### Usage
### License
###  Features
* ### Voice Command Input:
  Record voice commands and transcribe them using OpenAI's Whisper model.
* ### SQL Query Generation:
  Convert transcribed voice commands into SQL queries using GPT-3.5-turbo.
* ### Data Visualization:
  Generate and display visualizations of the query results using Plotly.
* ### User-Friendly Interface:
  Easy-to-use interface built with Streamlit.
## Setup Instructions
### Prerequisites
* Python 3.8 or higher
* Streamlit
* OpenAI API key
* Required Python packages
## Set up OpenAI API key:
Saving  OpenAI API key in a file located at D:\\pago\\key\\key.
## Set up MySQL database:
Make sure r MySQL server is running and  have the necessary permissions to access the database. Update the database connection details in the code if needed.
## Running the Application
streamlit run app.py
## Usage
### 1. Start the application:
Open a terminal and run the Streamlit application.
### 2. Record voice commands:
Use the built-in audio recorder to capture your voice commands.
### 3. Transcription and SQL Query Generation:
The application will transcribe the audio and generate an SQL query based on the transcribed text.
### 4. Execute Query and Visualize Data:
The SQL query is executed on the MySQL database, and the results are fetched and displayed. Additionally, Plotly visualizations are generated based on the results.
### 5. License
This project is licensed under the MIT License.
********************************************************************************************************************************************************
# few insights from Data
### Total Sales:
What is the total sales amount for each branch and city?
### Monthly Sales Trend:
How do sales trends vary month-over-month?
### Customer Type Distribution:
What is the distribution of customer types (e.g., Member vs. Normal) in each branch?
### Gender Distribution:
What is the gender distribution of customers in each branch?
### Sales by Product Line: 
Which product lines generate the most revenue in each branch?
### Top Sales Performers:
Which branches or cities have the highest average rating?
### Gross Income Analysis:
 What is the gross income for each branch and product line?
### Popular Payment Methods:
What are the most popular payment methods used by customers in each city?
### Tax Contribution:
What is the total tax collected for each branch?
### COGS Analysis: 
What are the total cost of goods sold (COGS) for each branch and product line?
### Peak Sales Hours: 
What are the peak hours for sales in each branch?
### Gross Margin Percentage: 
What is the average gross margin percentage for each product line?


