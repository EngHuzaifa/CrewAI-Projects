from crewai import Agent, Crew, Process, Task,LLM
from crewai.project import CrewBase, agent, task, crew
from crewai_tools import SerperDevTool


deepseek_llm=LLM(model="ollama/deepseek-r1:1.5b",base_url="http://localhost:11434")

@CrewBase
class JobMarketResearchCrew():
    """Job Market Research Crew"""

    @agent
    def researcher(self) -> Agent:
        return Agent(
            role="Job Market Researcher",
            goal="Gather current job market trends and in-demand skills for 2025",
            backstory=
                "You are an expert career analyst with a knack for finding the latest job "
                "market insights using online resources."
            ,
            tools=[SerperDevTool()],
            verbose=True
        )

    @agent
    def report_writer(self) -> Agent:
        return Agent(
            role="Job Market Report Writer",
            goal="Create a concise, structured report based on job market research",
            backstory=
                "You are a skilled writer specializing in turning complex data into "
                "clear, actionable reports for job seekers."
            ,
            verbose=True,
            llm=deepseek_llm
        )


    @task
    def research_task(self) -> Task:
        return Task(
            description=
                "{topic} Conduct thorough research on job market trends and in-demand skills for 2025. "
                "Focus on technology, healthcare, and remote work sectors."
            ,
            expected_output=
                "A list of 8-10 key findings about job trends and skills in bullet-point format."
            ,
            agent=self.researcher(),
           
        )

    @task
    def report_task(self) -> Task:
        return Task(
            description=
                "Using the research findings, create a concise report summarizing job market "
                "trends and skills for 2025. Include an introduction and actionable advice."
            ,
            expected_output=
                "A markdown-formatted report with an introduction, key trends section, "
                "and advice for job seekers."
            ,
          
            output_file='output/job_market_report.md',
            agent=self.report_writer(),
        )

    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
