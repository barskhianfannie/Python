"""
Car sales.
"""
from data.agents import agents
from data.customers import customers
from dealer.agent import Agent
from datetime import datetime, timedelta
from numpy import median
from statistics import stdev

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

Agent.init(agents(4))

agents = Agent._agents

wait_times = []
for customer in customers(4):
    stats= Agent.get(customer)
    print(stats)
    wait_times.append(stats[0])


wait_time_mean = ((sum(wait_times)) / float(len(wait_times)))
wait_time_median = median(wait_times)
SD = stdev(wait_times)
print(wait_time_mean, wait_time_median, SD)

   



    

if __name__ == "__main__":
    Run().sales()
