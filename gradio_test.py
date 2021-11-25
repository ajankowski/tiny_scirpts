import gradio as gr

def hi_gradio(name, number):
    return f'hi {name} from gradio {number**2}'

iface = gr.Interface(fn=hi_gradio, 
                     inputs=['text','number'], 
                     outputs='text', 
                     interpretation="default", 
                     examples=[["marek", 72], ['zdzislaw', 277]])

iface.launch(debug=True)
