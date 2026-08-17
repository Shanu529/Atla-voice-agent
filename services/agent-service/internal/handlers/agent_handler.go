package handlers

import (
	"net/http"

	"github.com/Shanu529/atla-voice-agent/services/agent-service/internal/models"
	"github.com/Shanu529/atla-voice-agent/services/agent-service/internal/services"
	"github.com/gin-gonic/gin"
)

// AgentHandler handles HTTP requests
// related to the Agent.

type AgentHandler struct {
	agentService *services.AgentService
}

// NewAgentHandler creates an AgentHandler
// and gives it access to AgentService.

func NewAgentHandler(agentService *services.AgentService) *AgentHandler {
	return &AgentHandler{
		agentService: agentService,
	}
}

// Hello handles:
//
// GET /hello
//
// The handler is responsible for HTTP.
// It calls the service to get the actual
// Agent response.

func (h *AgentHandler) Hello(c *gin.Context) {

	// Ask the service to perform the business logic.
	reply := h.agentService.Hello()

	// send the reply back to the client
	c.JSON(http.StatusOK, gin.H{
		"reply": reply,
	})
}

func (h *AgentHandler) Health(c *gin.Context){

	c.JSON(http.StatusOK, gin.H{
		"status": "ok",
	})
}

func (h *AgentHandler) Chat(c *gin.Context) {
	// create a variable to hold the request data
	var request  models.ChatRequest

	// convert JSON into go Request struct
	if err := c.ShouldBindJSON(&request); err != nil{
		c.JSON(http.StatusBadRequest, gin.H{
			"error": "message is required",
		})

		return
	}

	// Pass the request to the business logic.
	response := h.agentService.Chat(request)

	// return agent response as a json res
	c.JSON(http.StatusOK, response)


}
