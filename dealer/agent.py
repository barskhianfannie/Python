"""
Agent object.
"""
from data.agents import agents
from datetime import datetime, timedelta
from data import CARS, HOURS

freeAgents= []
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
        for agent in cls._agents:
            freeAgents.append(agent)
    
     

        
    @classmethod
    def get(cls, customer):
        """
        Assign the best agent for the customer, creating an instance if necessary.
        Return the agent and wait time (0 if an agent is readily available).
            - customer: Info of customer.
        """  
        wait_time = 0
        best_agent = []
        for agent in cls._agents:
            if len(freeAgents) == 0:
                best_agent = filter(lambda x : min(x["available_time"]) , cls._agents)
                wait_time = agent.available_time - customer["arrival_time"]
            else:
                break

        for agent in freeAgents:
            best_agent = max(freeAgents, key=lambda a: 10 * a._expertise[customer["interest"]] + a._rating)
            best_agent.available_time = customer['arrival_time'] + timedelta(hours = best_agent._service_time)
            freeAgents.remove(agent)
               

        return wait_time, best_agent
        
    
        # for revenue in cls._agents:
        #     if customer['sale_closed'] is True:
        #         car_sold = customer["interest"]
        #         total_revenue = CARS[car_sold]["price"]
        #         sales.append(total_revenue)
        #         revenue.revenue += total_revenue

        # return revenue.revenue

