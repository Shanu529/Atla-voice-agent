package handlers

import (
	"net/http"

	"github.com/Shanu529/atla-voice-agent/services/agent-service/internal/models"
	"github.com/Shanu529/atla-voice-agent/services/agent-service/internal/services"
	"github.com/gin-gonic/gin"
)

type AgentHandler struct {
	agentService *services.AgentService
}

func NewAgentHandler(
	agentService *services.AgentService,
) *AgentHandler {
	return &AgentHandler{
		agentService: agentService,
	}
}

// Chat handles the user's chat request.
func (h *AgentHandler) Chat(c *gin.Context) {

	var request models.ChatRequest

	// Convert incoming JSON into ChatRequest.
	if err := c.ShouldBindJSON(&request); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{
			"error": "message is required",
		})
		return
	}

	// Send the request to the Agent Service.
	response, err := h.agentService.Chat(
		c.Request.Context(),
		request,
	)

	if err != nil {
		c.JSON(http.StatusBadGateway, gin.H{
			"error": "AI engine unavailable",
		})
		return
	}

	// Return the response.
	c.JSON(http.StatusOK, response)
}