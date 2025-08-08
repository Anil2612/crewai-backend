from crewai import Task

def research_task(agent, topic):
    return Task(
        description=f"Research about: {topic}",
        agent=agent,
        expected_output="Detailed research summary with bullet points."
    )
