import gradio as gr
import random
import time
import config
from lab_gpt4_call import *
 
functions = [
    {
        "name": "ask_database",
        "description": "Use this function to answer user questions about sales analysis",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "SQL query extracting info to answer the user's question. Do not include comments in SQL."
                },
                "chart_type": {
                    "type": "string",
                    "description": " Suitable chart types for displaying this data, such as bar, line, and pie."
                }
            },
            "required": ["query", "chart_type"],
        },
    },
]
examples = '   \n'.join(["订单平均单价最高的客户", "尾款最多的客户", "客户平均毛利，降序排列", "卖得最好的产品"])

"""
def respond(message, chat_history):
    current_mess = {"role": "user", "content": message}
    llm_mess.append(current_mess)
    llm_mess = send_chat_request_Azure(llm_mess, config.sys_text2, config.openai_key, config.api_base, config.engine, functions)
    bot_message = llm_mess[-1]
    chat_history.append((message, bot_message))
    return "", chat_history
"""

with gr.Blocks() as demo:
    hi = gr.Markdown(
        """ 
        # Hello !!!!  
        A powerful AI system connects humans and data.   
        试试这些问题:   
        订单平均单价最高的客户  
        """)
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    llm_mess = gr.State(value=[])

    """
    def respond(message, chat_history):
        bot_message = random.choice(["How are you?", "I love you", "I'm very hungry"])
        chat_history.append((message, bot_message))
        time.sleep(2)
        return "", chat_history
    """
    def respond(message, chat_history, llm_mess):
        current_mess = {"role": "user", "content": message}
        llm_mess.append(current_mess)
        llm_mess, img_fn = send_chat_request_Azure(llm_mess, config.sys_text3, config.openai_key, config.api_base, config.engine, functions)
        bot_message = llm_mess[-1]["content"]
        chat_history.append((message, bot_message))
        if img_fn is not None:
            chat_history.append((None, (img_fn, )))
        llm_mess = gr.State(value=llm_mess)
        return "", chat_history

    msg.submit(respond, [msg, chatbot, llm_mess], [msg, chatbot])

demo.launch()

