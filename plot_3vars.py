"""

E. Wes Bethel, Copyright (C) 2022

October 2022

Description: This code loads a .csv file and creates a 3-variable plot

Inputs: the named file "sample_data_3vars.csv"

Outputs: displays a chart with matplotlib

Dependencies: matplotlib, pandas modules

Assumptions: developed and tested using Python version 3.8.8 on macOS 11.6

"""



import pandas as pd

import matplotlib.pyplot as plt



SYSTEM_MEMORY_BANDWIDTH_GBPS = 204.8  # CPU Node 204.8 GB/s memory bandwidth per CPU

BYTES_PER_ACCESS = 8  # Each uint64_t element is 8 bytes





fname = "sample_data_3vars.csv"

df = pd.read_csv(fname, comment="#")

print(df)



var_names = list(df.columns)

print("var names =", var_names)



problem_sizes = df[var_names[0]].values.tolist()

direct_time = df[var_names[1]].values.tolist()

vector_time = df[var_names[2]].values.tolist()

indirect_time = df[var_names[3]].values.tolist()



ops_per_problem_size = [i for i in problem_sizes]



# Calculate MFLOP/s

mflops_direct = [(ops / 1e6) / time for ops, time in zip(ops_per_problem_size, direct_time)]

mflops_vector = [(ops / 1e6) / time for ops, time in zip(ops_per_problem_size, vector_time)]

mflops_indirect = [(ops / 1e6) / time for ops, time in zip(ops_per_problem_size, indirect_time)]



# start a new plot

plt.figure()

plt.title("MFLOP/s")

xlocs = [i for i in range(len(problem_sizes))]

plt.xticks(xlocs, problem_sizes)



plt.plot(mflops_direct, "r-o", label=var_names[1])

plt.plot(mflops_vector, "b-x", label=var_names[2])

plt.plot(mflops_indirect, "g-^", label=var_names[3])



plt.xlabel("Problem Size")

plt.ylabel("MFLOP/s")

plt.legend(loc="best")

plt.grid(axis='both')

plt.show()



# Calculate % bandwidth

bandwidth_direct = [(0 / time) / SYSTEM_MEMORY_BANDWIDTH_GBPS * 100 if time > 0 else 0 for time in direct_time]

bandwidth_vector = [(size * BYTES_PER_ACCESS / 1e9) / time / SYSTEM_MEMORY_BANDWIDTH_GBPS * 100 for size, time in zip(problem_sizes, vector_time)]

bandwidth_indirect = [(2 * size * BYTES_PER_ACCESS / 1e9) / time / SYSTEM_MEMORY_BANDWIDTH_GBPS * 100 for size, time in zip(problem_sizes, indirect_time)]



plt.figure()

plt.title("Memory Bandwidth Utilization (%)")

xlocs = [i for i in range(len(problem_sizes))]

plt.xticks(xlocs, problem_sizes)



plt.plot(bandwidth_direct, "r-o", label=f"Bandwidth Utilization {var_names[1]}")

plt.plot(bandwidth_vector, "b-x", label=f"Bandwidth Utilization {var_names[2]}")

plt.plot(bandwidth_indirect, "g-^", label=f"Bandwidth Utilization {var_names[3]}")



plt.xlabel("Problem Size")

plt.ylabel("Memory Bandwidth Utilization (%)")

plt.legend(loc="best")

plt.grid(axis='both')

plt.show()



# Calculate latency

memory_direct = 0

latency_direct = [(time / memory_direct) * 1e9 if memory_direct > 0 else 0 for time in direct_time]

latency_vector = [(time / size) * 1e9 for time, size in zip(vector_time, problem_sizes)]

latency_indirect = [(time / (2*size)) * 1e9 for time, size in zip(indirect_time, problem_sizes)]



plt.figure()

plt.title("Memory Latency")

xlocs = [i for i in range(len(problem_sizes))]

plt.xticks(xlocs, problem_sizes)



plt.plot(latency_direct, "r-o", label=f"Latency {var_names[1]}")

plt.plot(latency_vector, "b-x", label=f"Latency {var_names[2]}")

plt.plot(latency_indirect, "g-^", label=f"Latency {var_names[3]}")



plt.xlabel("Problem Size")

plt.ylabel("Latency (ns)")

plt.legend(loc="best")

plt.grid(axis='both')

plt.show()



# EOF

