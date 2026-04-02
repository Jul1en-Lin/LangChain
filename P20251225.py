from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

# 1. 定义OpenAI模型
# model = ChatOpenAI(
#     model="gpt-4o-mini",
#     # temperature=2,       # 采样温度（熵）
#     # max_tokens=10,     # 最大 token 数
#     # timeout=None,      # 超时时间
#     # max_retries=2,     # 最大重试次数
#     # api_key="...",      # 指定 api key
#     # base_url="...",     # 指定前置请求路径
#     # organization="...", # openai 组织 IA
#     # other params...
# )
# model = ChatOpenAI(
#     model="deepseek-chat",
#     api_key="sk-a5b3406086ec4c89832442954c60f210",      # 指定 api key
#     base_url="https://api.deepseek.com/v1",     # 指定前置请求路径
# )

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2
)

# 2. 定义消息
messages = [
    SystemMessage(content="你是一名学习信号与系统专业的大学生，现在需要你完成关于该专业的作业"),
    HumanMessage(content="提供一份思政体会:涉及到与本课程的科学思想方法，科学精神，国家建设中与本课程有关的案例等，要求字数500字左右")
]
print(model.invoke(messages).content)


# # 3. 定义输出解析器组件
# parser = StrOutputParser()
#
# # 4. 定义链
# # 执行链
# chain = model | parser
# print(chain.invoke(messages))





