package configs

import "os"

type Config struct {
	AgentServiceURL string
}

func Load() Config {
	agentURL := os.Getenv("AGENT_SERVICE_URL")

	if agentURL == ""{
		agentURL = "http://localhost:8081"
	}

	return Config{
		AgentServiceURL: agentURL,
	}
}
