"""
Car sales.
"""
from data.agents import agents
from data.customers import customers
from dealer.agent import Agent

class Run(object):
    """
    Run the sales.
    """

    def sales(self):
        """
        Simulate sales using test data and print out customer and agent reports showing
            (1) Summary statistics, with the mean, median, and SD of customer wait times.
            (2) Agent data showing agent ID, deals closed, total revenue generated,
                commission earned, and bonus awarded, in a tabular form.
        """
Agent.init(agents(2))
all_customers = customers(1)  
agents = Agent._agents

for customer in all_customers:
    Agent.get(customer)

for agent in agents:
    print(agent.revenue)


    

if __name__ == "__main__":
    Run().sales()
