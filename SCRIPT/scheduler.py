import sys
import time
import subprocess

def main():
    if len(sys.argv) != 5:
        print(f"Usage: python {sys.argv[0]} <platform> <type> <sleep> <times>")
        sys.exit(1)

    platform = sys.argv[1]
    run_type = sys.argv[2]
    sleep_minutes = int(sys.argv[3])
    times = int(sys.argv[4])

    print(f"Starting scheduler with parameters: platform={platform}, type={run_type}, sleep={sleep_minutes}, times={times}")

    for _ in range(times):
        print(f"Running: make run platform={platform} type={run_type}")
        subprocess.run(["make", "run", f"platform={platform}", f"type={run_type}"])
        print(f"Sleeping for {sleep_minutes} minutes")
        time.sleep(sleep_minutes * 60)

if __name__ == "__main__":
    main()
