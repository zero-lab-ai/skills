# Manifest format the checker accepts

Any of:

```json
{"tools": [ {...}, {...} ]}
[ {...}, {...} ]
{"jsonrpc": "2.0", "id": 1, "result": {"tools": [ {...} ]}}
```

Each tool object:

```json
{
  "name": "read_file",
  "description": "Read a file under the project root.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "path": {"type": "string", "description": "Path relative to the project root"}
    },
    "required": ["path"]
  }
}
```

`input_schema` is accepted as an alias for `inputSchema`.

## Getting a manifest

- **Running server, stdio:** send `{"jsonrpc":"2.0","id":1,"method":"tools/list"}`
  on stdin after the initialize handshake and save the response.
- **Running server, HTTP:** POST the same body to the server's MCP endpoint.
- **Source checkout:** find the tool registrations (`@server.tool`,
  `@mcp.tool()`, `server.setRequestHandler(ListToolsRequestSchema, ...)`,
  `tools: [...]`) and transcribe name, description and schema into the shape
  above. Do this by hand or with a short script; do not guess descriptions
  from function names, because the description is what the model reads.
