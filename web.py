import streamlit as st
from functions import *

todos = get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    write_todos(todos)

st.title("My Todo App")
st.subheader("This is my Todo App")
st.write("This app is to increase your Productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add new To-do",
              on_change=add_todo, key="new_todo")