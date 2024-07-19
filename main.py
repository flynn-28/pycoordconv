import re

def convert(degrees, minutes, seconds, direction):
    decimal_degrees = degrees + minutes / 60 + seconds / 3600
    if direction in ['S', 'W']:
        decimal_degrees *= -1
    return decimal_degrees

def parse_dms(dms_str):
    dms_str = dms_str.replace("°", " deg")
    pattern = re.compile(r"(\d+)\s*deg\s*(\d+)'\s*([\d\.]+)\"\s*([NSEW])")
    matches = pattern.findall(dms_str)
    if not matches or len(matches) != 2:
        raise ValueError("Invalid DMS format")
    
    coordinates = []
    for match in matches:
        degrees, minutes, seconds, direction = match
        dd = convert(float(degrees), float(minutes), float(seconds), direction)
        coordinates.append(dd)
    
    return coordinates

def main():
    dms_input = input("Enter DMS Coordinates (Example: 35° 39' 56.27\" N, 139° 41' 32.50\" E): ")
    try:
        coordinates = parse_dms(dms_input)
        print(f"{coordinates[0]}° {coordinates[1]}°")
    except ValueError as e:
        print(str(e))

if __name__ == "__main__":
    main()
