package handlers
import (
	"net/http"

	"github.com/Shanu529/atla-voice-agent/services/agent/internal/services"
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
