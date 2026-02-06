# Phantom Synapse - Silent TCP Port Scanner

Phantom Synapse is a fast and silent TCP port scanner, developed in Python, that allows checking whether specific TCP ports are open, closed, or filtered on a target host. The scanner uses the Scapy library to send TCP SYN packets and analyze responses to determine the port state.

## Features

- TCP port scanning
- Support for multiple hosts
- Support for port ranges
- Support for multiple ports
- Command-line interface (CLI)
- Colorized output for better visualization

## Requirements

- Python 3.x
- Python libraries: Scapy, Colorama, argparse

## Installation

To install Phantom Synapse, follow these steps:

1. Clone the repository: `git clone https://github.com/RobotEby/phantom-synapse.git`

## Usage

To use Phantom Synapse, run the main script with the following parameters:

```bash
sudo python3 core/main.py <host> -p <ports>
```

### Parameters

- `<host>`: Target host IP address or domain name
- `-p <ports>`: Port range or comma-separated list of ports

### Examples

1. Single port scan:

   ```bash
   sudo python3 core/main.py 192.168.1.1 -p 80
   ```

2. Multiple ports scan:

   ```bash
   sudo python3 core/main.py 192.168.1.1 -p 22,80,443
   ```

3. Port range scan:

   ```bash
   sudo python3 core/main.py 192.168.1.1 -p 1-1000
   ```

4. Multiple hosts scan:

   ```bash
   sudo python3 core/main.py 192.168.1.1,192.168.1.2 -p 80
   ```

5. Multiple hosts with port range scan:
   ```bash
   sudo python3 core/main.py 192.168.1.1,192.168.1.2 -p 1-1000
   ```

## Source Code

The source code for Phantom Synapse is available at the GitHub repository: https://github.com/RobotEby/phantom-synapse

## Contributions

Contributions are welcome! To contribute, follow these steps:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/new-feature`
3. Commit changes: `git commit -m 'Add new feature'`
4. Push to the branch: `git push origin feature/new-feature`
5. Create a Pull Request

## License

Phantom Synapse is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contact

For questions or suggestions, contact the project author.
