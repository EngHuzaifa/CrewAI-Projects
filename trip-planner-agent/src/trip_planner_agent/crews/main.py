# src/trip_planner_agent/crews/main.py
from crewai.flow import Flow, start
from trip_planner_agent.crews.trip_crew import TripCrew

class TripPlannerFlow(Flow):
    @start()
    def run_trip_crew(self, inputs=None):
        if inputs is None:
            inputs = {
                "travel_prefs": """
                    - Duration: 3 days
                    - Budget: $200
                    - Interests: Beaches, local culture, and food
                    - Travel period: June 2025
                    - Starting location: Lahore,Pakistan
                """
            }
        
        output = TripCrew().crew().kickoff(inputs=inputs)
        return output

def flow_run():
    trip_flow = TripPlannerFlow()
    result = trip_flow.kickoff()
    return result

def flow_plot():
    trip_flow = TripPlannerFlow()
    trip_flow.plot()  # Generates crewai_flow.html
    return "Visualization saved as crewai_flow.html in the current directory"

if __name__ == "__main__":
    run_result = flow_run()
    print("Flow Execution Result:")
    print(run_result)

    plot_result = flow_plot()
    print(plot_result)