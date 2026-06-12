import subprocess
import datetime
def run_scan(target):
    print(f"\n Scanning {target}...")
    result=subprocess.run(
      ["nmap" , "-Pn", "-sV", "-oN", "scan report.txt", target], 
       capture_output=True,
       text=True
    )
    return result.stdout
def main():
    print("----- Network Scanner Tool -----")
    target = input("Enter IP address to scan: ")
    scan_result = run_scan(target)
    timestamp = datetime.datetime.now()
    print(f"\n Scan completed at: {timestamp}")
    print("Report saved to scan_report.txt")
    print("\n --- Scan Results ---")
    print(scan_result)
main()

