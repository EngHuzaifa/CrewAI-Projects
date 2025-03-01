# AI Trip Planner

An AI-powered trip planning application that uses CrewAI to help plan your perfect trip. The application uses multiple AI agents working together to research destinations, create itineraries, manage budgets, and find accommodations.

## Features

- 🌍 Destination research based on your preferences
- 📅 Detailed day-by-day itinerary planning
- 💰 Comprehensive budget breakdown
- 🏨 Accommodation recommendations
- 🎨 Beautiful Streamlit interface

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/trip-planner-agent.git
cd trip-planner-agent
```

2. Install the package in development mode:
```bash
pip install -e .
```

## Usage

There are two ways to run the application:

1. Using the installed script:
```bash
trip-planner
```

2. Using Streamlit directly:
```bash
streamlit run streamlit_app.py
```

## Project Structure

```
trip-planner-agent/
├── src/
│   └── trip_planner_agent/
│       ├── app.py              # Streamlit interface
│       └── crews/
│           ├── main.py         # Main flow definition
│           └── trip_crew.py    # CrewAI agents and tasks
├── pyproject.toml             # Project configuration
├── README.md                  # This file
└── streamlit_app.py          # Entry point for Streamlit
```

## Development

To install development dependencies:
```bash
pip install -e ".[dev]"
```

## License

MIT License
