from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("voice-mcp-agent")

# Add an user_info tool
@mcp.tool()
def user_info(name: str, age: int) -> str:
    """Return user information"""
    return f"User {name} is {age} years old and lives in Saudi Arabia."

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
