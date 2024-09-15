import speedtest
from termcolor import colored
from datetime import datetime
import os

# Define minimum speed thresholds in Mbps
MIN_DOWNLOAD_SPEED = # Set your minimum download speed in Mbps
MIN_UPLOAD_SPEED = # Set your minimum upload speed in Mbps

def get_desktop_path():
    # For macOS and Linux, desktop is typically located in the home directory
    return os.path.join(os.environ["HOME"], "Desktop")

def check_internet_speed():
    try:
        st = speedtest.Speedtest()

        # Get server list and choose the best server
        st.get_best_server()

        print("Performing download speed test...")
        download_speed = st.download() / 1_000_000  # Convert from bits per second to megabits per second (Mbps)

        print("Performing upload speed test...")
        upload_speed = st.upload() / 1_000_000  # Convert from bits per second to megabits per second (Mbps)

        ping = st.results.ping

        # Check download speed
        if download_speed < MIN_DOWNLOAD_SPEED:
            download_status = colored("below minimum", "red")
        else:
            download_status = colored("above minimum", "green")

        # Check upload speed
        if upload_speed < MIN_UPLOAD_SPEED:
            upload_status = colored("below minimum", "red")
        else:
            upload_status = colored("above minimum", "green")

        print(f"Download speed: {download_speed:.2f} Mbps - {download_status}")
        print(f"Upload speed: {upload_speed:.2f} Mbps - {upload_status}")
        print(f"Ping: {ping} ms")

        return download_speed, upload_speed, ping, download_status, upload_status

    except Exception as e:
        print(f"An error occurred: {e}")

def save_results_to_file(download_speed, upload_speed, ping, download_status, upload_status):
    # Get the current date and time for timestamping the file
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Define file path (Desktop)
    desktop_path = os.path.join(get_desktop_path(), "speedtest_results.txt")

    with open(desktop_path, "w") as file:
        file.write(f"Speed Test Results ({timestamp}):\n")
        file.write(f"Download speed: {download_speed:.2f} Mbps - {download_status}\n")
        file.write(f"Upload speed: {upload_speed:.2f} Mbps - {upload_status}\n")
        file.write(f"Ping: {ping} ms\n")

    print(f"Results saved to {desktop_path}")

if __name__ == "__main__":
    download_speed, upload_speed, ping, download_status, upload_status = check_internet_speed()
    save_option = input("Do you want to save the results to a file? (y/n): ").lower()

    if save_option == "y":
        save_results_to_file(download_speed, upload_speed, ping, download_status, upload_status)
