import matplotlib.pyplot as plt

from die import Die

die_1 = Die()
die_2 = Die()

results = [die_1.roll()+die_2.roll() for _ in range(1000)]

max_sides = die_1.num_sides + die_2.num_sides
frequencies = [results.count(x) for x in range(2, max_sides+1)]
values = [x for x in range(2, max_sides+1)]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(values, frequencies, linewidth=3)

ax.set_title('2 d6 Die Roll', fontsize=24)
ax.set_xlabel('Sides', fontsize=14)
ax.set_ylabel('Frequency of Roll', fontsize=14)

ax.tick_params(axis='both', labelsize=14)

plt.show()