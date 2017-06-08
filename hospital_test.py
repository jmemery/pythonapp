#!/usr/bin/python
# Filename: Simulation.py
import numpy as np
import random
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import CCmod as CC
def f(x): return x>.7

Times=800
Duration=1800
AHT=450
ExpVar=1./450
# Agenten klaar zetten:
Agents=[]
AgentsScheduled = 70

for i in range(0,AgentsScheduled):
	Agents.append(CC.Agent())

ArrivalRate = 300. / 1800.

SL=[]

#Het callcenter wordt Times geevalueerd
for teller in range(0,Times):
	Arrivals = stats.poisson.rvs(ArrivalRate,size=Duration)
	Callers=[]
	CallersInLine = 0
	CC.Caller.callers = 0.
	for a in Agents:
		a.busy=0
		a.busyTime=0
	i = 0
	# Elke i is een seconde. Elke seconde wordt het call center geevalueerd.
	while i <= Duration or CallersInLine > 0:
		# Evalueer of er gesprekken beeindigd worden. Callers zijn dan ready en Agent niet meer busy.
		for cal in Callers:
			if cal.ArrivalTime+cal.HandleTime+cal.TimeInQueue <= i and cal.queued==0:
				cal.Ready=1

		for ag in Agents:
			if ag.busy==1 and ag.busytime<=i:
				ag.busy=0

		# Maak de nieuwe bellers aan.
		if i < Duration:
			for j in range(0,Arrivals[i]):
				HT=random.expovariate(ExpVar)
				Callers.append(CC.Caller(i,HT))

		# check of er callers in de wachtrij staan. Als dat zo is wijs ze aan vrije agenten toe.
		for call in Callers:
			if call.queued==1:
				for ag in Agents:
					if call.queued == 1 and ag.busy == 0:
						call.queued = 0
						ag.busytime = call.ArrivalTime+call.HandleTime+call.TimeInQueue
						ag.busy = 1

		# Wachttijd updaten
		CallersInLine=0
		for call in Callers:
			if call.queued == 1:
				call.TimeInQueue = i - call.ArrivalTime
				CallersInLine += 1

		for ag in Agents:
			if ag.busy==0:
				ag.IdleTime += 1
		i+=1

	# Resultaten, statistieken maken.
	InServiceLevel=0.
	WaitTime=[]

	ArrivalTime=[]
	for a in Callers:
	#print a.TimeInQueue
		ArrivalTime.append(a.ArrivalTime)
		WaitTime.append(a.TimeInQueue)
		if a.TimeInQueue<30:
			InServiceLevel += 1.

	#print "Een Ronde"
	#print max(WaitTime)
	#print sum(WaitTime, 0.0) / len(WaitTime)
	print InServiceLevel/(CC.Caller.callers+1)
	SL.append(InServiceLevel/(CC.Caller.callers+1))

	#for a in Agents:
	#print a.IdleTime
	#plotnr=221+teller
	#plt.subplot(plotnr)
	#plt.plot(ArrivalTime,WaitTime)
Idle=0.
for a in Agents:
	Idle += a.IdleTime

print "Kans op verwacht servicelevel:"
print len(filter(f, SL))/(1.0*len(SL))
print "Idletime:"
print Idle/(Times*Duration*AgentsScheduled)


n, bins, patches = plt.hist(SL, 40, range=(0,1),normed=1, facecolor='green', alpha=0.75)

plt.show()
