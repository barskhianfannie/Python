"""
Unit tests for agent module.
"""
import unittest
from dealer.agent import Agent


class TestAgent(unittest.TestCase):
    """
    Tests for agent.
    """

    # def setUp(self):
    #     self.agent = Agent()

    def test_agent_instance(self):
        agent1_id = '675765'
        expertise1 = [3, 2, 4, 1]
        service_time1 = 8
        rating1 =  0.987
        agent = [agent1_id, expertise1, service_time1, rating1]
        agent_1 = Agent(agent)
        agent_1.init(agent)
        assert agent_1._agent_id == agent1_id
        assert agent_1._expertise == expertise1
        assert agent_1._service_time == service_time1
        assert agent_1._rating == rating1


    def setUp(self):
        pass


if __name__ == "__main__":
    unittest.main()
