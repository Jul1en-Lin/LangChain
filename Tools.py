from typing import List, Tuple

from langchain_core.tools import tool, StructuredTool
from pydantic import BaseModel, Field
from typing_extensions import Annotated

# 定义工具 @tool
# 方式一：
# @tool
# def add(a: int, b: int) -> int:
#     """两数相加
#
#     Args:
#         a: 第一个整数
#         b: 第二个整数
#     """
#     return a + b

# 方式二
# class AddInput(BaseModel):
#     """两数相加"""
#
#     a: int = Field(..., description="第一个整数")
#     b: int = Field(..., description="第二个整数")
#
#
# @tool(args_schema=AddInput)
# def add(a: int, b: int) -> int:
#     return a + b

@tool
def add(
        a : Annotated[int, ..., "第一个整数"],
        b : Annotated[int, ..., "第二个整数"],
) -> int:
    """两数相加

    Args:
        a: 第一个整数
        b: 第二个整数
    """
    return a + b

print(add.invoke({"a": 2, "b": 3}))
print(add.name)
print(add.description)
print(add.args)


# 方式一：
# def add(a: int, b: int) -> int:
#     """两数相加"""
#     return a + b
#
# add_tool = StructuredTool.from_function(func=add)


# 方式二：
# class AddInput(BaseModel):
#     a:int = Field(description="第一个整数")
#     b:int = Field(description="第二个整数")
#
#
# def add(a: int, b: int) -> int:
#     return a + b
#
# add_tool = StructuredTool.from_function(
#     func=add,
#     name="ADD",              # 工具名
#     description="两数相加",   # 工具描述
#     args_schema=AddInput,    # 工具参数
# )

# 方式三：
class AddInput(BaseModel):
    a:int = Field(description="第一个整数")
    b:int = Field(description="第二个整数")


def add(a: int, b: int) -> Tuple[str, List[int]]:
    nums = [a, b]
    content = f"{nums}相加的结果是{a + b}"
    return content, nums

add_tool = StructuredTool.from_function(
    func=add,
    name="ADD",              # 工具名
    description="两数相加",   # 工具描述
    args_schema=AddInput,   # 工具参数
    response_format="content_and_artifact"
)

# 模拟大模型调用姿势
print(add_tool.invoke(
        {   "name": "ADD",
            "args": {"a": 3, "b": 4},
            "type": "tool_call",  # 必填
            "id": "111",  # 必填, 用来将工具调用请求和结果关联起来。
        }
    )
)

# print(add_tool.invoke({"a": 2, "b": 5}))
# print(add_tool.name)
# print(add_tool.description)
# print(add_tool.args)