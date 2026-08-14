package main


import (
	"github.com/Shanu529/atla-voice-agent/services/agent-service/internal/handlers"
	"github.com/Shanu529/atla-voice-agent/services/agent-service/internal/services"

	"github.com/gin-gonic/gin"
)

func main() {

	r := gin.New()

	// Recover from unexpected panics
	// instead of crashing the server.

	r.Use(gin.Recovery())

	// CREATE AGENT SERVICE
	agentService := services.NewAgentService()

	// CREATE AGENT HANDLER
	agentHandler := handlers.NewAgentHandler(
		agentService,
	)
	r.GET(
		"/hello",
		agentHandler.Hello,
	)

	r.Run(":8081")
}