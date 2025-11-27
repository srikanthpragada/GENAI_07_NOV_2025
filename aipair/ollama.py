# Access llama3.2 model using langchain integration with ollama 
# invoke the model with the prompt given by user and display the result 

from langchain.llms import Ollama
def get_ollama_response(prompt: str) -> str:
    llm = Ollama(model="llama3.2")
    response = llm(prompt)
    return response


# call the function with a sample prompt
if __name__ == "__main__":
    sample_prompt = "Explain the theory of relativity in simple terms."
    result = get_ollama_response(sample_prompt)
    print("Ollama Response:")
    print(result)




