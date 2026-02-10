"""
CLI entry point for Lenny's Wisdom MCP Server
"""

def main():
    """Run the MCP server"""
    from .server import mcp
    mcp.run()

if __name__ == "__main__":
    main()
