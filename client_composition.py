import asyncio
import json
from fastmcp import Client

# Create a new client
client = Client("server_composition.py")

# Call the tool
async def call_tools():
    async with client:
        # Get the product
        product = await client.call_tool("get_product", {"product_id": 42})
        product = product.data
        # Apply the discount
        discounted = await client.call_tool("apply_discount", {"price": product["price"], "percent": 15})
        discounted = discounted.data
        # Format the message
        message = await client.call_tool("format_message", {"name": product["name"], "final_price": discounted})
        message = message.data
        print(message)

# Run the client asynchronously
asyncio.run(call_tools())