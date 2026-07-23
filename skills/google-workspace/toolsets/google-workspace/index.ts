export default {
  name: "Google Workspace",
  description:
    "Google Drive, Docs, Sheets, Slides, Gmail, Calendar and Workspace tools exposed through MCP.",
  rules: [
    {
      instruction:
        "Confirm before sending messages, deleting resources, changing permissions, sharing files, or overwriting substantial content.",
    },
  ],
  connection: {
    type: "mcp-server::stdio",
    command: "uvx",
    args: [
      "--from",
      "workspace-mcp==1.22.1",
      "workspace-mcp",
      "--tool-tier",
      "core",
    ],
  },
  tools: [],
};
