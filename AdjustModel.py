# 1. 定义OpenAI模型
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from pydantic.v1 import parse_raw_as

model = ChatOpenAI(
    base_url = "https://api.moonshot.cn/v1",
    model = "kimi-k2.5",
    # temperature = 2,       # 采样温度
    # max_tokens = 10,       # 最大 token 数
    # timeout = None,        # 超时时间
    # max_retries = 2,       # 最大重试次数
    # api_key = "...",       # 指定 api key
    # base_url = "...",      # 指定前置请求路径
    # organization = "...",  # openai 组织 ID
    # other params...
)

message = [
    HumanMessage(content="你好，我叫李雷，1+1等于多少？")
]

parser = StrOutputParser()
chain = model | parser
print(chain.invoke(message))