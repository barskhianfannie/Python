"""
Agent object.
"""
from data.agents import agents
from datetime import datetime, timedelta
from data import CARS, HOURS

agentList = []
busy = []
available = []
sales = []
waiting_times = []

class Agent(object):
    """
    Car sales agent.
    """
    
    def __init__(self, data):
        self._agent_id = data["agent_id"]
        self._expertise = data["expertise"]
        self._service_time = data["service_time"]
        self._rating = data["rating"]
        self.revenue = 5
        self.deals_closed = 0
        self.comission = 0
        self.bonus = 0
        today = datetime.today()
        self.available_time = datetime(today.year, today.month, today.day, HOURS[0])


    @classmethod
    def init(cls, agent_data):
        cls._agents = [Agent(data) for data in agent_data]
        agentList.append(cls._agents)

        
    @classmethod
    def get(cls, customer):
        """
        Assign the best agent for the customer, creating an instance if necessary.
        Return the agent and wait time (0 if an agent is readily available).
            - customer: Info of customer.
        """  
        print(customer)
        for agent in cls._agents:
            if customer["arrival_time"] >= agent.available_time:
                highest_rating = max(cls._agents, key=lambda a: 10 * a._expertise[customer["interest"]] + a._rating)
                highest_rating.available_time = customer['arrival_time'] + timedelta(hours= highest_rating._service_time)
                wait_time = 0
                print(wait_time, "didn't wait")
            else:
                wait_time = agent.available_time - customer["arrival_time"]
                agent.available_time = agent.available_time + timedelta(hours= agent._service_time)
                print(agent.available_time, "waited:", wait_time)


        

        # for rating in cls._agents:
        #     rating.available_time = customer['arrival_time'] + timedelta(hours=rating._service_time)
        #     print(rating.available_time, "updated arrival")
 
        for revenue in cls._agents:
            if customer['sale_closed'] is True:
                car_sold = customer["interest"]
                total_revenue = CARS[car_sold]["price"]
                sales.append(total_revenue)
            


        

 