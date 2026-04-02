n = int(input())

ph = {}

for _ in range(n):
	cmd = input().split()

	if cmd[0] == "ADD":
		name = cmd[1]
		phone = cmd[2]
		ph[name] = phone

	elif cmd[0] == "REMOVE":
		name = cmd[1]
		ph.pop(name, None)

	elif cmd[0] == "DISPLAY":
		if not ph:
			print("No contacts")
		else:
			for name in sorted(ph.keys()):
				print(f"{name}: {ph[name]}")
