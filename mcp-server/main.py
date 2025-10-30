from mcp.server.fastmcp import FastMCP
from .tools.FAQ_assistant import faq_assistant

mcp = FastMCP("voice-mcp-agent")

mcp.add_tool(faq_assistant)

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
