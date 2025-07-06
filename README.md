Gemini Python Agent

This project is a Python CLI tool that leverages Google Gemini and function calling to act as an “autonomous agent.”
It can reason through user requests, call tools (functions), and iterate toward solutions—keeping its context across multiple steps.
Features

    Conversational Agent: Uses an LLM to execute tasks, iterating via conversation memory.
    Function Calling: Supports Gemini “tool calls” for advanced code/project manipulation.
    Extensible: Add your own tools/functions in the call_function.py file.
    Environment Configurable: Loads API keys and settings from .env.

Requirements

    Python 3.8+
    Boot.dev coursework materials
    Google Gemini SDK
    An API key for Gemini

Installation

    git clone <your-repo-url>
    cd <your-project-dir>
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

Setup

    Obtain a Gemini API Key and add it to a .env file like so:

    GEMINI_API_KEY=your-key-here

    Any additional configuration (e.g., tool functions) can be set in call_function.py or config.py.

Usage

python main.py "How does the calculator render results to the console?"

Options

    --verbose: Show token counts, step-by-step tool use, and more debug info.

