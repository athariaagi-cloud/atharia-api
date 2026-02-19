"""
Nevermined Setup Script - Atharia Services
"""

import os
import requests
from payments_py import Payments, PaymentOptions
from payments_py.plans import get_erc20_price_config, get_fixed_credits_config

# Configuration
NVM_API_KEY = os.environ.get("NVM_API_KEY", "live:eyJhbGciOiJFUzI1NksifQ.eyJpc3MiOiIweDZCMTZEMGIzMzQ4MjQ1ODFCNGEyNEE0OUZkN2ZjYkQ2NTA5Q0U1ZGEiLCJzdWIiOiIweDlkOTk4ZGJjNjBkYUUwQWJENzQ0YzE2OGUzNTk3OTU2YTk5ZEMwNDQiLCJqdGkiOiIweDFlMDgzZTdmYzdmMDA2M2U2NTI0ZTk0NmY1MzQ5MzgzYWYwODUzOTM5M2VmMzFlMzQyNzE5MWM2NmEyN2I3YzUiLCJleHAiOjQ5MjcyNjg5MDksIm8xMXkiOiJzay1oZWxpY29uZS10cW5vNjRxLXl4NmVxcnEtdHBqeXJpcS1ybHY3aHVpIn0.FG5LIJ8NXGCZC17Ol9SLZfY3Nt03kGCPz1QF9DIFrlwaRd67p0ZkUNtRTsQlLeTID7w83jF6L8OvjABNqrtNfBs")

# YOUR WALLET FROM NEVERMINED DASHBOARD
BUILDER_ADDRESS = "0x9d998dbc60daE0AbD744c168e3597956a99dC044"

# USDC on Base Mainnet
USDC_ADDRESS = '0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913'

def setup_atharia_services():
    payments = Payments.get_instance(
        PaymentOptions(
            nvm_api_key=NVM_API_KEY,
            environment='live'
        )
    )
    
    services = [
        {
            'name': 'Atharia Research',
            'description': 'Query 440+ AI research articles',
            'price': 0.005,
            'credits': 1000,
            'endpoint': 'https://your-domain.com/research'
        },
        {
            'name': 'Atharia Scraper',
            'description': 'Undetectable web scraping',
            'price': 0.02,
            'credits': 500,
            'endpoint': 'https://your-domain.com/scrape'
        },
        {
            'name': 'Atharia Verification',
            'description': 'Fact verification service',
            'price': 0.015,
            'credits': 500,
            'endpoint': 'https://your-domain.com/verify'
        },
        {
            'name': 'Atharia Data',
            'description': 'Real-time data feeds',
            'price': 0.01,
            'credits': 1000,
            'endpoint': 'https://your-domain.com/data'
        }
    ]
    
    for svc in services:
        print(f"Registering: {svc['name']}")
        try:
            result = payments.agents.register_agent_and_plan(
                agent_metadata={'name': svc['name'], 'description': svc['description'], 'tags': ['atharia', 'ai']},
                agent_api={'endpoints': [{'POST': svc['endpoint']}]},
                plan_metadata={'name': 'Basic', 'description': f"{svc['credits']} calls"},
                price_config=get_erc20_price_config(int(svc['price'] * 1_000_000), USDC_ADDRESS, BUILDER_ADDRESS),
                credits_config=get_fixed_credits_config(svc['credits'], 1),
                access_limit='credits'
            )
            print(f"  ✅ Agent ID: {result.get('agentId')}")
            print(f"  ✅ Plan ID: {result.get('planId')}")
        except Exception as e:
            print(f"  ❌ Error: {e}")

if __name__ == '__main__':
    print("🚀 Atharia Nevermined Setup")
    setup_atharia_services()
