from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

# LangChain 封装的 ChatOpenAI
model = ChatOpenAI (
    # 由于使用第三方API，故baseurl需要指定，否则会自动匹配到openai
    base_url = "https://api.moonshot.cn/v1",
    model="moonshot-v1-32k"
)

# 2. 定义消息
# 用户消息 HumanMessage
# 系统提示消息 SystemMessage  通常作为第一条消息传入
# AI 消息 AIMessage
messages = [
    SystemMessage(content="你是一个小助手"),
    HumanMessage(content="你是什么模型")
]

# 3. 调用大模型
result = model.invoke(messages)
# print(result.content_blocks)
# print(result.content)

# 链式体现在哪里？？？

# 4. 定义输出解析器组件（将模型输出转换为简单字符串格式）
parser = StrOutputParser()
print(parser.invoke(result))

# 5. 定义链
# 执行链
chain = model | parser
# chain = RunnableSequence(first=model, last=parser)
# chain = model.pipe(parser)
print(chain.invoke(messages))