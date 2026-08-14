package clients
import (
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

func (a *AgentClient) Hello(ctx context.Context) ([]byte, int, error) {

	url := fmt.Sprintf("%s/hello", a.baseURL)

	req, err := http.NewRequestWithContext(
		ctx,
		http.MethodGet,
		url,
		nil,
	)

	if err != nil {
		return nil, 0, err
	}

	resp, err := a.httpClient.Do(req)

	if err != nil {
		return nil, 0, err
	}

	defer resp.Body.Close()

	body, err := io.ReadAll(resp.Body)

	if err != nil {
		return nil, 0, err
	}

	return body, resp.StatusCode, nil
}