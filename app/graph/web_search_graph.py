from __future__ import annotations
from langgraph.graph import StateGraph, START, END
from app.graph.state import WebSearchState
from app.agents.web_search_agent import WebSearchAgent


def build_web_search_graph(agent: WebSearchAgent):
    """Build the Web Search subgraph used by the platform-level NOVA LangGraph.

    The platform graph can invoke this compiled subgraph as one node among Treasury
    Navigator, Risk Calculator, Scenario Simulator, and other specialist agents.
    """
    graph = StateGraph(WebSearchState)

    async def run_agent(state: WebSearchState):
        return await agent.execute(dict(state))

    def route_after_agent(state: WebSearchState):
        if state.get('policy_decision') == 'block':
            return 'blocked'
        if not state.get('evidence_sufficient'):
            return 'insufficient'
        return 'ready'

    def blocked(state: WebSearchState):
        return {'warnings': list(dict.fromkeys(state.get('warnings', []) + ['SEARCH_BLOCKED_BY_POLICY']))}

    def insufficient(state: WebSearchState):
        return {'warnings': list(dict.fromkeys(state.get('warnings', []) + ['INSUFFICIENT_EVIDENCE']))}

    def ready(state: WebSearchState):
        return state

    graph.add_node('web_search_agent', run_agent)
    graph.add_node('blocked', blocked)
    graph.add_node('insufficient', insufficient)
    graph.add_node('ready', ready)
    graph.add_edge(START, 'web_search_agent')
    graph.add_conditional_edges('web_search_agent', route_after_agent,
                                {'blocked': 'blocked', 'insufficient': 'insufficient', 'ready': 'ready'})
    graph.add_edge('blocked', END)
    graph.add_edge('insufficient', END)
    graph.add_edge('ready', END)
    return graph.compile()
