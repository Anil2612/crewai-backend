from crewai import Agent

def create_writer_agent():
    return Agent(
        role='Content Writer',
        goal='Write engaging blog posts based on provided research',
        backstory='A creative writer who turns facts into compelling stories.',
        verbose=True,
        llm='huggingface/gpt2'
    )
