#!/usr/bin/env python
# coding: utf-8



import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

class Oscilador:
    #Llamamos al constructor
    def __init__(self,k,m):
        #Atributos 
        self.k = k
        self.m = m
        
    #Creamos f que es la ecuación de movimiento de un M.A.S
    
    def f(self,y,t):
        
        return np.array([y[1],-(self.k/self.m)*y[0]])



class OsciladorAmortiguado:
    #Llamamos al constructor
    def __init__(self,k,m,gamma):
        #Atributos 
        self.k = k
        self.m = m
        self.gamma = gamma
        
    #Creamos f que es la ecuación de movimiento libre amortiguado
    
    def f(self,y,t):

        return np.array([y[1],(-(self.k/self.m))*(y[0]) - self.gamma*y[1]])



        







