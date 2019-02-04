"""
Unit tests for agent module.
"""
import unittest
from dealer.agent import Agent
from data.agents import agents
from data.customers import customers


class TestAgent(unittest.TestCase):
    """
    Tests for agent.
    """

    #Make sure agent is being added correctly
    def test_init(self):
        agent1_id = 675765
        expertise1 = [3, 2, 4, 1]
        service_time1 = 8
        rating1 =  0.987
        agent1 = [agent1_id, expertise1, service_time1, rating1]
        for agent in Agent.init(agent1):
            assert agent._agent_id == 675765
            assert agent._expertise == [3, 2, 4, 1]
            assert agent._service_time == 8
            assert agent._rating == 0.987

    #Make sure bonus is applied
    @classmethod
    def test_get(cls, customer):
        for agent in Agent.init(agents(1)):
            assert agent.deals_closed == 10
            assert agent._bonus > customer["arrival_time"]
            if agent.bonus == 100000:
                print("this test works")
        


if __name__ == "__main__":
    unittest.main()
