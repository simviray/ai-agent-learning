memory = open("agent_memory.txt", "w")

memory.write("BTC price checked.\n")
memory.write("AI decision: Buy\n")

memory.close()

print("Memory saved.")