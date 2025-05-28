# MIT License
# Copyright (c) 2025 Dogan Ege Bulte
# GitHub: https://github.com/Dege34
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import streamlit as st
import sqlite3
import pandas as pd
import datetime

DB_PATH = "gym.db"

def get_conn():
    return sqlite3.connect(DB_PATH, check_same_thread=False)

st.set_page_config(page_title="GYM Database App", layout="wide")

st.sidebar.title("GYM Database Navigation")
page = st.sidebar.radio("Go to", ["Homepage", "Courses", "Instructors", "Add Course", "Add Lesson"])

if page == "Homepage":
    st.title("Welcome to My GYM Database App!")
    st.markdown("""
    **Author:** *Dogan Ege BULTE*  
    **Objective:** Manage and visualize activities in a gym using the GYM database.
    
    ---
    ### **Scheduled Lessons Analysis**
    """)
    conn = get_conn()
    program_df = pd.read_sql_query("SELECT * FROM PROGRAM", conn)
    
    if not program_df.empty:

        st.subheader("Lessons by Start Time")
        slot_counts = program_df.groupby("StartTime").size().reset_index(name="NumLessons")
        st.bar_chart(slot_counts.set_index("StartTime"))

        st.subheader("Lessons by Day of the Week")
        day_counts = program_df.groupby("Day").size().reindex([
            "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"
        ]).fillna(0).reset_index(name="NumLessons")
        st.line_chart(day_counts.set_index("Day"))
    else:
        st.info("No lessons scheduled yet, Do u want to add some lessons to see charts??")

elif page == "Courses":
    st.title("View & Filter Courses")
    conn = get_conn()
    courses_df = pd.read_sql_query("SELECT * FROM COURSES", conn)

    if courses_df.empty:
        st.warning("No course available.")
    else:
        c_types = sorted(courses_df["CType"].unique())
        min_level, max_level = int(courses_df["Level"].min()), int(courses_df["Level"].max())

        with st.expander("Filter Options", expanded=True):
            selected_types = st.multiselect("Course Types", options=c_types, default=c_types)
            level_range = st.slider("Level Range", min_value=1, max_value=4, value=(min_level, max_level))

        filtered = courses_df[
            courses_df["CType"].isin(selected_types) & 
            (courses_df["Level"].between(level_range[0], level_range[1]))
        ]

        col1, col2 = st.columns(2)
        col1.metric("Number of Courses", len(filtered))
        col2.metric("Distinct Types", filtered["CType"].nunique())
        st.dataframe(filtered)

        with st.expander("Lesson Plans for Selected Courses"):
            if filtered.empty:
                st.warning("No courses match the filter.")
            else:
                codes = tuple(filtered["CodC"])
                sql = """
                SELECT P.CodC, P.Day, P.StartTime, P.Duration, I.Name || ' ' || I.Surname as Instructor, I.Email
                FROM PROGRAM P JOIN INSTRUCTOR I ON P.FisCode = I.FisCode
                WHERE P.CodC IN ({seq})
                """.format(seq=','.join(['?']*len(codes)))
                lesson_plans = pd.read_sql_query(sql, conn, params=codes)
                if lesson_plans.empty:
                    st.warning("No lesson plans found for selected courses.")
                else:
                    st.dataframe(lesson_plans)

elif page == "Instructors":
    st.title("Instructor List & Filter")
    conn = get_conn()
    inst_df = pd.read_sql_query("SELECT * FROM INSTRUCTOR", conn)
    if inst_df.empty:
        st.warning("No instructors found.")
    else:
        with st.expander("Filter Instructors", expanded=True):
            last_name = st.text_input("Search by Surname")
            min_date = datetime.date(1950, 1, 1)
            max_date = datetime.date.today()
            date_range = st.date_input("Birth Date Range", value=(min_date, max_date))
        filtered = inst_df.copy()
        if last_name:
            filtered = filtered[filtered["Surname"].str.contains(last_name, case=False)]
        if len(date_range) == 2:
            filtered = filtered[
                (filtered["BirthDate"] >= str(date_range[0])) &
                (filtered["BirthDate"] <= str(date_range[1]))
            ]
        if filtered.empty:
            st.error("No instructors match the criteria.")
        else:
            for _, row in filtered.iterrows():
                st.write(f"👤 **{row['Name']} {row['Surname']}**  \n"
                         f"- Birth Date: {row['BirthDate']}  \n"
                         f"- Email: {row['Email']}  \n"
                         f"- Telephone: {row['Telephone']}  \n"
                         f"- FisCode: {row['FisCode']}")

elif page == "Add Course":
    st.title("Add a New Course")
    with st.form("add_course"):
        codc = st.text_input("Course Code (STARTING FROM 'CT')")
        name = st.text_input("Course Name")
        ctype = st.text_input("Course Type")
        level = st.number_input("Level (1-4)", min_value=1, max_value=4, step=1)
        submitted = st.form_submit_button("Add Course")
    if submitted:
        if not (codc and name and ctype and level):
            st.error("All fields are required.")
        elif not codc.startswith("CT"):
            st.error("Course Code must start with 'CT'.")
        else:
            conn = get_conn()
            try:
                conn.execute(
                    "INSERT INTO COURSES (CodC, Name, CType, Level) VALUES (?, ?, ?, ?)",
                    (codc, name, ctype, level)
                )
                conn.commit()
                st.success(f"Course {codc} added successfully.")
            except sqlite3.IntegrityError as e:
                st.error(f"Error: {str(e)}")

elif page == "Add Lesson":
    st.title("Schedule a New Lesson")
    conn = get_conn()
    insts = pd.read_sql_query("SELECT FisCode FROM INSTRUCTOR", conn)
    courses = pd.read_sql_query("SELECT CodC FROM COURSES", conn)
    with st.form("add_lesson"):
        fiscode = st.selectbox("Instructor (FisCode)", insts["FisCode"] if not insts.empty else [])
        codc = st.selectbox("Course (CodC)", courses["CodC"] if not courses.empty else [])
        day = st.selectbox("Day", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
        start_time = st.slider("Start Time (hour)", 6, 22, 9)
        duration = st.slider("Duration (minutes)", 15, 60, 45)
        room = st.text_input("Room")
        submitted = st.form_submit_button("Schedule Lesson")
    if submitted:
        if duration > 60:
            st.error("Duration cannot exceed 60 minutes.")
        elif not room:
            st.error("Room cannot be empty.")
        else:
            conn = get_conn()


            exists = pd.read_sql_query(
                "SELECT * FROM PROGRAM WHERE CodC=? AND Day=?",
                conn, params=(codc, day)
            )
            if not exists.empty:
                st.error("A lesson for this course is already scheduled on this day.")
            else:
                try:
                    conn.execute(
                        "INSERT INTO PROGRAM (FisCode, Day, StartTime, Duration, CodC, Room) VALUES (?, ?, ?, ?, ?, ?)",
                        (fiscode, day, start_time, duration, codc, room)
                    )
                    conn.commit()
                    st.success("Lesson scheduled successfully!")
                except sqlite3.IntegrityError as e:
                    st.error(f"Error: {str(e)}")
