from Model import *
from mesa import Model
from mesa import Agent
from TrafficLight import TrafficLightAgent
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

Intersectionmodel = Intersection

grid = CanvasGrid(agent_portrayal, Intersectionmodel().width, Intersectionmodel().height, 750, 750)
server = ModularServer(Intersectionmodel,
                       [grid],
                       "Intersectionmodel"
                       )
server.port = 8520  # The default
server.launch()
