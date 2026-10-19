from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch



llm = ChatOpenAI(model="gpt-5")
tools =[TavilySearch()]
agent = create_agent(model=llm,tools=tools)

def main() -> None:
    print("Hello from search-agent!")
    result = agent.invoke({"messages":HumanMessage(content="find 3  job java developer in florida for me")})
    print(result)



if __name__ == "__main__":
    main()
