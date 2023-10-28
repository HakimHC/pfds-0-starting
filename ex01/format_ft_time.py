import time
from datetime import datetime

def main():
    seconds_since_epoch = time.time()
    scientific_notation = f"{seconds_since_epoch:.4e}"
    current_date = datetime.fromtimestamp(seconds_since_epoch).strftime('%b %d %Y')
    
    print(f"Seconds since January 1, 1970: {seconds_since_epoch:.4f} or {scientific_notation} in scientific notation")
    print(current_date)

if __name__ == "__main__":
    main()
