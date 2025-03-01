# trip_planner_agent/crews/trip_crew.py
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class TripCrew:
    """Trip Planner Crew"""
    
    # agents_config = "config/agents.yaml"
    # tasks_config = "config/tasks.yaml"

    @agent
    def destination_researcher(self) -> Agent:
        return Agent(
            role="Destination Researcher",
            goal="Research and recommend travel destinations based on user preferences",
            backstory="You're an expert travel researcher with knowledge of global destinations.",
            verbose=True,
        )

    @agent
    def itinerary_planner(self) -> Agent:
        return Agent(
            role="Itinerary Planner",
            goal="Create detailed daily itineraries for the trip",
            backstory="You're a meticulous planner who crafts perfect travel schedules.",
            verbose=True,
        )

    @agent
    def budget_analyst(self) -> Agent:
        return Agent(
            role="Budget Analyst",
            goal="Manage trip costs and find cost-effective solutions",
            backstory="You're a financial expert specializing in travel budgeting.",
            verbose=True,
        )

    @agent
    def accommodation_specialist(self) -> Agent:
        return Agent(
            role="Accommodation Specialist",
            goal="Find and recommend suitable accommodations",
            backstory="You're an expert in finding the best hotels and lodging options.",
            verbose=True,
        )

    @task
    def destination_researcher_task(self) -> Task:
        return Task(
            description="""Research potential destinations based on these preferences:
            {travel_prefs} Provide 3 destination options with pros and cons for each.""",
            expected_output="A list of 3 destinations with pros and cons",
            agent=self.destination_researcher(),
        )

    @task
    def itinerary_task(self) -> Task:
        return Task(
            description="Create a  itinerary for the chosen destination, including daily activities and timing.",
            expected_output="A detailed  itinerary",
            agent=self.itinerary_planner(),
        )

    @task
    def budget_task(self) -> Task:
        return Task(
            description="Create a budget breakdown for the trip including transportation, accommodation, food, and activities.",
            expected_output="A detailed budget breakdown",
            agent=self.budget_analyst(),
        )

    @task
    def accommodation_task(self) -> Task:
        return Task(
            description="Research and recommend 3 accommodation options for the chosen destination with prices and amenities.",
            expected_output="A list of 3 accommodation options with details",
            agent=self.accommodation_specialist(),
            output_file="output/imp_notes.md"
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Trip Planner crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )