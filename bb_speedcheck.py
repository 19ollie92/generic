import speedtest
from termcolor import colored
from datetime import datetime
import os

MIN_DOWNLOAD_SPEED = # Set your minimum download speed in Mbps
MIN_UPLOAD_SPEED = # Set your minimum upload speed in Mbps

def get_desktop_path():
    return os.path.join(os.environ["HOME"], "Desktop")

def check_internet_speed():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        print("Performing download speed test...")
        download_speed = st.download() / 1_000_000 
        print("Performing upload speed test...")
        upload_speed = st.upload() / 1_000_000  
        ping = st.results.ping
        if download_speed < MIN_DOWNLOAD_SPEED:
            download_status = colored("below minimum", "red")
        else:
            download_status = colored("above minimum", "green")
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
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
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
