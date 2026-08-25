package services

import (
	"context"
	"encoding/json"
	"fmt"

	"github.com/Shanu529/atla-voice-agent/services/agent-service/internal/clients"
	"github.com/Shanu529/atla-voice-agent/services/agent-service/internal/models"
)

type AgentService struct {
	aiClient *clients.AIClient
}

func NewAgentService(aiClient *clients.AIClient) *AgentService {
	return &AgentService{
		aiClient: aiClient,
	}
}

// Chat sends the user's message to the AI Engine.
func (s *AgentService) Chat(
	ctx context.Context,
	request models.ChatRequest,
) (models.ChatResponse, error) {

	// Convert ChatRequest into JSON.
	requestBody, err := json.Marshal(request)

	if err != nil {
		return models.ChatResponse{}, err
	}

	// Send the request to the Python AI Engine.
	responseBody, statusCode, err := s.aiClient.Chat(
		ctx,
		requestBody,
	)

	if err != nil {
		return models.ChatResponse{}, err
	}

	// AI Engine should return a successful response.
	if statusCode < 200 || statusCode >= 300 {
		return models.ChatResponse{}, fmt.Errorf(
			"AI engine returned status %d",
			statusCode,
		)
	}

	// Convert AI Engine JSON response
	// back into ChatResponse.
	var response models.ChatResponse

	if err := json.Unmarshal(responseBody, &response); err != nil {
		return models.ChatResponse{}, err
	}

	return response, nil
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
