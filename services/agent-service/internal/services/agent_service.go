package services

import (
	"context"
	"github.com/Shanu529/atla-voice-agent/services/agent-service/internal/clients"
	"github.com/Shanu529/atla-voice-agent/services/agent-service/internal/models"
)

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

// it will contains busness logic of our AI Agent

type AgentService struct {
	aiClient *clients.AIClient
}

// NewAgentService creates a new AgentService.
//
// This is called a constructor-style function.
// Go doesn't have a special "constructor" keyword
// like some other languages.

func NewAgentService(aiClient *clients.AIClient) *AgentService {

	return &AgentService{
		aiClient: aiClient,
	} // return a pointer to a new agent servicee instance
}

// send user's msg to ai engine service and get the response
func (s *AgentService) Chat(ctx context.Context, request models.ChatRequest) (models.ChatResponse, error) {

	// TODO:
	// Convert request to JSON and send it
	// to the AI Engine

	return models.ChatResponse{
		Reply: "Ai Engine not connected yet. Please try again later.",
	}, nil
}



// // Hello contains the actual business logic
// // for our first Agent operation.

// func (s *AgentService) Hello() string {
// 	return "Hello from the Agent Service!"
// }

// func (s *AgentService) Chat( // this is a method of the AgentService struct and chat() it is mehtod beloging it
// 	request models.ChatRequest,
// ) models.ChatResponse {

// 	return models.ChatResponse{
// 		Reply: "Agent received: " + request.Message,
// 	}
// }
