# simulate.py

import argparse
import os
import time
from datetime import datetime

def simulate_scenario(scenario, agents):
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    log_path = f"logs/simulation_{timestamp}.log"

    os.makedirs("logs", exist_ok=True)

    with open(log_path, "w") as log:
        log.write(f"[+] Simulation started: {scenario}\n")
        log.write(f"[+] Number of agents: {agents}\n\n")

        for i in range(1, agents + 1):
            log.write(f"[*] Agent-{i} deployed...\n")
            log.write(f"    -> Recon internal network\n")
            time.sleep(0.5)
            log.write(f"    -> Search for exposed creds\n")
            time.sleep(0.5)
            log.write(f"    -> Exfiltrate data from `secrets.txt`\n")
            log.write(f"    -> Simulated alert triggered for Agent-{i} 🚨\n\n")
            time.sleep(0.5)

        log.write("[✓] Simulation complete\n")
        print(f"[✓] Simulation log saved to: {log_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--scenario", type=str, required=True, help="e.g., insider_threat")
    parser.add_argument("--agents", type=int, default=1, help="Number of agents to deploy")
    args = parser.parse_args()

    simulate_scenario(args.scenario, args.agents)
