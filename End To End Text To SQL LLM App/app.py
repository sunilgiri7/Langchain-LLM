from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3 
import google.generativeai as genai

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

#function to load gemini
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

#function to retrive query from database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)

    return rows

prompt = [
"""
You are an expert in converting English questions to SQL queries!
The SQL database has the name EMPLOYEE and has the following columns - NAME, JOB, YOE (Years of Experience), SALARY.

For example:
- Example 1: Insert the following employee data into the EMPLOYEE table:
  ('Sunil Giri', 'Analyst', 5, 70000)

- Example 2: Insert the following employee data into the EMPLOYEE table:
  ('Jane Smith', 'Developer', 3, 60000)

Example 1: Retrieve all records from the EMPLOYEE table:
SELECT * FROM EMPLOYEE;

Example 2: Retrieve the names and job roles of employees with a salary greater than 60000:
SELECT NAME, JOB FROM EMPLOYEE WHERE SALARY > 60000;

Example 3: Find the average years of experience (YOE) for all employees:
SELECT AVG(YOE) FROM EMPLOYEE;

Example 4: Count the number of employees in each job role:
SELECT JOB, COUNT(*) FROM EMPLOYEE GROUP BY JOB;

Example 5: Retrieve the employee with the highest salary:
SELECT * FROM EMPLOYEE ORDER BY SALARY DESC LIMIT 1;

Example 6: Update the salary for the employee named 'John Doe' to 85000:
UPDATE EMPLOYEE SET SALARY = 85000 WHERE NAME = 'John Doe';

Example 7: Delete all records of employees with less than 2 years of experience:
DELETE FROM EMPLOYEE WHERE YOE < 2;

Example 8: Find the distinct job roles in the EMPLOYEE table:
SELECT DISTINCT JOB FROM EMPLOYEE;

Example 9: Retrieve employees whose names start with 'A' or 'B':
SELECT * FROM EMPLOYEE WHERE NAME LIKE 'A%' OR NAME LIKE 'B%';

Example 10: Calculate the total salary for all employees:
SELECT SUM(SALARY) FROM EMPLOYEE;

also the sql code should not have ``` in beginning or end and sql word in output
"""
]

## Streamlit app
def main():
    st.set_page_config(page_title="I can Retrieve Any SQL query", page_icon=":gem:", layout="wide")
    st.title("Gemini App To Retrieve SQL Data")
    
    question = st.text_input("Input your question:")
    submit = st.button("Ask the question")

    if submit:
        # Generate SQL query using gemini-pro model
        generated_query = get_gemini_response(question, prompt)

        # Display the generated SQL query
        st.subheader("Generated SQL Query:")
        st.code(generated_query, language="sql")

        # Execute the generated query
        try:
            response = read_sql_query(generated_query, 'employer.db')
            st.subheader("Query Result:")
            st.table(response)
        except Exception as e:
            st.error(f"Error executing the query: {e}")

if __name__ == "__main__":
    main()