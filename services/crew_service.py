from crewai import Crew
from agents.research_agent import create_research_agent
from agents.writer_agent import create_writer_agent
from tasks.research_task import research_task
from tasks.writing_task import writing_task

def run_research_and_writing(topic):
    research_agent = create_research_agent()
    writer_agent = create_writer_agent()

    research = research_task(research_agent, topic)
    writing = writing_task(writer_agent, research)  # Pass result of research

    crew = Crew(
        agents=[research_agent, writer_agent],
        tasks=[research, writing],
        verbose=True
    )

    results = crew.kickoff()
    return results
