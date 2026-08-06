package main

// import "fmt"

import (
	"github.com/gin-gonic/gin"
	"net/http"
	"sync/atomic"
    "github.com/Shanu529/atla-voice-agent/services/gateway/internal/middlewares"
)

func main() {
	r := gin.New()

	var isReady atomic.Bool
    isReady.Store(true)

    r.Use(middlewares.Logger())
    r.Use(gin.Recovery())

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

	r.Run(":8080")
}
