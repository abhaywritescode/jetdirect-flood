# jetdirect-flood

This repository contains an educational tool demonstrating a resource exhaustion vulnerability in legacy printer protocols. It is designed to illustrate why exposing raw printing ports on modern networks is a security risk.

⚠️ **Disclaimer:** This code is for educational and authorized auditing purposes only. Do not use this against networks or devices you do not own or do not have explicit permission to test.

## 📌 Vulnerability Overview

Legacy network printers often rely on JetDirect (TCP Port 9100) for receiving raw print jobs. Because this protocol was designed for frictionless local network printing, it inherently lacks authentication and robust connection management.

When a device rapidly cycles TCP connections and transmits malformed or junk data to port 9100, the printer's interpreter attempts to parse the invalid instructions. This can lead to:
* **Memory Exhaustion:** The printer's memory buffers or connection pools fill up.
* **Denial of Service (DoS):** The print spooler locks up, ignoring legitimate print jobs and rendering the network interface unresponsive until physically rebooted.
* **Resource Waste:** If parsed as text, the printer may continuously print garbage characters.
