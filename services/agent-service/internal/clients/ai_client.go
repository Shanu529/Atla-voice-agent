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

// chat send to ai engine service and get the response

func (c *AIClient) Chat(ctx context.Context, body []byte) ([]byte, int, error) {
	url := fmt.Sprintf("%s/chat", c.baseURL)

	req, err := http.NewRequestWithContext(ctx, http.MethodPost, url, bytes.NewReader(body))
	if err != nil {
		return nil, 0, fmt.Errorf("failed to create request: %w", err)
	}

	req.Header.Set(
		"Content-Type",
		"application/json",
	)

	resp, err := c.httpClient.Do(req)

	if err != nil {
		return nil, 0, fmt.Errorf("failed to send request: %w", err)
	}

	defer resp.Body.Close()

	responseBody, err := io.ReadAll(resp.Body)

	if err != nil{
		return nil, 0, fmt.Errorf("failed to read response body: %w", err)	
	}
	return responseBody, resp.StatusCode, nil
}