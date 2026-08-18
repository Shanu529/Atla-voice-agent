package handlers

import (
	"io"
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

// Chat receives the user's chat request
// and forwards it to the Agent Service.
func (h *AgentHandler) Chat(c *gin.Context) {

	// Read the JSON body sent by the user.
	body, err := io.ReadAll(c.Request.Body)

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{
			"error": "invalid request body",
		})
		return
	}

	// Send the user's request to Agent Service.
	responseBody, statusCode, err := h.agentClient.Chat(
		c.Request.Context(),
		body,
	)

	if err != nil {
		c.JSON(http.StatusBadGateway, gin.H{
			"error": "agent service unavailable",
		})
		return
	}

	// Return Agent's response to the user.
	c.Data(
		statusCode,
		"application/json",
		responseBody,
	)
}