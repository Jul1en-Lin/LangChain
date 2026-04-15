from langchain_ollama import ChatOllama

# 初始化Ollama模型
# Ollama 默认端口为11434
ollama_model = ChatOllama(model="deepseek-r1:14b",
                          base_url="http://127.0.0.1:11434")
print(ollama_model.invoke("你是谁？").content)