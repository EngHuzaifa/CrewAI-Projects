# src/trip_planner_agent/crews/main.py
from crewai.flow import Flow, start
from job_market_research.crews.crew import JobMarketResearchCrew

class JobMarketResearchCrewflow(Flow):
    @start()
    def run_job_crew(self, inputs=None):
        if inputs is None:
            inputs = {
                "topic": " what is the job market for Agentic AI Engineer in the US?"
                  
                
            }
        
        output = JobMarketResearchCrew().crew().kickoff(inputs=inputs)
        return output


def flow_run():
    job_flow =JobMarketResearchCrewflow()
    result = job_flow.kickoff()
    return result

if __name__ == "__main__":
    run_result = flow_run()
    print("Flow Execution Result:")
    print(run_result)

