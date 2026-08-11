
package main
import (
	"net/http"

	"github.com/Shanu529/atla-voice-agent/services/gateway/internal/middlewares"
	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.New()

	r.Use(gin.Recovery())
	r.Use(middlewares.Logger())

	// create  dummy response from agent service
	r.GET("/hello", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{"message": "Hello, World! from Golang"})
	})

	r.Run(":8081")
}