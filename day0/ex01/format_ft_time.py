import time
import datetime

second = time.time()
secondf = f"{second:,.4f}"
seconds = f"{second:.2e}"
date = datetime.datetime.now().strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {secondf} or {seconds} in scientific notation")
print(date)
