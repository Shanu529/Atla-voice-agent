package middlewares

import (
	"log";
	"time";
	"github.com/gin-gonic/gin";
)

func Logger() gin.HandlerFunc {
	return func(c *gin.Context){
		start := time.Now();
		
		log.Println("Request received: ", c.Request.Method, " ", c.Request.URL.Path);

		c.Next();
		
		log.Println("time", time.Since(start))

	}
}

