"""
Car sales.
"""
from data.agents import agents
from data.customers import customers
from dealer.agent import Agent
from datetime import datetime, timedelta
from numpy import median
from statistics import stdev
import locale

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

Agent.init(agents(5))

agents = Agent._agents
agent_stats = []
agents = []
wait_times = []

for customer in customers(100):
    stats= Agent.get(customer)
    wait_times.append(stats[0])
    agent_stats.append(stats[1:])


#Calculating Mean, Median, SD
wait_time_mean = ((sum(wait_times)) / float(len(wait_times)))
wait_time_median = median(wait_times)
SD = stdev(wait_times)
stats = [wait_time_mean, wait_time_median, SD]


#Printing Formats
print("----------------------------------------------------------------------------------")
print("%-2s%14s%12s"%("MEAN", "MEDIAN", "SD"))
print("%-2.2f%12.2f%15.2f"%(stats[0], stats[1], stats[2]))
each_agent = set(agent_stats)
print("----------------------------------------------------------------------------------")


print("%-2s%18s%19s%18s%18s"%("AGENT ID", "DEALS MADE", "TOTAL REVENUE", "COMMISSION", "BONUS"))
print("----------------------------------------------------------------------------------")
for individual in each_agent:
    for items in individual:
        locale.setlocale(locale.LC_ALL, '')
        revenue = locale.currency(items.revenue, grouping = True)
        comission = locale.currency(items.comission, grouping = True)
        bonus = locale.currency(items.bonus, grouping = True)
        print("%2s%16s%23s%18s%18s"%(items._agent_id,  items.deals_closed, revenue,  comission, bonus))

   



    

if __name__ == "__main__":
    Run().sales()
