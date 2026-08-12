package main

import (
	"io"
	"net/http"
	"sync/atomic"

	"github.com/Shanu529/atla-voice-agent/services/gateway/internal/middlewares"
	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.New()

	var isReady atomic.Bool
	isReady.Store(true)

	r.Use(gin.Recovery())
	r.Use(middlewares.Logger())

	// Liveness: is the process alive or not?
	r.GET("/healthy", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{"status": "alive"})
	})

	// Readiness: can we serve traffic?
	r.GET("/readyz", func(c *gin.Context) {
		if !isReady.Load() {
			c.JSON(http.StatusServiceUnavailable, gin.H{"status": "Not Ready"})
		} else {
			c.JSON(http.StatusOK, gin.H{"status": "Ready"})
		}
	})

	// Reverse proxy endpoint to downstream agent
	r.GET("/api/agent/hello", func(c *gin.Context) {
		resp, err := http.Get("http://localhost:8081/hello")
		if err != nil {
			c.JSON(http.StatusBadGateway, gin.H{
				"error": "Agent service unavailable",
			})
			return
		}
		
		defer resp.Body.Close()

		body, err := io.ReadAll(resp.Body)
		if err != nil {
			c.JSON(http.StatusBadGateway, gin.H{
				"error": "Failed to read agent response",
			})
			return
		}

		c.Data(
			resp.StatusCode,
			"application/json",
			body,
		)
	})

	r.Run(":8080")
}
