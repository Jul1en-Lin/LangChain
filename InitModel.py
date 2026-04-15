from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser

# 1. 基本用法

# LangChain 封装了更上层的方法，让我们初始化模型
# gpt_model = init_chat_model(model="gpt-4o-mini", model_provider="openai", temperature=0.3)
# deepseek_model = init_chat_model("deepseek-chat", model_provider="deepseek", temperature=0.3)
# kimi_model = init_chat_model(model="kimi-k2.5", model_provider="openai", base_url="https://api.moonshot.cn/v1")
# print(kimi_model.invoke("我去，你是谁！").content)

# 2. 可配置的模型（默认参数）
# 精简版本
model = init_chat_model(
    model="kimi-k2.5",
    model_provider="openai",
    base_url="https://api.moonshot.cn/v1",
    temperature=1,
    max_tokens=1024,
    # 指定可配置的字段
    configurable_fields=("max_tokens", "model","model_provider"),
    config_prefix="first",
)

messages = [
    SystemMessage(content="请补全一段故事，100个字："),
    HumanMessage(content="姜太公__？")
]

result = model.invoke(
    input = messages,
    config={
        "configurable" : {
            # 最大 token 数
            "first_max_tokens" : 1000,
            "first_model": "moonshot-v1-8k"
        }
    }
)
parser = StrOutputParser()
chain = model | parser
print(chain.invoke(messages))
