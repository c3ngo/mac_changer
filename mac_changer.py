import subprocess
import optparse
import re

ascii_art = """
       _____                      __  ___              ________                               
  ____|__  /____  ____ _____     /  |/  /___ ______   / ____/ /_  ____ _____  ____ ____  _____
 / ___//_ </ __ \/ __ `/ __ \   / /|_/ / __ `/ ___/  / /   / __ \/ __ `/ __ \/ __ `/ _ \/ ___/
/ /_____/ / / / / /_/ / /_/ /  / /  / / /_/ / /__   / /___/ / / / /_/ / / / / /_/ /  __/ /    
\___/____/_/ /_/\__, /\____/  /_/  /_/\__,_/\___/   \____/_/ /_/\__,_/_/ /_/\__, /\___/_/     
               /____/                                                      /____/
"""


def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface", dest="interface", help=" Interface to be changed")
    parse_object.add_option("-m", "--mac", dest="mac_address", help="New mac address")

    return parse_object.parse_args()


def change_mac_address(user_interface, user_mac_address):
    subprocess.call(["ifconfig", user_interface, "down"])
    subprocess.call(["ifconfig", user_interface, "hw", "ether", user_mac_address])
    subprocess.call(["ifconfig", user_interface, "up"])


def control_new_mac(interface):

    ifconfig = subprocess.check_output(["ifconfig", interface]).decode("utf-8")
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig)

    if new_mac:
        return new_mac.group(0)
    else:
        return None


print(ascii_art)


(user_input, arguments) = get_user_input()
change_mac_address(user_input.interface, user_input.mac_address)
finalized_mac = control_new_mac(user_input.interface)


if finalized_mac == user_input.mac_address:
    print("Success! " + "Your " + user_input.interface + "'s MAC address " + user_input.mac_address)
else:
    print("Error!")
