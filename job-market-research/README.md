# Job Market Research 

## Overview
This project is built using **CrewAI**, designed to research job market trends and generate structured reports. It employs **DeepSeek LLM** and **SerperDevTool** to gather insights on the most in-demand skills for 2025 across technology, healthcare, and remote work sectors.

## Features
- **Research Agent:** Gathers up-to-date job market insights.
- **Report Writer Agent:** Summarizes findings into a clear, structured report.
- **DeepSeek LLM Integration:** Enhances report generation using AI-powered natural language processing.
- **SerperDevTool:** Enables real-time web research for accurate job market data.

## Components

### Agents
1. **Researcher**
   - Role: Job Market Researcher
   - Goal: Find and analyze job market trends for 2025
   - Tools: SerperDevTool for web search

2. **Report Writer**
   - Role: Job Market Report Writer
   - Goal: Create a structured and actionable job market trends report
   - Uses **DeepSeek LLM** for AI-powered content generation

### Tasks
1. **Research Task**
   - Conducts in-depth research on job market trends and in-demand skills for 2025.
   - Focus areas: Technology, Healthcare, Remote Work sectors.
   - Produces a bullet-point list of key findings.

2. **Report Task**
   - Summarizes research findings into a structured report.
   - Provides an introduction, key trends, and actionable advice.
   - Saves the output in markdown format.

## Setup and Installation

### Prerequisites
- Python 3.8+
- CrewAI
- Ollama (for DeepSeek LLM)
- Serper API Key (for real-time web search)

### Installation Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/job-market-research-crew.git
   cd job-market-research-crew
   ```
2. Install dependencies:
   ```sh
   pip install crewai
   ```
3. Set up DeepSeek LLM locally:
   ```sh
   ollama pull deepseek-r1:1.5b
   ```
4. Run the project:
   ```sh
   python main.py
   ```

## Model Configuration
The system uses:
- **DeepSeek LLM** (`ollama/deepseek-r1:1.5b`)
- **Google Gemini** (`gemini/gemini-2.0-flash` for high-speed responses)

## Output
The project generates a report in `output/job_market_report.md`, summarizing the latest job market trends and actionable insights.

## Future Improvements
- Adding more AI models for comparison
- Expanding research to more industries
- Enhancing report formatting and visualization

## License
This project is open-source under the MIT License.

## Author
Developed by **Your Name**

