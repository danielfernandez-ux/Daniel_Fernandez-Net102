
from netmiko import ConnectHandler

router_device = {
    'device_type': 'cisco_ios_telnet',
    'ip': '192.168.10.17',
    'port': 32770,
    'username': 'admin',
    'password': 'eve123',
    'secret': 'eve123',
}

try:
    print("Connecting to router...")

    net_connect = ConnectHandler(**router_device)

    print("Connected successfully!")

    # Enter privileged EXEC mode
    net_connect.enable()

    # Commands to execute
    command_to_run = [
        "show version",
        "show ip interface brief",
        "show running-config"
    ]

    # Execute each command
    for cmd in command_to_run:
        print(f"\n--- Output for: {cmd} ---")
        output = net_connect.send_command(cmd)
        print(output)

    # Disconnect from router
    net_connect.disconnect()

    print("\nDisconnected successfully.")

except Exception as e:
    print(f"Connection failed: {e}")
