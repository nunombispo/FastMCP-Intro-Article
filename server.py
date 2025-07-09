from fastmcp import FastMCP

# Create a new MCP server
mcp = FastMCP("My MCP Server")

# Create a new tool
@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Run the server
if __name__ == "__main__":
    mcp.run()