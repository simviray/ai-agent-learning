import json

agent_data = {
    "agent_name": "BTC AI Agent",
    "model": "Qwen",
    "status": "Active",
    "confidence": 92
}

json_data = json.dumps(agent_data, indent=4)

print(json_data)