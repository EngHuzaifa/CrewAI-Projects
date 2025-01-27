# CrewAI Framework

[![PyPI version](https://badge.fury.io/py/crewai.svg)](https://badge.fury.io/py/crewai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

CrewAI is a cutting-edge framework for orchestrating role-based autonomous AI agents. Built on top of LangChain, it enables AI agents to work together seamlessly, tackling complex tasks through autonomous collaboration.

## 🌟 Features

- **Role-Based Agent Architecture**: Create specialized AI agents with defined roles and goals
- **Autonomous Collaboration**: Agents work together to solve complex tasks without human intervention
- **Flexible Task Management**: Define, assign, and manage tasks dynamically
- **Built-in Tools Integration**: Easy integration with various tools and APIs
- **Process Automation**: Automate complex workflows through agent collaboration
- **Customizable Agent Behaviors**: Fine-tune agent personalities and behaviors for optimal performance

## 🚀 Quick Start

### Installation

```bash
pip install crewai
```

### Basic Usage

```python
from crewai import Agent, Task, Crew
from langchain.llms import OpenAI

# Create agents with specific roles
researcher = Agent(
    role='Research Analyst',
    goal='Conduct comprehensive market research',
    backstory='Experienced market analyst with expertise in data analysis',
    llm=OpenAI()
)

writer = Agent(
    role='Content Writer',
    goal='Create engaging content based on research',
    backstory='Professional writer with expertise in technical communication',
    llm=OpenAI()
)

# Define tasks for the agents
research_task = Task(
    description='Analyze market trends in AI industry',
    agent=researcher
)

writing_task = Task(
    description='Write a market analysis report',
    agent=writer
)

# Create a crew with the agents and tasks
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task]
)

# Execute the tasks
result = crew.kickoff()
```

## 🔧 Configuration

### Environment Variables

```bash
export OPENAI_API_KEY="your-api-key"
```

### Advanced Configuration

```python
from crewai import Agent, Task, Crew
from crewai.tools import Tool

# Create custom tools
custom_tool = Tool(
    name="web_search",
    description="Search the web for information",
    func=your_search_function
)

# Create agent with custom tools
agent = Agent(
    role='Researcher',
    goal='Find specific information',
    tools=[custom_tool],
    llm=OpenAI()
)
```

## 📚 Documentation

For detailed documentation and advanced usage examples, visit our [documentation site](https://docs.crewai.com).

### Key Concepts

- **Agents**: Autonomous AI entities with specific roles and goals
- **Tasks**: Units of work assigned to agents
- **Crews**: Groups of agents working together
- **Tools**: Integrations and capabilities available to agents

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built on top of [LangChain](https://github.com/hwchase17/langchain)
- Inspired by the concept of autonomous AI agents


## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=joaomdmoura/crewai&type=Date)](https://star-history.com/#joaomdmoura/crewai&Date)
