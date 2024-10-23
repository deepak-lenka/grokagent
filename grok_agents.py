from phi.agent import Agent
from phi.model.xai import xAI
from phi.playground import Playground, serve_playground_app
from phi.storage.agent.sqlite import SqlAgentStorage
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from phi.tools.youtube_tools import YouTubeTools

# Define the SQLite storage for agents
xai_agent_storage: str = "tmp/xai_agents.db"

# Common instructions for all agents
common_instructions = [
    "Introduce yourself with your name and role when asked.",
    "Provide clear and concise responses.",
    "If unsure, ask the user for more context or clarify the question.",
]

# Web Search Agent using DuckDuckGo
web_agent = Agent(
    name="Web Agent",
    role="Search the web for accurate information",
    agent_id="web-agent",
    model=xAI(id="grok-beta"),
    tools=[DuckDuckGo()],
    instructions=[
        "Use the `duckduckgo_search` or `duckduckgo_news` tools to gather up-to-date and relevant information.",
        "Summarize the key points clearly and concisely.",
        "Always include the sources you used to gather the information in your response.",
        "If you cannot find specific details, provide the closest relevant information.",
    ] + common_instructions,
    storage=SqlAgentStorage(table_name="web_agent", db_file=xai_agent_storage),
    show_tool_calls=True,
    add_history_to_messages=True,
    num_history_responses=2,
    add_name_to_instructions=True,
    add_datetime_to_instructions=True,
    markdown=True,
)

# Finance Agent using YFinanceTools
finance_agent = Agent(
    name="Finance Agent",
    role="Provide financial data and analysis",
    agent_id="finance-agent",
    model=xAI(id="grok-beta"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    description="You provide financial data and help users make informed investment decisions.",
    instructions=[
        "Always provide current and accurate stock prices when asked.",
        "Use tables to present stock prices, recommendations, or financial data clearly.",
        "Summarize analyst recommendations and any important news related to the requested stock.",
        "If you don’t have relevant data, suggest other stocks or related financial info.",
    ] + common_instructions,
    storage=SqlAgentStorage(table_name="finance_agent", db_file=xai_agent_storage),
    show_tool_calls=True,
    add_history_to_messages=True,
    num_history_responses=5,
    add_name_to_instructions=True,
    add_datetime_to_instructions=True,
    markdown=True,
)

# YouTube Agent for understanding YouTube videos
youtube_agent = Agent(
    name="YouTube Agent",
    role="Analyze YouTube videos and answer questions based on their content",
    agent_id="youtube-agent",
    model=xAI(id="grok-beta"),
    tools=[YouTubeTools()],
    description="You analyze YouTube videos and answer user questions based on video content.",
    instructions=[
        "Use the `get_youtube_video_data` tool to extract video details such as title, description, and metadata.",
        "Extract captions using the `get_youtube_video_data` tool to understand the content of the video.",
        "Summarize the video’s main points clearly, and answer the user's questions based on the video content.",
        "Focus on providing answers based on factual content from the video and avoid assumptions.",
        "If the video lacks necessary details, ask the user for clarification or another video.",
    ] + common_instructions,
    storage=SqlAgentStorage(table_name="youtube_agent", db_file=xai_agent_storage),
    show_tool_calls=True,
    add_history_to_messages=True,
    num_history_responses=5,
    add_name_to_instructions=True,
    add_datetime_to_instructions=True,
    markdown=True,
)

# Joke Agent for humor generation
joke_agent = Agent(
    name="Joke Agent",
    role="Tell light-hearted, funny jokes",
    agent_id="joke-agent",
    model=xAI(id="grok-beta"),
    tools=[],
    description="You tell jokes and make light-hearted, humorous responses.",
    instructions=[
        "When asked for a joke, provide a brief, family-friendly joke or pun.",
        "Keep the jokes simple and suitable for all ages.",
        "Avoid offensive or inappropriate content at all times.",
    ] + common_instructions,
    storage=SqlAgentStorage(table_name="joke_agent", db_file=xai_agent_storage),
    show_tool_calls=True,
    add_history_to_messages=True,
    num_history_responses=2,
    add_name_to_instructions=True,
    add_datetime_to_instructions=True,
    markdown=True,
)

# Weather Agent for providing weather updates
weather_agent = Agent(
    name="Weather Agent",
    role="Provide real-time weather information and forecasts",
    agent_id="weather-agent",
    model=xAI(id="grok-beta"),
    tools=[DuckDuckGo()],  # Using DuckDuckGo to search for weather reports
    description="You provide up-to-date weather reports and forecasts.",
    instructions=[
        "Search for the most recent weather reports and forecasts using the `duckduckgo_search` tool.",
        "Present the current temperature, weather conditions, and forecast clearly and concisely.",
        "Include the source of the weather information in your response.",
        "If no specific location is given, ask for the city or region to provide accurate weather data.",
    ] + common_instructions,
    storage=SqlAgentStorage(table_name="weather_agent", db_file=xai_agent_storage),
    show_tool_calls=True,
    add_history_to_messages=True,
    num_history_responses=2,
    add_name_to_instructions=True,
    add_datetime_to_instructions=True,
    markdown=True,
)

# CEO Agent for technical leadership, software engineering, physics, and research
ceo_agent = Agent(
    name="CEO Agent",
    role="Provide technical leadership and insights into software engineering, physics, and research",
    agent_id="ceo-agent",
    model=xAI(id="grok-beta"),
    tools=[DuckDuckGo()],  # Using DuckDuckGo to search for latest research papers and news
    description="You are a co-founder and CEO with expertise in software engineering, physics, and research. You can also stay updated with the latest research papers and provide technical leadership.",
    instructions=[
        "Provide strategic and technical insights when asked about software engineering, including best practices, frameworks, and architectural advice.",
        "For physics-related questions, offer clear explanations of complex concepts and suggest up-to-date research or studies.",
        "Use the `duckduckgo_search` tool to find and summarize recent research papers, and highlight the most relevant findings.",
        "Assist with startup advice, leadership strategies, and co-founder-level decisions.",
        "Summarize research papers and scientific advances concisely, focusing on how they impact technology or industry trends.",
        "If unsure of the latest updates, ask the user for clarification or additional context.",
    ] + common_instructions,
    storage=SqlAgentStorage(table_name="ceo_agent", db_file=xai_agent_storage),
    show_tool_calls=True,
    add_history_to_messages=True,
    num_history_responses=5,
    add_name_to_instructions=True,
    add_datetime_to_instructions=True,
    markdown=True,
)

# Add more agents here as needed...

# Define the Playground app with all the agents
app = Playground(agents=[finance_agent, youtube_agent, web_agent, joke_agent, weather_agent, ceo_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("grok_agents:app", reload=True)
