import time as t

sec = t.time()
now = t.localtime(sec)

print("Seconds since January 1, 1970:", f"{sec:,.4f}", "or", f"{sec:.2e}", "in scientific notation")
print(t.strftime("%b %d %Y", now))