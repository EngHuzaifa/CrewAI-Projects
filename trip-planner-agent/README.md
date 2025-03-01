# AI Trip Planner 🌍

An intelligent travel planning assistant powered by CrewAI that revolutionizes your trip planning experience. This application orchestrates multiple AI agents working in harmony to create personalized travel experiences, from destination research to detailed itinerary planning.

## ✨ Features

- **Smart Destination Research** - AI-powered analysis of travel destinations based on your preferences and constraints
- **Intelligent Itinerary Creation** - Detailed day-by-day planning that optimizes your time and experiences
- **Budget Management** - Comprehensive budget breakdown and cost optimization suggestions
- **Accommodation Finder** - Personalized lodging recommendations based on your preferences and budget
- **Interactive Interface** - Modern and intuitive Streamlit-based user interface

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or higher
- Git

### Installation

1. Clone the repository:
```bash
git clone https://github.com/EngHuzaifa/trip-planner-agent.git
cd trip-planner-agent
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate
```

3. Install the package in development mode:
```bash
pip install -e .
```

### Environment Setup

Create a `.env` file in the root directory and add your API keys:
```env
GEMINI_API_KEY=your_api_key_here
```


## 🏗️ Project Structure

```
trip-planner-agent/
├── src/
│   └── trip_planner_agent/
│       └── crews/
│           ├── main.py         # Main flow definition
│           └── trip_crew.py    # CrewAI agents and tasks
├── pyproject.toml             # Project configuration
├── README.md                  # Documentation

```

## 🛠️ Technologies

- [CrewAI](https://github.com/joaomdmoura/crewAI) - Multi-agent orchestration framework


## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## ✨ Acknowledgments

- [CrewAI](https://github.com/joaomdmoura/crewAI) for the amazing multi-agent framework
- The open-source community for their invaluable tools and libraries

## 📧 Contact

Muhammad Huzaifa - muhammadhuzaifaai890@gmail.com



