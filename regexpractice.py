import re
from pprint import pprint



# To match IP adddress

# animated = """The IP address of Google is 192.168.0.1
# ip address 10.0.0.1 interface 0
# The IP address of Google is 172.16.254.1
# This could be invalid, 172.16.254.260
# This could be invalid, 256.168.0.1
# ip address 192.168.0.200 interface 0
# This could be invalid, 192.168.0.300"""


# animated = animated.splitlines()

# ip_regex = r'\b(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-5]{2})(?:\.(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-5]{2})){3}\b'
# valid = []

# for anim in animated:
# 	valid.append(re.findall(ip_regex, anim))

# print(valid)


# response = """
# Interface IP-Address OK? Method Status Protocol 
# eth1/0 10.108.00.5 YES NVRAM up up 
# eth0/0 10.108.200.5 YES NVRAM up up 
# ethernet0/1 10.108.100.5 YES NVRAM down up 
# eth3/2 10.108.40.5 YES NVRAM up up 
# eth2/1 10.108.100.5 YES manual down up
# """


# for anim in response.splitlines():
# 	match = re.findall(r"((?:eth|ethernet)[0-3]\/[0-3]).*((up|down))", anim)
# 	print(match)


# animated = """
# 2023-07-15 08:23:45 Connection established with IP 192.168.1.10
# 2023-07-15 08:25:12 Interface GigabitEthernet1/0/1 is down
# 2023-07-15 08:28:55 VLAN 20 configuration updated
# """

# output = [('2023-07-15 08:23:45', 'Connection established with IP 192.168.1.10'), ('2023-07-15 08:25:12', 'Interface GigabitEthernet1/0/1 is down'), ('2023-07-15 08:28:55', 'VLAN 20 configuration updated')]



# regex_pattern = r"(\d{4}(?:\-\d{2}){2}\s+\d{2}(?:\:\d{2}){2})(.*)"

# output = []


# for anim in animated.splitlines():
# 	temp = re.findall(regex_pattern, anim)
# 	if len(temp) > 0:
# 		output.append(temp[0])


# print(output)



# animated = """interface GigabitEthernet0/1
#   description Link to Server
#   ip address 192.168.1.1/24
#   no shutdown
# !
# interface GigabitEthernet0/2
#   description Link to Switch
#   ip address 192.168.2.1/24
#   no shutdown
# !"""


# output = [('GigabitEthernet0/1', 'description Link to Server\n  ip address 192.168.1.1/24\n  no shutdown\n'), ('GigabitEthernet0/2', 'description Link to Switch\n  ip address 192.168.2.1/24\n  no shutdown\n')]

# animated = [anim for anim in animated.split("!") if anim]

# output = []
# regex_pattern = r"interface (\S+)\n(.*)"

# for anim in animated:
# 	output.append(re.findall(regex_pattern, anim, re.DOTALL)[0])

# pprint(output)

# pattern = r'\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
# ip_addresses = re.findall(pattern, text)


# animated = """
# rule 101 {
#   action allow
#   source 192.168.1.0/24
#   destination 10.0.0.0/8
# }
# rule 202 {
#   action deny
#   source 10.0.0.0/8
#   destination 192.168.1.0/24
#   description Block Internal Traffic
# }
# """

# output = [('101', '  action allow\n  source 192.168.1.0/24\n  destination 10.0.0.0/8\n'), ('202', '  action deny\n  source 10.0.0.0/8\n  destination 192.168.1.0/24\n  description Block Internal Traffic\n')]


# regex_pattern = r"rule (\d+) \{((?:.|\n)*?)\n\}"

# output = re.findall(regex_pattern, animated, re.DOTALL)

# print(output)


# animated = """
# <a href="https://www.example.com">Example Website</a>
# <a href="https://www.example2.com">Another Example</a>
# <a href="https://www.example3.com">Yet Another Example</a>
# """


# output = """URL: https://www.example.com
# Link Text: Example Website

# URL: https://www.example2.com
# Link Text: Another Example

# URL: https://www.example3.com
# Link Text: Yet Another Example
# """


# regex_pattern = r'.\"(.*)\"\>(.*)\<'
# output = ""

# for anim in re.findall(regex_pattern, animated):
# 	print(anim)
# 	output += f"URL: {anim[0]}\n\bLink Text: {anim[1]}\n\n"

# print(output)



# animated = "((())())((()))"

# output = "Matches: ['()', '()', '()']"


# regex_pattern = "\(.?\)"

# print(re.findall(regex_pattern, animated))

# sop = {"(": ")"}

# left = 0

# while left < len(animated):
# 	if animated[left] in sop and animated[left+1] == sop[animated[left]]:
# 		print(left, left+1)
# 	left += 1



animated = [1, 2, 3, 3, 4, 5]

for anim, bnim in enumerate(animated):
	if bnim in animated[anim+1:] or bnim in animated[0:anim]:
		print(bnim)

