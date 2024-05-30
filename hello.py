from llama_index.llms.ollama import Ollama

llm = Ollama(model="mistral", request_timeout=30.0)

result = llm.complete("What is the capital of France?")
print(result)