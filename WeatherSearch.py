# 定义模型
import json

from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

model = ChatOpenAI(
    model="kimi-k2.5",
    base_url="https://api.moonshot.cn/v1",
    reasoning_effort=None,
    timeout=30,
    max_retries=1,
)

# 定义工具
tool = TavilySearch(max_results=4)

# 绑定工具
model_with_tools = model.bind_tools(tools=[tool], tool_choice="auto")

# 定义消息列表
messages = [
    HumanMessage("北京今天的天气怎么样？")
]
ai_message = model_with_tools.invoke(messages)
search_results = []
for tool_call in ai_message.tool_calls:
    # TavilySearch 需要传入 tool_call 中的 args
    tool_result = tool.invoke(tool_call["args"])
    search_results.append(tool_result)

if ai_message.tool_calls:
    # Moonshot 在工具二次回传链路上可能报 400，这里改为两阶段稳妥方案
    final_prompt = (
        "你是一名天气助手。请根据以下 Tavily 检索结果回答用户问题，"
        "先给结论，再给 3 条出行建议。\n\n"
        f"用户问题: {messages[0].content}\n\n"
        f"检索结果(JSON): {json.dumps(search_results, ensure_ascii=False)}"
    )
    final = model.invoke([HumanMessage(final_prompt)])
    print(final.content)
else:
    # 没有触发工具时直接输出首轮回答，避免额外等待
    print(ai_message.content)