import json
import requests
import time
import subprocess
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)  # Initialize colorama for colored output

# Define sound file paths
SOUND_OK = "OK.mp3"
SOUND_ERROR = "ERROR.mp3"
SOUND_WARNING = "StatusWarning.mp3"

def get_timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def play_sound(sound_file):
    command = f'vlc --play-and-exit "{sound_file}"'
    subprocess.Popen(command, shell=True)

def remove_unicode_chars(text):
    # Replace or remove Unicode characters that can't be displayed in the Windows console
    return text.encode("ascii", "ignore").decode()

def check_website_health(url):
    timestamp = get_timestamp()  # Initialize timestamp here
    try:
        response = requests.get(url)
        if response.status_code == 200:
            status = f"{Fore.GREEN} ✓ Website is up! ✓ {Style.RESET_ALL} Response time: {response.elapsed.total_seconds()} seconds"
            #play_sound(SOUND_OK)  # Play OK sound
        else:
            status = f"{Fore.YELLOW}Warning Website returned status code {response.status_code}{Style.RESET_ALL}"
            play_sound(SOUND_WARNING)  # Play warning sound
        formatted_status = f"{timestamp} - {url}: {status}\n"
        formatted_status = remove_unicode_chars(formatted_status)
        print(formatted_status)
        return formatted_status
    except requests.ConnectionError:
        status = f"{Fore.RED}Website is down!{Style.RESET_ALL}"
        play_sound(SOUND_ERROR)  # Play error sound
        formatted_status = f"{timestamp} - {url}: {status}\n"
        formatted_status = remove_unicode_chars(formatted_status)
        print(formatted_status)
        return formatted_status

def save_status_to_file(status, filename):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(status)

def main():
    try:
        # Get URLs and check_interval_seconds from JSON file
        with open("website_monitor.json", "r") as f:
            config = json.load(f)
            website_urls = config["urls"]
            check_interval_seconds = config["check_interval_seconds"]

        while True:
            for url in website_urls:
                status = check_website_health(url)
                save_status_to_file(status, "status.txt")  # Save status to a text file
                countdown = check_interval_seconds
                while countdown > 0:
                    print(f"{Fore.CYAN}Next check Will Start in {countdown} seconds...{Style.RESET_ALL}", end='\r')
                    time.sleep(1)
                    countdown -= 1

                # Clear the old countdown line by printing spaces
                print(' ' * 60, end='\r')
                print()
                time.sleep(1)  # A brief pause for readability

    except KeyboardInterrupt:
        print("Program Terminated Successfully.")

if __name__ == "__main__":
    main()
