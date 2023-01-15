import streamlit as st
import filehandler

todos = filehandler.get_todos("files/todos.txt")


def add_todo():
    new_todo = st.session_state["new_todo"]
    todos.append(new_todo)
    filehandler.write_todos("files/todos.txt", todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This application increases the productivity")

# To run the app - streamlit run webgui.py
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        filehandler.write_todos("files/todos.txt", todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add a new todo..", on_change=add_todo, key="new_todo")
