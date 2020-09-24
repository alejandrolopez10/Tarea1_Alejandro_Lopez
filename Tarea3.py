#!/usr/bin/env python
# coding: utf-8

# In[24]:


from MasaResorte import *


#-----------------Oscilador Armonico Simple----------
#Tiempo en segundos
t = np.linspace(0,100, 200) 
#Se deja caer el bloque a una altura de y = 4m
y01 = np.array([4.0, 0.0])
#Ingresamos los valores de k y m
sol1=Oscilador(1,3) #Insertamos k y m respectivamente
sol1 = odeint(sol1.f, y01, t)

y02 = np.array([-3.0, 0.0])
sol2=Oscilador(0.3,2) #Insertamos k y m respectivamente
sol2 = odeint(sol2.f, y02, t)

y03 = np.array([3.0, 0.0])
sol3=Oscilador(0.3,0.5) #Insertamos k y m respectivamente
sol3 = odeint(sol3.f, y03, t)

y04 = np.array([2.0, 0.0])
sol4=Oscilador(1,8) #Insertamos k y m respectivamente
sol4 = odeint(sol4.f, y04, t)

y05 = np.array([10.0, 0.0])
sol5=Oscilador(0.1,1) #Insertamos k y m respectivamente
sol5 = odeint(sol5.f, y05, t)


#-----------------Posicion vs tiempo


fig, (ax1,ax2,ax3,ax4,ax5) = plt.subplots(5,1,figsize=(10, 20))
# los valores de los ejes y el marcador 
ax1.plot(t, sol1[:, 0], color = 'darkblue')
ax2.plot(t, sol2[:, 0], color = 'green')
ax3.plot(t, sol3[:, 0], color = 'red')
ax4.plot(t, sol4[:, 0], color = 'pink')
ax5.plot(t, sol5[:, 0], color = 'brown')


# Se ponen titulo y nombre de los ejes
ax1.set(title = "Solución M.A.S Bloque soltado desde y = 4m, k = 1, m = 3Kg",
       xlabel = "time",
       ylabel = "$y$")
ax2.set(title = "Solución M.A.S Bloque soltado desde y = -3m, k = 0.3, m = 2Kg \n ",
       xlabel = "time",
       ylabel = "$y$")
ax3.set(title = "Solución M.A.S Bloque soltado desde y = 3m, k = 0.3, m = 0.5Kg",
       xlabel = "time",
       ylabel = "$y$")
ax4.set(title = "Solución M.A.S Bloque soltado desde y = 2m, k = 1, m = 8Kg",
       xlabel = "time",
       ylabel = "$y$")
ax5.set(title = "Solución M.A.S Bloque soltado desde y = 10m, k = 0.1, m = 1Kg",
       xlabel = "time",
       ylabel = "$y$")
fig.suptitle ("Graficas $ y $ vs  $ t $ para Movimiento Armonico Simple ",fontsize=16)
fig.tight_layout(pad=3.0) #Espaciado entre graficas
plt.savefig("MAS.jpg")

#------------------Espacios de fase

fig2, (ax11,ax22,ax33,ax44,ax55) = plt.subplots(5,1,figsize=(10, 20))
# los valores de los ejes y el marcador 
ax11.plot(sol1[:, 0], sol1[:, 1], color = 'darkblue')
ax22.plot(sol2[:, 0], sol2[:, 1], color = 'green')
ax33.plot(sol3[:, 0], sol3[:, 1], color = 'red')
ax44.plot(sol4[:, 0], sol4[:, 1], color = 'pink')
ax55.plot(sol5[:, 0], sol5[:, 1], color = 'brown')


# Se ponen titulo y nombre de los ejes
ax11.set(title = "Espacio de fase k = 1, m = 3Kg",
       xlabel = "$y$",
       ylabel = "$y'$")
ax22.set(title = "Espacio de fase k = 1, m = 1Kg",
       xlabel = "$y$",
       ylabel = "$y'$")
ax33.set(title = "Espacio de fase k = 0.03, m = 0.1Kg",
       xlabel = "$y$",
       ylabel = "$y'$")
ax44.set(title = "Espacio de fase k = 1, m = 8Kg",
       xlabel = "$y$",
       ylabel = "$y'$")
ax55.set(title = "Espacio de fase k = 0.1, m = 4Kg",
       xlabel = "$y$",
       ylabel = "$y'$")
fig2.suptitle ("Graficas $ v $ vs  $ y $ para Movimiento Armonico Simple ",fontsize=16)

fig2.tight_layout(pad=3.0) #Espaciado entre graficas
plt.savefig("MAS_FASE.jpg")


#-------------------------Oscilador Amortiguado

#Ingresamos los valores de k y m
sola1=OsciladorAmortiguado(1,3,0.3) #Insertamos k y m respectivamente
sola1 = odeint(sola1.f, y01, t)


sola2=OsciladorAmortiguado(0.3,2,0.1) #Insertamos k y m respectivamente
sola2 = odeint(sola2.f, y02, t)


sola3=OsciladorAmortiguado(0.3,0.5,0.2) #Insertamos k y m respectivamente
sola3 = odeint(sola3.f, y03, t)


sola4=OsciladorAmortiguado(1,8,0.01) #Insertamos k y m respectivamente
sola4 = odeint(sola4.f, y04, t)


sola5=OsciladorAmortiguado(0.1,1,0.2) #Insertamos k y m respectivamente
sola5 = odeint(sola5.f, y05, t)


#-----------------Posicion vs tiempo


fig3, (ax1,ax2,ax3,ax4,ax5) = plt.subplots(5,1,figsize=(10, 20))
# los valores de los ejes y el marcador 
ax1.plot(t, sola1[:, 0], color = 'darkblue')
ax2.plot(t, sola2[:, 0], color = 'green')
ax3.plot(t, sola3[:, 0], color = 'red')
ax4.plot(t, sola4[:, 0], color = 'pink')
ax5.plot(t, sola5[:, 0], color = 'brown')


# Se ponen titulo y nombre de los ejes
ax1.set(title = "Solución Movimiento Amortiguado Bloque soltado desde y = 4m, k = 1, m = 3Kg, $\gamma =0.3$",
       xlabel = "time",
       ylabel = "$y$")
ax2.set(title = "Solución Movimiento Amortiguado Bloque soltado desde y = -3m, k = 0.3, m = 2Kg , $\gamma =0.1$ \n ",
       xlabel = "time",
       ylabel = "$y'$")
ax3.set(title = "Solución Movimiento Amortiguado Bloque soltado desde y = 3m, k = 0.3, m = 0.5Kg, $\gamma =0.2$",
       xlabel = "time",
       ylabel = "$y'$")
ax4.set(title = "Solución Movimiento Amortiguado Bloque soltado desde y = 2m, k = 1, m = 8Kg, $\gamma =0.01$",
       xlabel = "time",
       ylabel = "$y'$")
ax5.set(title = "Solución Movimiento Amortiguado Bloque soltado desde y = 10m, k = 0.1, m = 1Kg, $\gamma =0.2$",
       xlabel = "time",
       ylabel = "$y'$")
fig3.suptitle ("Graficas $ y $ vs  $ t $ para Movimiento Sub-Amortiguado ",fontsize=16)
fig3.tight_layout(pad=3.0) #Espaciado entre graficas
plt.savefig("Amortiguado.jpg")

#------------------Espacios de fase

fig4, (ax11,ax22,ax33,ax44,ax55) = plt.subplots(5,1,figsize=(10, 20))
# los valores de los ejes y el marcador 
ax11.plot(sola1[:, 0], sola1[:, 1], color = 'darkblue')
ax22.plot(sola2[:, 0], sola2[:, 1], color = 'green')
ax33.plot(sola3[:, 0], sola3[:, 1], color = 'red')
ax44.plot(sola4[:, 0], sola4[:, 1], color = 'pink')
ax55.plot(sola5[:, 0], sola5[:, 1], color = 'brown')


# Se ponen titulo y nombre de los ejes
ax11.set(title = "Espacio de fase k = 1, m = 3Kg, $\gamma =0.3$",
       xlabel = "$y$",
       ylabel = "$y'$")
ax22.set(title = "Espacio de fase k = 1, m = 1Kg, $\gamma =0.1$",
       xlabel = "$y$",
       ylabel = "$y'$")
ax33.set(title = "Espacio de fase k = 0.03, m = 0.1Kg, $\gamma =0.2$",
       xlabel = "$y$",
       ylabel = "$y'$")
ax44.set(title = "Espacio de fase k = 1, m = 8Kg, $\gamma =0.01$",
       xlabel = "$y$",
       ylabel = "$y'$")
ax55.set(title = "Espacio de fase k = 0.1, m = 4Kg, $\gamma =0.2$",
       xlabel = "$y$",
       ylabel = "$y'$")
fig4.suptitle ("Graficas $ v $ vs  $ y $ para Movimiento Amortiguado ",fontsize=16)
fig4.tight_layout(pad=3.0) #Espaciado entre graficas
plt.savefig("Amortiguado_fases.jpg")

plt.show()




        
    


# In[ ]:




