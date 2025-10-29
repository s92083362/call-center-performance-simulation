import random # for random number generation
import csv  # for CSV file operations
import math # for mathematical functions
import pandas as pd  # for data manipulation and analysis
import matplotlib.pyplot as plt  # for plotting graphs
import os  # for interacting with the operating system


# Ensure output directories exist
os.makedirs("results", exist_ok=True)
os.makedirs("dataset", exist_ok=True)

# CONFIGURATION PARAMETERS
SIMULATION_TIME = 3600  # seconds (1 hour)
CALL_ARRIVAL_RATE = 0.2  # average 0.2 calls/sec
SERVICE_TIME_MEAN = 30   # average call service time (seconds)
NUM_AGENTS_LIST = [3, 5, 7, 9]  # Scenarios to test

# HELPER FUNCTIONS
def exponential(mean):
    """Generate an exponentially distributed random variable."""
    return random.expovariate(1 / mean)

def poisson_next_arrival(rate):
    """Generate next arrival time from exponential distribution."""
    return random.expovariate(rate)

# SIMULATION FUNCTION
def run_simulation(num_agents):  # Simulate call center with given number of agents
    current_time = 0  # in seconds
    next_arrival = poisson_next_arrival(CALL_ARRIVAL_RATE)  # time of next call arrival
    agents = [0] * num_agents  # When each agent becomes free
    queue = []  # Call queue
    dataset = []  # To store simulation data
    call_id = 0   # Unique call identifier

    while current_time < SIMULATION_TIME:
        # Handle arrivals
        if next_arrival <= current_time:
            call_id += 1
            queue.append((call_id, current_time))
            next_arrival += poisson_next_arrival(CALL_ARRIVAL_RATE)

        # Assign calls to free agents
        for agent_id in range(num_agents):
            if agents[agent_id] <= current_time and queue:  # Agent is free and there are calls waiting
                call, arrival_time = queue.pop(0)   # Get next call from queue
                waiting_time = current_time - arrival_time   # Calculate waiting time
                service_time = exponential(SERVICE_TIME_MEAN)  # Generate service time
                service_end = current_time + service_time # Calculate service end time
                agents[agent_id] = service_end  # Update agent's next free time

                dataset.append({
                    "Call_ID": call,  # Unique call identifier
                    "Arrival_Time": round(arrival_time, 2),  # Round to 2 decimal places
                    "Service_Start_Time": round(current_time, 2), 
                    "Service_End_Time": round(service_end, 2),
                    "Waiting_Time": round(waiting_time, 2),
                    "Service_Duration": round(service_time, 2),
                    "Agent_ID": agent_id + 1, # 1-based agent ID
                    "Queue_Length_On_Arrival": len(queue)  # Queue length when call arrived
                })

        current_time += 1  # advance time step

    return dataset

# PERFORMANCE METRIC CALCULATIONS
def calculate_metrics(data, num_agents):
    df = pd.DataFrame(data)
    total_calls = len(df)
    avg_waiting_time = df["Waiting_Time"].mean()
    avg_queue_length = df["Queue_Length_On_Arrival"].mean()
    throughput = total_calls / (SIMULATION_TIME / 3600)

    # Agent utilization = (sum of all service times) / (num_agents * total simulation time)
    total_service_time = df["Service_Duration"].sum()
    utilization = total_service_time / (num_agents * SIMULATION_TIME)

    metrics = {
        "Agents": num_agents,
        "Average_Waiting_Time (s)": round(avg_waiting_time, 2),
        "Average_Queue_Length": round(avg_queue_length, 2),
        "Throughput (calls/hour)": round(throughput, 2),
        "Agent_Utilization (%)": round(utilization * 100, 2)
    }
    return metrics

# MAIN SIMULATION & ANALYSIS LOOP
all_metrics = []

for num_agents in NUM_AGENTS_LIST:
    print(f"\nRunning simulation for {num_agents} agents...")
    data = run_simulation(num_agents)

    # Save dataset to CSV in "dataset" directory
    filename = f"dataset/simulation_results_{num_agents}_agents.csv"
    pd.DataFrame(data).to_csv(filename, index=False)
    print(f"Saved dataset: {filename} ({len(data)} records)")

    # Calculate metrics
    metrics = calculate_metrics(data, num_agents)
    all_metrics.append(metrics)

# SHOW PERFORMANCE SUMMARY
results_df = pd.DataFrame(all_metrics)
print("\nPERFORMANCE SUMMARY:")
print(results_df.to_string(index=False))

# PLOT GRAPHS (save to "results" folder)
#  Average Waiting Time vs Number of Agents
plt.figure(figsize=(8, 5))
plt.plot(results_df["Agents"], results_df["Average_Waiting_Time (s)"], marker='o', color='blue')
plt.title("Average Waiting Time vs Number of Agents")
plt.xlabel("Number of Agents")
plt.ylabel("Average Waiting Time (seconds)")
plt.grid(True)
plt.savefig("results/waiting_time_vs_agents.png", dpi=300)
plt.show()

#  Average Queue Length vs Number of Agents
plt.figure(figsize=(8, 5))
plt.plot(results_df["Agents"], results_df["Average_Queue_Length"], marker='o', color='orange')
plt.title("Average Queue Length vs Number of Agents")
plt.xlabel("Number of Agents")
plt.ylabel("Average Queue Length")
plt.grid(True)
plt.savefig("results/queue_length_vs_agents.png", dpi=300)
plt.show()

#  Throughput vs Number of Agents
plt.figure(figsize=(10, 6))
plt.plot(results_df["Agents"], results_df["Throughput (calls/hour)"], marker='o', color='green', label='Throughput')
plt.title("Throughput vs Number of Agents")
plt.xlabel("Number of Agents")
plt.ylabel("Calls per Hour")
plt.legend()
plt.grid(True)
plt.savefig("results/throughput.png", dpi=300)
plt.show()

#  Agent Utilization vs Number of Agents
plt.figure(figsize=(10, 6))
plt.plot(results_df["Agents"], results_df["Agent_Utilization (%)"], marker='o', color='red', label='Agent Utilization (%)')
plt.title("Agent Utilization vs Number of Agents")
plt.xlabel("Number of Agents")
plt.ylabel("Utilization (%)")
plt.legend()
plt.grid(True)
plt.savefig("results/utilization.png", dpi=300)
plt.show()

# SAVE SUMMARY TO CSV in "dataset" directory
results_df.to_csv("dataset/performance_summary.csv", index=False)
print("\nAll results saved: dataset/performance_summary.csv, graph images in 'results', and scenario datasets in 'dataset'.")
