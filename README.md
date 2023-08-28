# MAC Address Changer Script

This script allows you to change the MAC address of a specified network interface on a Unix-like operating system.

It utilizes the subprocess and re modules in Python for interacting with the system.

## Usage
1. Make sure you have Python installed on your system.

2. Open a terminal and navigate to the directory containing the script.

3. Run the script with the following command:



```sh
python mac_changer.py -i [interface] -m [new_mac_address]
```


Replace [interface] with the name of the network interface you want to modify (e.g., eth0, wlan0) and [new_mac_address] with the desired new MAC address in the format xx:xx:xx:xx:xx:xx.

## Example
To change the MAC address of the interface eth0 to 00:11:22:33:44:55, you would run:



```sh
python mac_changer.py -i eth0 -m 00:11:22:33:44:55
```


## Important Notes
The script requires administrative privileges to make changes. Run it with sudo or as the root user.

Changing the MAC address of a network interface can have legal and security implications. Make sure you have proper authorization to modify MAC addresses on your system.

This script is intended for educational and testing purposes. Use it responsibly and in compliance with your local laws and regulations.
