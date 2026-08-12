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

func (h *AgentHandler) Hello(c *gin.Context) {

	body, statusCode, err := h.agentClient.Hello(c.Request.Context())

	if err != nil {
		c.JSON(http.StatusBadGateway, gin.H{
			"error": "Agent service unavailable",
		})
		return
	}

	c.Data(
		statusCode,
		"application/json",
		body,
	)
}