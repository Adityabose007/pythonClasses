import matplotlib.pyplot as plt
sizes = [30, 40, 20 ,10]
labels = ['A', 'B', 'C', 'D']
plt.pie(sizes, labels=labels)
plt.show()

plt.savefig("myplot2.png", dpi=300, bbox_inches='tight')
