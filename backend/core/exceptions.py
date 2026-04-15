class IkmanAgentError(Exception):
    """Base exception. All agent errors inherit from this."""

    def __init__(self, message: str, details: dict | None = None):
        super().__init__(message)
        self.details = details or {}


class LLMError(IkmanAgentError):
    """LLM call failed — rate limit, network, or model error."""


class ToolError(IkmanAgentError):
    """A tool execution failed."""

    def __init__(self, tool_name: str, message: str, details: dict | None = None):
        super().__init__(f"Tool {tool_name!r} failed: {message}", details)
        self.tool_name = tool_name


class ScrapingError(ToolError):
    """ikman.lk scraping failed — page structure changed or rate limited."""


class WhatsAppError(ToolError):
    """WhatsApp Web automation failed."""


class AgentError(IkmanAgentError):
    """Agent-level failure — max iterations exceeded, no valid action, etc."""

    def __init__(self, agent_name: str, message: str, details: dict | None = None):
        super().__init__(f"Agent {agent_name!r}: {message}", details)
        self.agent_name = agent_name


class ConfigurationError(IkmanAgentError):
    """Missing or invalid configuration."""

