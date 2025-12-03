import os
from PIL import Image
from google import genai

os.environ["GEMINI_API_KEY"] = "AIzaSyDqNOl9JGZaTPur0VdLJC-R77eSl8zxAyc"

client = genai.Client()
#
# response = client.models.generate_content(
#     model='gemini-2.0-flash',
#     contents='hi'
# )
# print(response.text)
#
# print(response.model_dump_json(
#     exclude_none=True, indent=4))

chat = client.chats.create(model='gemini-2.0-flash')

# response = chat.send_message(
#     message='你是谁？夸夸我吧')

# response = chat.send_message(
#     message='这是我第一次调用SDK~~')
response = chat.send_message(
    message='我很好奇如何将AI模型无缝集成到应用程序、设备或系统中，且它们具体应用的场景都有哪些？'
)

print(response.text)

print(response.model_dump_json(
    exclude_none=True, indent=4))