from crewai import Agent


def create_research_agent():
    return Agent(
        role='Market Research Analyst',
        goal='Research given topic and return a detailed report',
        backstory='An expert in market trends and competitor analysis.',
        verbose=True,
        llm='huggingface/bigscience/bloom'
    )
