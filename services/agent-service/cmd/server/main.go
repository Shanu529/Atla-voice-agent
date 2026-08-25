

package main

import (
	"github.com/Shanu529/atla-voice-agent/services/agent-service/internal/clients"
	"github.com/Shanu529/atla-voice-agent/services/agent-service/internal/handlers"
	"github.com/Shanu529/atla-voice-agent/services/agent-service/internal/services"
	"github.com/gin-gonic/gin"
)

func main() {

	r := gin.New()

	// Recover from unexpected panics
	// instead of crashing the server.

	r.Use(gin.Recovery())


	
	// CREATE AGENT CLIENT

	aiClient := clients.NewAIClient(
		"http://localhost:8000",
	)

	// create agent serviec to communicate with ai engine
	agentService := services.NewAgentService(
		aiClient,
	)

	// CREATE AGENT HANDLER
	agentHandler := handlers.NewAgentHandler(
		agentService,
	)
	
	r.POST("/chat", agentHandler.Chat)


	r.Run(":8081")
}
