import streamlit as st
import Funtions.functions as funct

todos = funct.get_todos()
st.set_page_config(layout="wide")

def add_todo():
    todo_local = st.session_state["new_todo"] + "\n"
    todos.append(todo_local)
    funct.write_todos(todos)

st.title("My todo App")

st.subheader("This is my todo app. ")
st.write("This app is to increase your <b>productivity</b>.",
        unsafe_allow_html=True)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        funct.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo ", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")

#st.session_state