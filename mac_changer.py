import subprocess
import optparse
import re


def get_user_input():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to be changed")
    parser.add_option("-m", "--mac", dest="mac_address", help="new MAC address")
    return parser.parse_args()


def change_mac_address(interface, mac_address):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
    subprocess.call(["ifconfig", interface, "up"])


def control_new_mac(interface):
    ifconfig_output = subprocess.check_output(["ifconfig", interface]).decode("utf-8")
    mac_address_match = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_output)

    if mac_address_match:
        return mac_address_match.group(0)
    else:
        return None


if __name__ == "__main__":
    user_input, _ = get_user_input()
    change_mac_address(user_input.interface, user_input.mac_address)
    finalized_mac = control_new_mac(user_input.interface)

    if finalized_mac == user_input.mac_address:
        print(f"Success! Your {user_input.interface}'s MAC address is now {user_input.mac_address}")
    else:
        print("Error!")
