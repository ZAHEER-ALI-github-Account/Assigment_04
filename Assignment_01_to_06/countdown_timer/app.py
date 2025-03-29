import time

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02}:{secs:02}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    
    print("Time's up!")

if __name__ == "__main__":
    try:
        total_seconds = int(input("Enter the countdown time in seconds: "))
        countdown_timer(total_seconds)
    except ValueError:
        print("Please enter a valid number!")
