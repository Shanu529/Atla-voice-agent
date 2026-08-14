package main

import (
	"github.com/Shanu529/atla-voice-agent/services/gateway/internal/clients"
	"github.com/Shanu529/atla-voice-agent/services/gateway/internal/handlers"
	"github.com/Shanu529/atla-voice-agent/services/gateway/internal/middlewares"
	"github.com/gin-gonic/gin"
	"github.com/Shanu529/atla-voice-agent/services/gateway/internal/config"
)

func main() {

	// its gin router instance
	r := gin.New()

	r.Use(gin.Recovery())
	r.Use(middlewares.Logger())

	cfg := config.Load()

	// create agent client to communicate with agent service
	agentClient := clients.NewAgentClient(
		cfg.AgentServiceURL,
	)

	// create agent handler to hande requests from gateway to agent service
	agentHandler := handlers.NewAgentHandler(
		agentClient,
	)

	r.GET(
		"/api/agent/hello",
		agentHandler.Hello,
	)
	
	r.Run(":8080")
}