from langchain_community.llms.ollama import Ollama

from tools.utils import remove_emojis,word_match
from tools.config import ollama_url

#Initialize Llama to summerize article
llm_sum = Ollama(model='llama3.2:3b', base_url=ollama_url, verbose=True, temperature=0)
#Initialize Llama to analyze article
llm_ana = Ollama(model='llama3.2:3b', base_url=ollama_url, verbose=True, temperature=0,num_predict=20)

def ollama_gen(text: str) -> str:
    messages=[
    {
        'role': 'system',
        'content': "Our company is a cloud native company that treats High quantity of data for their customers and seek to have a better optimized cloud infrastructure which is currently on Azure. We have multiple application running with kubernetes clusters, we use terraform for IaC, and our app are Next.js and Micronaut. You are a analyst searching for emerging technologies and trends around cloud infrastructure in articles, presenting your findings to the architecture team. Making informed decisions to keep the company's architecture team competitive and aligned with industry advancements.",
    },
    {
        'role': 'user',
        'content': f"Find out if this article is essential for our core infrastructure and could improve our strategy. \nRespond by (Low,Morerate,High-Moderate,High Priority):\n{text}",
    },
    ]
    response = llm_ana.invoke(messages)
    return response

def ollama_sum(text: str) -> str:
    messages=[
    {
        'role': 'system',
        'content': "Our company is a cloud native company that treats High quantity of data for their customers and seek to have a better optimized cloud infrastructure which is currently on Azure. We have multiple application running with kubernetes clusters, we use terraform for IaC, and our app are Next.js and Micronaut. You are a analyst searching for emerging technologies and trends around cloud infrastructure in articles, presenting your findings to the architecture team. Making informed decisions to keep the company's architecture team competitive and aligned with industry advancements.",
    },
    {
        'role': 'user',
        'content': f"Make a resume of this article showing key parts of it:\n{text}",
    },
    ]
    response = llm_sum.invoke(messages)
    return response

def analyze_relevance(article_text):
    text = remove_emojis(article_text)
    matched_categories = word_match(text)
    resume = ollama_sum(article_text)
    output = ollama_gen(article_text)
    return (output,resume,matched_categories)
