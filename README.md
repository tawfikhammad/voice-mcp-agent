# voice-mcp-agent

A LiveKit voice agent wired to an MCP server.

This project contains two main components:

- `livekit-voice-agent/` — a LiveKit agent that uses STT, an LLM, TTS, VAD and turn-detection to act as a voice assistant.
- `mcp-server/` — a tiny MCP server (tools) the agent can call via HTTP.

## Quick overview

When you run the agent (`livekit-voice-agent/agent.py`) it starts a LiveKit worker which will join rooms when LiveKit dispatches jobs. The agent configures a pipeline:

- STT: Azure Speech-to-Text (configured for Arabic `ar-SA` in the example)
- LLM: Google Gemini (config in the example uses `gemini-2.0-flash-exp`)
- TTS: Azure Text-to-Speech
- VAD / turn detection: Silero and a multilingual turn detector
- MCP: The agent connects to an MCP server at `http://127.0.0.1:8000` to expose/call tools.

## Requirements

- Python 3.10+
- (Recommended) create a virtual environment for the project
- Network access for Azure cloud providers.

## Setup (Windows / PowerShell)

1. Create and activate a virtual environment:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies for each subproject. The repo uses per-package `pyproject.toml`. From the repo root you can install the packages in editable mode:

```powershell
py -m pip install -e .\livekit-voice-agent
py -m pip install -e .\mcp-server
```

3. Create a `.env` file in `livekit-voice-agent/` with the secrets your agent needs that the same in `.env.example`.

## Running the MCP server

Start the MCP server before starting the agent so the agent can initialize its MCP client.

```powershell
py .\mcp-server\main.py
```

This runs the `FastMCP` server defined in `mcp-server/main.py`. The example agent expects the MCP server to be reachable at `http://127.0.0.1:8000` (see `livekit-voice-agent/agent.py`). If you run the server on a different host/port, update the URL in the agent code.

## Running the LiveKit agent

In another terminal:

```powershell
py .\livekit-voice-agent\agent.py
```
