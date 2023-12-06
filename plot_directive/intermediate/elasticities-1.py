import tellurium as te
r = te.loada ('''A -> B; k1*A; k1=0.1; A = 10''')
m = r.simulate (0, 40, 100)
r.plot()