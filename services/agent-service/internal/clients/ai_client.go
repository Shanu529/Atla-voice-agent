package clients

import (
	"bytes"
	"context"
	"fmt"
	"io"
	"net/http"
	"time"
)

// AIClient will be the communicate client to the ai engine service
type AIClient struct {
	baseURL string
	httpClient *http.Client
}


// newAiclient will create a new ai engine client
func NewAIClient(baseURL string) *AIClient{
	return &AIClient{
		baseURL : baseURL,
		httpClient: &http.Client{
			Timeout: 10 * time.Second,
		},
	}
}