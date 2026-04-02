import os
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

# # 需要设置代理
# proxy_url = "http://127.0.0.1:7897"
# os.environ["http_proxy"] = proxy_url
# os.environ["https_proxy"] = proxy_url


# 1. 定义Gemini模型
# API_Key 默认读取环境变量配置
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    # 显式设置超时时间，避免无限等待
    request_timeout=20
)
# 2. 定义用户信息

messages = [
    SystemMessage(content = "help me translate this sentence to Chinese"),
    HumanMessage(content = "hi i am Julien,a student from WuYi University")
]

# 3. 调用大模型
# result = model.invoke(messages)
# print(result.content)

# 4. 可以定义输出解析组件
parser = StrOutputParser()
#print(parser.invoke(result))

# 5. 定义链
chain = model | parser
# 执行链 不用手动再调用组件，chain会由上到下调用组件，只需将messages传入
print(chain.invoke(messages))