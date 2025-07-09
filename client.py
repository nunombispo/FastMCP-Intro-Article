import asyncio
from fastmcp import Client

# Create a new client
client = Client("server.py")

# Call the tool
async def call_tool(name: str):
    async with client:
        result = await client.call_tool("greet", {"name": name})
        print(result)

# Run the client asynchronously
asyncio.run(call_tool("Ford"))