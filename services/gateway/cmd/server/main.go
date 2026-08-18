package main
import (
	"github.com/Shanu529/atla-voice-agent/services/gateway/internal/clients"
	config "github.com/Shanu529/atla-voice-agent/services/gateway/internal/configs"
	"github.com/Shanu529/atla-voice-agent/services/gateway/internal/handlers"
	"github.com/Shanu529/atla-voice-agent/services/gateway/internal/middlewares"
	"github.com/gin-gonic/gin"
)
func main() {

	// Create Gin router.
	r := gin.New()

	r.Use(gin.Recovery())
	r.Use(middlewares.Logger())

	// Load Gateway configuration.
	cfg := config.Load()

	// Create client used to communicate
	// with the Agent Service.

	agentClient := clients.NewAgentClient(
		cfg.AgentServiceURL,
	)

	// Give the Agent Client to the Handler.
	agentHandler := handlers.NewAgentHandler(
		agentClient,
	)

	// Connect HTTP route to Handler.
	r.POST(
		"/api/agent/chat",
		agentHandler.Chat,
	)

	// Start Gateway.
	r.Run(":8080")
}