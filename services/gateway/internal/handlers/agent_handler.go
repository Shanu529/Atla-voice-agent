package handlers

import (
	"net/http"

	"github.com/Shanu529/atla-voice-agent/services/gateway/internal/clients"
	"github.com/gin-gonic/gin"
)

type AgentHandler struct {
	agentClient *clients.AgentClient
}

func NewAgentHandler(agentClient *clients.AgentClient) *AgentHandler {
	return &AgentHandler{
		agentClient: agentClient,
	}
}

// and forwards it to the Agent Service.
func (h *AgentHandler) Chat(c *gin.Context) {
	responseBody, statusCode, err := h.agentClient.Chat(c.Request.Context())
	if err != nil {
		c.JSON(http.StatusBadGateway, gin.H{
			"error": "agent service unavailable",
		})
		return
	}

	// Return the Agent response to the user.
	c.Data(
		statusCode,
		"application/json",
		responseBody,
	)
}