import time
from datetime import datetime

seconds_since_epoch = time.time()

scientific_notation = f"{seconds_since_epoch:.4e}"

print(f"Seconds since January 1, 1970: {seconds_since_epoch:.4f} or {scientific_notation} in scientific notation")

current_date = datetime.fromtimestamp(seconds_since_epoch).strftime('%b %d %Y')

print(current_date)
