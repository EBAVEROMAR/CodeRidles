import time

def get_roman_numerals():
    """Return a dictionary of Roman numerals for numbers 1 to 59."""
    roman_map = {
        1: "I", 2: "II", 3: "III", 4: "IV", 5: "V",
        6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X",
        11: "XI", 12: "XII", 13: "XIII", 14: "XIV", 15: "XV",
        16: "XVI", 17: "XVII", 18: "XVIII", 19: "XIX", 20: "XX",
        21: "XXI", 22: "XXII", 23: "XXIII", 24: "XXIV", 25: "XXV",
        26: "XXVI", 27: "XXVII", 28: "XXVIII", 29: "XXIX", 30: "XXX",
        31: "XXXI", 32: "XXXII", 33: "XXXIII", 34: "XXXIV", 35: "XXXV",
        36: "XXXVI", 37: "XXXVII", 38: "XXXVIII", 39: "XXXIX", 40: "XL",
        41: "XLI", 42: "XLII", 43: "XLIII", 44: "XLIV", 45: "XLV",
        46: "XLVI", 47: "XLVII", 48: "XLVIII", 49: "XLIX", 50: "L",
        51: "LI", 52: "LII", 53: "LIII", 54: "LIV", 55: "LV",
        56: "LVI", 57: "LVII", 58: "LVIII", 59: "LIX", 0: "nulla"
    }
    return roman_map

def convert_time_to_roman():
    """Fetch the current system time and convert it to Roman numerals."""
    roman_map = get_roman_numerals()
    
    while True:
        current_time = time.localtime()
        hours = current_time.tm_hour
        minutes = current_time.tm_min
        seconds = current_time.tm_sec

        roman_hours = roman_map.get(hours, str(hours))
        roman_minutes = roman_map.get(minutes, str(minutes))
        roman_seconds = roman_map.get(seconds, str(seconds))

        print(f"\rCurrent Time: {roman_hours}:{roman_minutes}:{roman_seconds}", end='', flush=True)
        time.sleep(1)

if __name__ == "__main__":
    convert_time_to_roman()
