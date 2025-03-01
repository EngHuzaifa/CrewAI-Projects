import sys
import os

# Add the src directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from trip_planner_agent.app import main

if __name__ == "__main__":
    main()