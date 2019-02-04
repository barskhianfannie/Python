"""
Agent object.
"""
from data.agents import agents
from datetime import datetime, timedelta
from data import CARS, HOURS

freeAgents= []

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
            cls._bonus = agent.available_time + timedelta(days= 7)
        
        
    @classmethod
    def get(cls, customer):
        """
        Assign the best agent for the customer, creating an instance if necessary.
        Return the agent and wait time (0 if an agent is readily available).
            - customer: Info of customer.
        """  
        wait_time = 0.0
        #Placing 5 agents into Free Agent List to calculate best agents for first customers
        for agent in cls._agents:
            if agent.available_time < customer["arrival_time"]:
                freeAgents.append(agent)
            
        #calculating best agent then updating time and adding to available agent list
        if len(freeAgents) > 0 :
            for agent in freeAgents:
                best_agent = max(freeAgents, key=lambda a: 10 * a._expertise[customer["interest"]] + a._rating)
                freeAgents.remove(best_agent)
                best_agent.available_time = customer['arrival_time'] + timedelta(hours = best_agent._service_time)
        else:
            for agent in cls._agents:
                if agent.available_time < customer["arrival_time"]:
                    wait_time = 0.0
                else:
                    wait_object= agent.available_time - customer["arrival_time"] 
                    agent.available_time = agent.available_time + timedelta(hours= agent._service_time)
                    wait_time = (((wait_object.total_seconds()) / 60 ))         
       
        if customer["sale_closed"]:
                    car = customer["interest"]
                    agent.revenue += CARS[car]["price"]
                    agent.deals_closed += 1
                    agent.comission += 10000


        #Calculate Bonus if sold 10 or more cars in one week. 
        for bonus in cls._agents:
            if bonus.deals_closed >= 10 and (cls._bonus > customer["arrival_time"]):
                bonus.bonus = 100000

        return wait_time, agent
