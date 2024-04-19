import gradio as gr

def greet(name):
    return "Hello " + name + "! Welcome to the Hello World App."

gr.Interface(fn=greet, inputs="text", outputs="text").launch()