"""
Nevermined Payments Integration - LIVE
"""

import os
import requests
import json

# LIVE API Key
NVM_API_KEY = "live:eyJhbGciOiJFUzI1NksifQ.eyJpc3MiOiIweDZCMTZEMGIzMzQ4MjQ1ODFCNGEyNEE0OUZkN2ZjYkQ2NTA5Q0U1ZGEiLCJzdWIiOiIweDlkOTk4ZGJjNjBkYUUwQWJENzQ0YzE2OGUzNTk3OTU2YTk5ZEMwNDQiLCJqdGkiOiIweDFlMDgzZTdmYzdmMDA2M2U2NTI0ZTk0NmY1MzQ5MzgzYWYwODUzOTM5M2VmMzFlMzQyNzE5MWM2NmEyN2I3YzUiLCJleHAiOjQ5MjcyNjg5MDksIm8xMXkiOiJzay1oZWxpY29uZS10cW5vNjRxLXl4NmVxcnEtdHBqeXJpcS1ybHY3aHVpIn0.FG5LIJ8NXGCZC17Ol9SLZfY3Nt03kGCPz1QF9DIFrlwaRd67p0ZkUNtRTsQlLeTID7w83jF6L8OvjABNqrtNfBs"

class NeverminedAPI:
    """Nevermined API Client"""
    
    def __init__(self):
        self.base_url = "https://api.nevermined.io"
        self.headers = {
            "Authorization": f"Bearer {NVM_API_KEY}",
            "Content-Type": "application/json"
        }
    
    def get_user_info(self):
        """Get current user info"""
        resp = requests.get(
            f"{self.base_url}/v1/users/me",
            headers=self.headers
        )
        return resp.json()
    
    def list_agents(self):
        """List registered agents"""
        resp = requests.get(
            f"{self.base_url}/v1/agents",
            headers=self.headers
        )
        return resp.json()
    
    def register_agent(self, name, description, endpoints):
        """Register a new agent"""
        data = {
            "name": name,
            "description": description,
            "tags": ["atharia", "ai", "service"],
            "endpoints": endpoints
        }
        resp = requests.post(
            f"{self.base_url}/v1/agents",
            headers=self.headers,
            json=data
        )
        return resp.json()
    
    def get_balance(self):
        """Get earnings balance"""
        resp = requests.get(
            f"{self.base_url}/v1/balance",
            headers=self.headers
        )
        return resp.json()

# Initialize
api = NeverminedAPI()

# Test connection
try:
    user_info = api.get_user_info()
    print("✅ Nevermined Connected!")
    print(f"User: {user_info}")
except Exception as e:
    print(f"❌ Error: {e}")
