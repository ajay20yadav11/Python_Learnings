import re
import ipaddress
from collections import defaultdict


class LogAnalysis:
	def __init__(self, log_entry: str):

		self.log_entry = log_entry
		self.analysis, self.log_message, self.user, self.source_ip = "", "", "", ""

	def checking_logs(self) -> None:
		"""
		Example 1: checking_logs()

			input: %SYS-5-CONFIG_I: Configured from console by user1 on vty0 (192.168.1.10)

			output:

				Log Message (e.g., "%SYS-5-CONFIG_I")
				User (e.g., "user1")
				Source IP Address (e.g., "192.168.1.10")

		"""
		ip_pattern = r'(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
		re_pattern = rf'%(.*):.*by\s+(.*?)\s+on\s+vty0.*?({ip_pattern}).*'
		matches = re.search(re_pattern, self.log_entry)
		print(f'Log Message ({matches.group(1)})\nUser "{matches.group(2)}"\nSource IP Address ({matches.group(3)})')
		return

	def checking_connection_status(self) -> None:
		"""
		Example 2: checking_connection_status()

			input: [2023-09-15 14:30:00] Device 192.168.1.1: Connection established.
					[2023-09-15 14:31:15] Device 192.168.2.2: Connection lost.
					[2023-09-15 14:32:30] Device 192.168.1.1: Connection lost.
					[2023-09-15 14:33:45] Device 192.168.2.2: Connection established.

			output: {
			    "connections_established": 2,
			    "connections_lost": 2,
			    "most_frequent_device": "192.168.2.2"
				}
		"""
		ip_pattern = r'(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?\.)){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
		regex_pattern = rf'Device.*?({ip_pattern}):\s+(.*)'

		consize_log = {}
		output = {}
		track_ip = {}

		for index, log in enumerate(self.log_entry.splitlines()):
			matches = re.search(regex_pattern, log)
			consize_log.setdefault(matches.group(2), [])
			consize_log[matches.group(2)].append(matches.group(1))
			track_ip.setdefault(matches.group(1), 0)
			track_ip[matches.group(1)] += 1

		output = {conn: len(ips) for conn, ips in consize_log.items()}
		most_frequent_connection = max(track_ip, key=track_ip.get)

		output.setdefault('most_frequent_connection', most_frequent_connection)
		print(output)
		return


if __name__ == '__main__':
	raw_log = '%SYS-5-CONFIG_I: Configured from console by user1 on vty0 (192.168.1.10)'
	raw_log = """[2023-09-15 14:30:00] Device 192.168.1.1: Connection established.
[2023-09-15 14:31:15] Device 192.168.2.2: Connection lost.
[2023-09-15 14:32:30] Device 192.168.1.1: Connection lost.
[2023-09-15 14:32:30] Device 192.168.1.1: Connection lost.
[2023-09-15 14:33:45] Device 192.168.2.2: Connection established."""
	analyze_logs = LogAnalysis(raw_log)
	analyze_logs.checking_connection_status()
