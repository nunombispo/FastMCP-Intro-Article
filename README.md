# FastMCP Introduction Article

This repository contains examples demonstrating how to use FastMCP (Model Context Protocol) for creating MCP servers and clients. The project includes both simple and composition examples to showcase different use cases.

## What is FastMCP?

FastMCP is a Python library that simplifies the creation of MCP (Model Context Protocol) servers and clients. MCP allows AI models to interact with external tools and data sources through a standardized protocol.

## Project Structure

```
FastMCP-Intro-Article/
├── client.py              # Simple client example
├── server.py              # Simple server example
├── client_composition.py  # Composition client example
├── server_composition.py  # Composition server example
├── requirements.txt       # Python dependencies
└── README.md            # This file
```

## Examples

### 1. Simple Example

**Server (`server.py`)**

- Creates a basic MCP server with a single `greet` tool
- The tool takes a name parameter and returns a greeting message

**Client (`client.py`)**

- Connects to the server and calls the `greet` tool
- Demonstrates basic client-server communication

### 2. Composition Example

**Server (`server_composition.py`)**

- Implements a pricing system with three tools:
  - `get_product`: Retrieves product information
  - `apply_discount`: Calculates discounted prices
  - `format_message`: Formats the final output message

**Client (`client_composition.py`)**

- Demonstrates tool composition by chaining multiple tool calls
- Shows how to use the output of one tool as input for another

## Installation

1. Clone this repository:

```bash
git clone <repository-url>
cd FastMCP-Intro-Article
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Running the Simple Example

1. Start the server in one terminal:

```bash
python server.py
```

2. Run the client in another terminal:

```bash
python client.py
```

Expected output:

```
Hello, Ford!
```

### Running the Composition Example

1. Start the composition server in one terminal:

```bash
python server_composition.py
```

2. Run the composition client in another terminal:

```bash
python client_composition.py
```

Expected output:

```
The product 'Headphones' is available for $102.0.
```

## Key Features Demonstrated

- **Simple Tool Creation**: How to create basic MCP tools with FastMCP
- **Client-Server Communication**: How clients connect to and interact with MCP servers
- **Tool Composition**: How to chain multiple tool calls together
- **Async/Await Pattern**: Proper handling of asynchronous operations
- **Type Safety**: Using type hints for better code clarity

## Dependencies

- `fastmcp`: The main FastMCP library for creating MCP servers and clients

## Learning Resources

- [FastMCP Documentation](https://fastmcp.com)
- [Model Context Protocol Specification](https://modelcontextprotocol.io)

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the [MIT License](LICENSE).
