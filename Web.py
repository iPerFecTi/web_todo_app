import streamlit as st
import Functions

todos = Functions.get_todos()

st.set_page_config(layout="wide")

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    Functions.write_todos(todos)

todos = Functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("<h1>This app is to increase your <b>productivity</b>.</h1>",
         unsafe_allow_html=True)


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        Functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a todo: ", placeholder= "Add new todo...",
              on_change=add_todo, key='new_todo')

st.session_state
