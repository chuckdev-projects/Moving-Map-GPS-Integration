# Reads GPS data using gpsd (make sure gpsd is installed and running)
import gps

session = gps.gps(mode=gps.WATCH_ENABLE)

print("Reading GPS data (Ctrl+C to stop)...")
try:
    for report in session:
        if report['class'] == 'TPV':
            lat = getattr(report, 'lat', "Unknown")
            lon = getattr(report, 'lon', "Unknown")
            print(f"Lat: {lat}, Lon: {lon}")
except KeyboardInterrupt:
    print("\nStopped")
