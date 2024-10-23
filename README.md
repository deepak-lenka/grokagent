# GrokAgent Multi-Agent Playground

## Overview

GrokAgent is a Multi-Agent System that provides various specialized agents to assist with tasks ranging from web searches and financial analysis to weather updates and joke delivery. using the **Grok-Beta** model for accurate responses.

## Features

- **Web Search Agent**: Fetches and summarizes information from the web.
- **Finance Agent**: Provides real-time stock prices and financial analysis.
- **YouTube Agent**: Analyzes and extracts information from YouTube videos.
- **Joke Agent**: Delivers family-friendly jokes.
- **Weather Agent**: Retrieves real-time weather data.
- **CEO Agent**: Offers insights on technical leadership and current scientific research.

## Table of Contents

- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Customization](#customization)
- [Future Enhancements](#future-enhancements)
- [License](#license)
- [Contributing](#contributing)

## Setup Instructions

### Prerequisites

- **Python 3.7+**
- **pip** (Python package installer)

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/deepak-lenka/grokagent.git
   cd grokagent
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/MacOS
   venv\Scripts\activate      # For Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install openai duckduckgo-search yfinance pypdf sqlalchemy 'fastapi[standard]' youtube-transcript-api phidata
   ```

4. **Set up the SQLite database**: The required database files will be created automatically when the application is run.

## Running the Application

To start the playground, run the following command:
```bash
python grok_agents.py
```

You can then access the playground at `http://localhost:7777`.

## Usage

- **Web Agent**: Ask any general question, and the agent will fetch relevant information from the web.
- **Finance Agent**: Inquire about stock prices, financial news, or analyst recommendations.
- **YouTube Agent**: Provide a YouTube video link and ask questions based on the video content.
- **Joke Agent**: Request a joke for some light-hearted humor.
- **Weather Agent**: Ask for the current weather or forecast for a specific location.
- **CEO Agent**: Pose technical questions related to software engineering, physics, or business strategies.

## Customization

### Adding New Agents

To create a new agent, extend the `Agent` class and define the agent's role, tools, and instructions. For example:
```python
new_agent = Agent(
    name="New Agent",
    role="Performs specialized tasks",
    agent_id="new-agent",
    model=xAI(id="grok-beta"),
    tools=[...],  # Add specific tools here
    instructions=[...],  # Define precise instructions
    storage=SqlAgentStorage(table_name="new_agent", db_file=xai_agent_storage),
)
```

### Customizing Agent Instructions

You can modify the `instructions` attribute of any agent to change its behavior and response patterns.

## Future Enhancements

- Support for more specialized agents covering areas like health, education, or entertainment.
- Integration with additional APIs for enhanced functionality (e.g., Google Search, Wolfram Alpha).
- Improved storage options, including support for more robust databases or cloud-based solutions.
- Implement agent collaboration for complex tasks requiring input from multiple agents.

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for any suggestions or improvements.
