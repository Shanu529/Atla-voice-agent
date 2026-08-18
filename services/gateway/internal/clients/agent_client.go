package clients

import (
	"bytes"
	"context"
	"fmt"
	"io"
	"net/http"
	"time"
)

type AgentClient struct {
	baseURL    string
	httpClient *http.Client
}

func NewAgentClient(baseURL string) *AgentClient {
	return &AgentClient{
		baseURL: baseURL,
		httpClient: &http.Client{
			Timeout: 5 * time.Second,
		},
	}
}

// Chat sends the user's chat request
// to the Agent Service and returns its response.
func (a *AgentClient) Chat(
	ctx context.Context,
	body []byte,
) ([]byte, int, error) {

	// Agent's real chat endpoint.
	url := fmt.Sprintf("%s/chat", a.baseURL)

	// Create POST request with the user's
	// JSON body.
	req, err := http.NewRequestWithContext(
		ctx,
		http.MethodPost,
		url,
		bytes.NewReader(body),
	)

	if err != nil {
		return nil, 0, err
	}

	// Tell Agent that we're sending JSON.
	req.Header.Set(
		"Content-Type",
		"application/json",
	)

	// Send request to Agent Service.
	resp, err := a.httpClient.Do(req)

	if err != nil {
		return nil, 0, err
	}

	defer resp.Body.Close()

	// Read Agent's response.
	responseBody, err := io.ReadAll(resp.Body)

	if err != nil {
		return nil, 0, err
	}

	return responseBody, resp.StatusCode, nil
}