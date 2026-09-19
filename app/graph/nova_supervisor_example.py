"""Reference top-level NOVA LangGraph composition.

Replace placeholder specialist nodes with the production Treasury Navigator,
Risk Calculator, Scenario Simulator, and other agent subgraphs in the main NOVA codebase.
"""
from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class NovaState(TypedDict, total=False):
    user_query: str
    route: str
    result: dict


def build_nova_supervisor(web_search_node, treasury_navigator_node, risk_calculator_node, scenario_simulator_node):
    graph = StateGraph(NovaState)

    def route(state: NovaState):
        # Production router should use NOVA's approved routing policy/model.
        return state.get('route', 'web_search')

    graph.add_node('web_search', web_search_node)
    graph.add_node('treasury_navigator', treasury_navigator_node)
    graph.add_node('risk_calculator', risk_calculator_node)
    graph.add_node('scenario_simulator', scenario_simulator_node)
    graph.add_conditional_edges(START, route, {
        'web_search': 'web_search',
        'treasury_navigator': 'treasury_navigator',
        'risk_calculator': 'risk_calculator',
        'scenario_simulator': 'scenario_simulator',
    })
    for node in ('web_search','treasury_navigator','risk_calculator','scenario_simulator'):
        graph.add_edge(node, END)
    return graph.compile()
