import phonenumbers
from phonenumbers import geocoder, timezone, carrier
import folium
import argparse
import os
from opencage.geocoder import OpenCageGeocode
from colorama import init, Fore

init()

def process_number(number):
    try:
        global location
        parsed_number = phonenumbers.parse(number)
        print(f"{Fore.GREEN}[+] Attempting to track location of "
              f"{phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}..")

        print(f"{Fore.GREEN}[+] Time Zone ID: {timezone.time_zones_for_number(parsed_number)}")

        location = geocoder.description_for_number(parsed_number, "en")
        if location:
            print(f"{Fore.GREEN}[+] Region: {location}")
        else:
            print(f"{Fore.RED}[-] Region: Unknown")

        if carrier.name_for_number(parsed_number, 'en'):
            print(f"{Fore.GREEN}[+] Service Provider: {carrier.name_for_number(parsed_number, 'en')}")
        else:
            pass
    except Exception:
        print(f"{Fore.RED}[-] Please specify a valid phone number (with country code) "
              "or check your internet connection.")
        sys.exit()

def get_approx_coordinates():
    global coder, latitude, longitude
    try:
        coder = OpenCageGeocode("42c84373c47e490ba410d4132ae64fc4")
        query = location
        results = coder.geocode(query)
        latitude = results[0]['geometry']['lat']
        longitude = results[0]['geometry']['lng']

        address = coder.reverse_geocode(latitude, longitude)
        if address:
            address = address[0]['formatted']
            print(f"{Fore.LIGHTRED_EX}[+] Approximate Location is {address}")
        else:
            print(f"{Fore.RED}[-] No address found for the given coordinates.")
    except Exception:
        print(f"{Fore.RED}[-] Could not get the location of this number. "
              "Please specify a valid phone number or check your internet connection.")
        sys.exit()

def clean_phone_number(phone_number):
    cleaned = ''.join(char for part in phone_number for char in part if char.isdigit() or char == '+')
    return cleaned or "unknown"

def draw_map():
    try:
        my_map = folium.Map(location=[latitude, longitude], zoom_start=9)
        folium.Marker([latitude, longitude], popup=location).add_to(my_map)

        cleaned_phone_number = clean_phone_number(args.phone_number)
        file_name = f"{cleaned_phone_number}.html"

        my_map.save(file_name)
        print(f"[+] See Aerial Coverage at: {os.path.abspath(file_name)}")
    except NameError:
        print(f"{Fore.RED}[-] Could not get Aerial coverage for this number. "
              "Please check the number again.")

def cli_argument():
    parser = argparse.ArgumentParser(description="Get approximate location of a Phone number.")
    parser.add_argument("-p", "--phone", dest="phone_number", type=str,
                        help="Phone number to track. Please include the country code when specifying the number.",
                        required=True, nargs="+")
    argument = parser.parse_args()

    if not argument.phone_number:
        print(f"{Fore.RED}[-] Please specify the phone number to track (including country code)."
              " Use --help to see usage.")
        sys.exit()

    return argument

args = cli_argument()
process_number("".join(args.phone_number))
get_approx_coordinates()
draw_map()
