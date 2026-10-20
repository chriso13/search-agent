from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from search_agent.source import AgentResponse



llm = ChatOpenAI(model="gpt-5")
tools =[TavilySearch()]
agent = create_agent(model=llm,tools=tools, response_format=AgentResponse)

def main() -> None:
    print("Hello from search-agent!")
    result = agent.invoke({"messages":HumanMessage(content="Search for 3  job postings an java developer for USA at any city  remote/ onsite/hybrid roles okay  don't have more than 7 days in the area on indeed or likedin and list the details")})
    print(result)



if __name__ == "__main__":
    main()
