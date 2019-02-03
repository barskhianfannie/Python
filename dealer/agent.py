"""
Agent object.
"""
from data.agents import agents
from datetime import datetime, timedelta
from data import CARS, HOURS

freeAgents= []
agentList = []
wait_time = 0

class Agent(object):
    """
    Car sales agent.
    """
    
    def __init__(self, data):
        self._agent_id = data["agent_id"]
        self._expertise = data["expertise"]
        self._service_time = data["service_time"]
        self._rating = data["rating"]
        self.revenue = 0
        self.deals_closed = 0
        self.comission = 0
        self.bonus = 0
        today = datetime.today()
        self.available_time = datetime(today.year, today.month, today.day, HOURS[0])


    @classmethod
    def init(cls, agent_data):
        cls._agents = [Agent(data) for data in agent_data]
        
        
    @classmethod
    def get(cls, customer):
        """
        Assign the best agent for the customer, creating an instance if necessary.
        Return the agent and wait time (0 if an agent is readily available).
            - customer: Info of customer.
        """  
        wait_time = 0.0
        best_agent = []

        for agent in cls._agents:
            if agent.available_time < customer["arrival_time"]:
                freeAgents.append(agent)
            
        
        if len(freeAgents) > 0 :
            for agent in freeAgents:
                best_agent = max(freeAgents, key=lambda a: 10 * a._expertise[customer["interest"]] + a._rating)
                freeAgents.remove(agent)
                agent.available_time = customer['arrival_time'] + timedelta(hours = agent._service_time)
                if customer["sale_closed"]:
                    car = customer["interest"]
                    best_agent.revenue += CARS[car]["price"]
                    best_agent.deals_closed += 1
                    best_agent.comission += 10000
        else:
            for agent in cls._agents:
                if agent.available_time < customer["arrival_time"]:
                    wait_time = 0.0
                else:
                    wait_object= agent.available_time - customer["arrival_time"] 
                    agent.available_time = agent.available_time + timedelta(hours= agent._service_time)
                    wait_time = (((wait_object.total_seconds()) / 60 / 60))
           
       
        return wait_time, agent

        # for revenue in cls._agents:
        #     if customer['sale_closed'] is True:
        #         car_sold = customer["interest"]
        #         total_revenue = CARS[car_sold]["price"]
        #         sales.append(total_revenue)
        #         revenue.revenue += total_revenue

        # return revenue.revenue

