
import streamlit as st
import pandas as pd

# --------------------------------
# PAGE CONFIGURATION
# --------------------------------
st.set_page_config(
    page_title="Student Grade Manager",
    page_icon="🎓",
    layout="wide"
)

# --------------------------------
# TITLE
# --------------------------------
st.title("🎓 Student Grade Manager")
st.write("Manage student marks and calculate grades easily.")

st.divider()

# --------------------------------
# INITIAL STUDENT DATA
# --------------------------------
if "students" not in st.session_state:
    st.session_state.students = [
        {"name": "Priya", "mark": 92, "grade": "A"},
        {"name": "Arun", "mark": 78, "grade": "C"},
        {"name": "Divya", "mark": 59, "grade": "E"}
    ]

# --------------------------------
# GRADE FUNCTION
# --------------------------------
def get_grade(mark):

    if mark >= 90:
        return "A"

    elif mark >= 80:
        return "B"

    elif mark >= 70:
        return "C"

    elif mark >= 60:
        return "D"

    else:
        return "E"

# --------------------------------
# ADD STUDENT
# --------------------------------
st.subheader("➕ Add New Student")

with st.form("student_form"):

    name = st.text_input("Enter Student Name")

    mark = st.number_input(
        "Enter Student Mark",
        min_value=0,
        max_value=100,
        value=50,
        step=1
    )

    submit = st.form_submit_button("Add Student")

    if submit:

        if name.strip() == "":
            st.error("Name cannot be empty!")

        else:

            grade = get_grade(mark)

            student = {
                "name": name.strip(),
                "mark": mark,
                "grade": grade
            }

            st.session_state.students.append(student)

            st.success("Student added successfully!")

# --------------------------------
# SHOW RESULTS
# --------------------------------
st.divider()

st.subheader("📋 Student Results")

if len(st.session_state.students) == 0:

    st.warning("No students available!")

else:

    df = pd.DataFrame(st.session_state.students)

    df.columns = ["Name", "Mark", "Grade"]

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    # --------------------------------
    # STATISTICS
    # --------------------------------

    marks = [student["mark"]
             for student in st.session_state.students]

    average = sum(marks) / len(marks)

    highest = max(marks)

    lowest = min(marks)

    st.divider()

    st.subheader("📊 Student Statistics")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Students",
        len(st.session_state.students)
    )

    col2.metric(
        "Average Mark",
        f"{average:.1f}"
    )

    col3.metric(
        "Highest Mark",
        highest
    )

    col4.metric(
        "Lowest Mark",
        lowest
    )

# --------------------------------
# FOOTER
# --------------------------------
st.divider()

st.caption(
    "Student Grade Manager | Developed using Python and Streamlit"
)
