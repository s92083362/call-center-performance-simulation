
##  Project Overview

This simulation analyzes a call center system where:
- Customers call randomly following a **Poisson process**
- Agents handle calls with **exponentially distributed** service times
- Queue follows **First-Come, First-Served (FCFS)** discipline
- Multiple staffing scenarios (3, 5, 7, 9 agents) are compared

**Academic Context:** Mini-project for EEX5362 - Performance Modelling, Open University of Sri Lanka

##  Key Features

- Stochastic simulation using proper statistical distributions
- Multiple performance metrics tracking:
  - Average waiting time
  - Peak queue length
  - Agent utilization
  - System throughput
- Comprehensive data export (CSV format)
- Visualization of performance trends
- Scenario comparison analysis

##  Technologies Used

- **Python 3.x**
- **Libraries:**
  - `random` - Stochastic process generation
  - `pandas` - Data manipulation and analysis
  - `matplotlib` - Performance visualization
  - `numpy` - Mathematical operations
## 📁 Repository Structure
```
call-center-performance-simulation/
│
├── README.md                       #  Project overview and documentation
│
├── simulation_code/                
│   └── call_center_sim.py         #   Main simulation code
│
├── reports/                        #  Project documentation
│   ├── MiniProject_5362.docx       #  Mini-project submission 
│   
│
├── dataset/                        #  Generated simulation data
│   ├── performance_summary.csv     #  Overall metrics across 
│   ├── simulation_results_3_agents.csv
│   ├── simulation_results_5_agents.csv
│   ├── simulation_results_7_agents.csv
│   └── simulation_results_9_agents.csv
│
└── results/                        #  Performance visualizations
    ├── waiting_time_vs_agents.png is
    ├── queue_length_vs_agents.png
    ├── utilization.png          
    └── throughput.png             
```
##  How to Run

### Prerequisites
```bash
pip install pandas matplotlib numpy
```

### Execute Simulation
```bash
python call_center_sim.py
```

### Output
- CSV files in `dataset/` folder with detailed call records
- PNG graphs in `results/` folder showing performance metrics
- Console output with performance summary
## Simulation Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| **SIMULATION_TIME** | 3600 seconds | 1 hour simulation duration |
| **CALL_ARRIVAL_RATE** | 0.2 calls/sec | ~720 calls/hour |
| **SERVICE_TIME_MEAN** | 30 seconds | Average call handling time |
| **NUM_AGENTS** | [3, 5, 7, 9] | Staffing scenarios tested |

##  Key Performance Metrics

1. **Average Waiting Time** - Customer time in queue before service
2. **Peak Queue Length** - Maximum concurrent waiting customers
3. **Agent Utilization** - Percentage of time agents are busy
4. **Throughput** - Total calls successfully completed

##  Key Findings

- **3 agents**: System severely overloaded (880s avg wait, 100% utilization)
- **5 agents**: Still congested (297s avg wait, 100% utilization)
- **7 agents**: Optimal balance (14s avg wait, 92% utilization)
- **9 agents**: Overstaffed (2s avg wait, 69% utilization)

**Conclusion:** 7 agents provides the best balance between service quality and resource efficiency for this call volume.

## 📄 Documentation

Detailed project documentation including:
- High-level problem description
- System architecture
- Performance objectives
- Dataset specifications


See `MiniProject_5362.docx` for complete documentation.

## 👤 Author

**R.M.B.P.B Weerakoon**
- Registration: 721643362
- Student Number: S92083362
- Course: EEX5362 - Performance Modelling

