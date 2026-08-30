


from langgraph.graph import END, START, StateGraph

from app.agent import run_agent
from app.state import AgentState


def agent_node(state: AgentState):
    response = run_agent(state["message"])

    return {
        "response": response
    }


builder = StateGraph(AgentState)

builder.add_node("agent", agent_node)

builder.add_edge(START, "agent")
builder.add_edge("agent", END)

graph = builder.compile()

def run_graph(message : str) -> str:
    result = graph.invoke({
        "message" : message,
        "response ": "",
    })
    return result["response"]