import argparse
import subprocess
from rich.console import Console
from rich.table import Table
import os
import json

console = Console()

def run_command(command):
    """Run a shell command and capture output"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout, result.stderr, result.returncode
    except Exception as e:
        return "", str(e), 1


def run_bandit(target_dir):
    """Run Bandit security scanner"""
    console.print("[bold blue]🔍 Running Bandit (Python security scan)...[/bold blue]")
    os.makedirs("reports", exist_ok=True)
    cmd = f"python -m bandit -r {target_dir} -f json -o reports/bandit_report.json"
    return run_command(cmd)


def run_checkov(target_dir):
    """Run Checkov IaC & config scanner"""
    console.print("[bold blue]☁️  Running Checkov (IaC / config scan)...[/bold blue]")
    os.makedirs("reports", exist_ok=True)
    # Correct usage of Checkov output mapping
    cmd = f"checkov -d {target_dir} -o json --output-file-path reports"
    return run_command(cmd)


def summarize_bandit():
    """Read and summarize Bandit results"""
    try:
        with open("reports/bandit_report.json", "r") as f:
            data = json.load(f)
        issues = data.get("results", [])
        return len(issues)
    except Exception:
        return 0


def summarize_checkov():
    """Read and summarize Checkov results across multiple frameworks"""
    try:
        report_path = "reports/results_json.json"
        if not os.path.exists(report_path):
            return {}

        with open(report_path, "r") as f:
            data = json.load(f)

        summary = {}
        if isinstance(data, list):
            for item in data:
                check_type = item.get("check_type", "unknown")
                failed = item.get("summary", {}).get("failed", 0)
                summary[check_type] = failed
        else:
            # fallback in case output is not list
            failed = data.get("summary", {}).get("failed", 0)
            summary["generic"] = failed

        return summary

    except Exception as e:
        console.print(f"[red]Error parsing Checkov report: {e}[/red]")
        return {}

def main():
    parser = argparse.ArgumentParser(description="SecurePipe - Lightweight DevSecOps Security Scanner")
    parser.add_argument("--repo", required=True, help="Path to local repo directory")
    args = parser.parse_args()

    os.makedirs("reports", exist_ok=True)

    # --- Run Bandit ---
    bandit_out, bandit_err, bandit_code = run_bandit(args.repo)
    with open("reports/bandit_console.log", "w") as f:
        f.write(bandit_out or "")
        f.write(bandit_err or "")
    if bandit_code != 0:
        console.print(f"[red]❌ Bandit failed: {bandit_err}[/red]")

    # --- Run Checkov ---
    checkov_out, checkov_err, checkov_code = run_checkov(args.repo)
    with open("reports/checkov_console.log", "w") as f:
        f.write(checkov_out or "")
        f.write(checkov_err or "")
    if checkov_code != 0:
        console.print(f"[red]❌ Checkov failed: {checkov_err}[/red]")

    # --- Summarize results ---
    bandit_issues = summarize_bandit()
    checkov_issues = summarize_checkov()

    
    # --- Print summary table ---
    table = Table(title="🔒 SecurePipe Scan Summary", show_header=True, header_style="bold magenta")
    table.add_column("Tool", justify="center")
    table.add_column("Issues Found", justify="center")
    table.add_column("Report Path", justify="center")

    table.add_row("Bandit", str(bandit_issues), "reports/bandit_report.json")
    # table.add_row("Checkov", str(checkov_issues), "reports/results_json.json")

    if not checkov_issues:
        console.print("[yellow]⚠️  No IaC files detected for Checkov. Add Terraform, YAML, or Docker files to scan.[/yellow]")
    else:
        for check_type, failed_count in checkov_issues.items():
            table.add_row(f"Checkov ({check_type})", str(failed_count), "reports/results_json.json")

    console.print("\n")
    console.print(table)
    console.print("\n[green]✅ Scanning complete! Reports saved in ./reports[/green]")


if __name__ == "__main__":
    main()
