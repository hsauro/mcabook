import tellurium as te

r = te.loada("""
  J1: $S1 -> S2; k1*S1 - k2*S2
  J2: S2 -> $S3; k3*S2 - k4*S3

  k1 = 0.34; k2 = 0.23
  k3 = 0.45; k4 = 0.23
  S1 = 10
""")

m = r.simulate (0, 20, 100, ['time', 'S1', 'S2', 'S3', 'J1', 'J2'])
r.plot(xtitle='Time', ytitle='Concentration')