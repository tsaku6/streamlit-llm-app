from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain import LLMChain

st.title("専門家AI相談Webアプリ")

st.write("相談内容を入力し、専門家AIを選択することで回答を引き出せます。")
selected_item = st.radio(
    "動作モードを選択してください。",
    ["親の育児ストレス軽減に詳しい専門家", "子どもの栄養に詳しい専門家"]
)
st.markdown("---")

input_message = st.text_input(label="相談内容を入力してください。")

def result_chain(param, system_template):
    if not param:
        raise ValueError("paramが空です。正しい値を渡してください。")

    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.5)

    prompt = ChatPromptTemplate.from_messages([
        {"role": "system", "content": system_template},
        {"role": "human", "content": "{input_message}"}
    ])

    chain = LLMChain(prompt=prompt, llm=llm)

    result = chain.run({"input_message": param})  # 入力キーを明示的に指定
    return result

def get_childcare_stress_advice(param):
    system_template = """
    あなたは親の育児ストレスを軽減するための専門家です。
    育児疲れやストレス管理に関する実践的なアドバイスを提供します。
    親自身の心身の健康を保つための方法を教えます。
    """
    return result_chain(param, system_template)

def get_childcare_nutrition_advice(param):
    system_template = """
    あなたは子どもの栄養に詳しいアドバイザーです。
    子どもの健康な発育を支える食事や栄養バランスについてアドバイスを提供します。
    食事の習慣や偏食に関する質問にも丁寧に答えます。
    """
    return result_chain(param, system_template)

if st.button("実行"):
    st.markdown("---")

    if selected_item == "親の育児ストレス軽減に詳しい専門家":
        if input_message:
            st.write(get_childcare_stress_advice(input_message))
        else:
            st.error("相談内容を入力してから「実行」ボタンを押してください。")
    elif selected_item == "子どもの栄養に詳しい専門家":
        if input_message:
            st.write(get_childcare_nutrition_advice(input_message))
        else:
            st.error("相談内容を入力してから「実行」ボタンを押してください。")