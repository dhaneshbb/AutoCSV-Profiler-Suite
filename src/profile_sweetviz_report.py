import sys
import subprocess
import os
import pandas as pd

def install_missing_packages():
    """Installs required packages if they are not already installed."""
    required_packages = [
        "sweetviz",
        "pandas"
    ]

    for package in required_packages:
        package_name = package.split("==")[0] if "==" in package else package
        try:
            __import__(package_name.replace("-", "_"))  # Convert sweetviz to sweetviz for import check
        except ImportError:
            print(f"Installing missing package: {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def main():
    """Main function to generate the Sweetviz report."""
    install_missing_packages()  # Ensure required packages are installed

    import sweetviz as sv  # Import after ensuring installation

    if len(sys.argv) != 3:
        print("Usage: python script.py <path_to_csv_file> <delimiter>")
        sys.exit(1)

    csv_path = sys.argv[1]
    delimiter = sys.argv[2]

    try:
        # Load the CSV file
        df = pd.read_csv(csv_path, delimiter=delimiter)

        # Generate a Sweetviz report
        report = sv.analyze(df)

        # Save the report as an HTML file in the same directory as the CSV file
        report_file = os.path.join(os.path.dirname(csv_path), "sweetviz_report.html")
        report.show_html(filepath=report_file, open_browser=False)

        print(f"Sweetviz report saved to: {report_file}")

    except Exception as e:
        print(f"Error processing the file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
