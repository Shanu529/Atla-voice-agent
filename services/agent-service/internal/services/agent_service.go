package services

// AgentService contains the business logic
// of our AI Agent.
//
// Right now the logic is very simple.
// Later this will contain things like:
//
// - LLM calls
// - Memory
// - Tool execution
// - Planning
// - Agent reasoning

type AgentService struct{}

// NewAgentService creates a new AgentService.
//
// This is called a constructor-style function.
// Go doesn't have a special "constructor" keyword
// like some other languages.

func NewAgentService() *AgentService {
	return &AgentService{} // return a pointer to a new agent servicee instance
}

// Hello contains the actual business logic
// for our first Agent operation.

func (s *AgentService) Hello() string {
	return "Hello from the Agent Service!"
}
