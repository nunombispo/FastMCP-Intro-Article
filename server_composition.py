from fastmcp import FastMCP

# Create a new MCP server
mcp = FastMCP("PricingTools")

# Step 1: Fake product lookup
@mcp.tool()
def get_product(product_id: int) -> dict:
    return {"id": product_id, "name": "Headphones", "price": 120.0}

# Step 2: Discount calculator
@mcp.tool()
def apply_discount(price: float, percent: float = 10.0) -> float:
    return round(price * (1 - percent / 100), 2)

# Step 3: Formatter
@mcp.tool()
def format_message(name: str, final_price: float) -> str:
    return f"The product '{name}' is available for ${final_price}."

# Run the server
if __name__ == "__main__":
    mcp.run()