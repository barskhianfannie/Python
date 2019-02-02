"""
Agent object.
"""
from data.agents import agents
from datetime import datetime, timedelta
from data import CARS, HOURS

customerList = []
sales = []

class Agent(object):
    """
    Car sales agent.
    """
    
    waiting_time = 0


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
        cls.customer = customer
        total_revenue = int
        
        
        for cust in customer:
            customerList.append(cust)
        print(customerList)
        
        for rating in cls._agents:
            print(rating.available_time)
            specialty = max(rating._expertise)
            top_rating = [i for i, j in enumerate(rating._expertise) if j == specialty]
            print(rating._service_time)
        for customer in customerList:
            # if customer['interest'] == top_rating:
            rating.available_time = customer['arrival_time'] + timedelta(hours=rating._service_time)
            print(rating.available_time)
            if customer['sale_closed'] is True:
                car_sold = customer["interest"]
                total_revenue = CARS[car_sold]["price"]
                print(rating.revenue + total_revenue)
                print(total_revenue)
                sales.append(total_revenue)

        print(sum(sales))

        

    # total_revenue = 0 
    # def showroom_revenue(self):
    #     for customer in customerList:
    #         print(customer)
    #     if customer['sale_closed']:
    #         car_sold = customer["interest"]
    #         total_revenue = CARS[car_sold]["price"]
    #         print(total_revenue)
                        
        # agent = max(cls._agent_data, )
        # #Pick the right agent from agent_data
        # if agent_id  not in self._agents:
        #     self._agents[agent_id]


 