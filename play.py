import matplotlib.pyplot as plt
import numpy as np

TOTAL_ACC = 229_000
MONTHLY_SAVINGS = TOTAL_ACC/32
AIM = 1_000_000
YEARLY_RATE = 0.1447

yearly_incs = []

while TOTAL_ACC < AIM:
    inc = TOTAL_ACC * YEARLY_RATE + MONTHLY_SAVINGS * 12
    TOTAL_ACC += inc
    yearly_incs.append(TOTAL_ACC)

xaxis = np.array(range(1, len(yearly_incs) + 1))
yaxis = np.array(yearly_incs)

plt.plot(xaxis, yaxis)
plt.show()

print(TOTAL_ACC)
print(len(yearly_incs))
