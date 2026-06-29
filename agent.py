from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search
from google.adk.agents import SequentialAgent

def basic_addition(a: int, b: int) -> int:
    """
    Adds two integers together.
    """
    return a + b





research_agent = Agent(
    model='gemma-4-26b-a4b-it',
    name='research_agent',
    description='A helpful assistant for research questions.',
    instruction='Uses google_search tool to research user questions.',
    tools=[google_search]
)

writer_agent = Agent(
    model='gemma-4-26b-a4b-it',
    name='writer_agent',
    description='A helpful assistant for writing user questions.',
    instruction='Utilizes the output of research_agent to summarize the research on a topic.'
)

sequential_agent = SequentialAgent(
    name='research_and_write_agent',
    sub_agents=[research_agent, writer_agent],
    description='Researches a topic and writes a summary of the research.'
)

root_agent = Agent(
    model='gemma-4-26b-a4b-it',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
    sub_agents=[sequential_agent]
    #tools=[google_search]
)
