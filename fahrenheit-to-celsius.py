while True:
    f = input("Fahrenheit(or 'q' to quit): ")
    if f.lower() == 'q':
        break
    f=float(f) 
    c = (f - 32)* 5 /9
    print(f"{f} °F = {c:.1f} °C\n")