from crewai import Task

def writing_task(agent, research_summary):
    return Task(
        description=f"Write a blog post based on the research: {research_summary}",
        agent=agent,
        expected_output="A well-written blog article."
    )
