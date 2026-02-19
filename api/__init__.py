"""
Agentic Economy API Services
Monetizing AI-to-AI services via Nevermined & Virtuals
"""

SERVICES = {
    "data": {
        "name": "Data Provider",
        "description": "Real-time data access for AI agents",
        "price_per_call": 0.01,  # USDC
        "endpoints": ["/api/prices", "/api/news", "/api/trends"]
    },
    "research": {
        "name": "Research Service", 
        "description": "Knowledge retrieval from 440+ articles",
        "price_per_call": 0.005,
        "endpoints": ["/api/query", "/api/summarize"]
    },
    "scrape": {
        "name": "Stealth Web",
        "description": "Undetectable web scraping",
        "price_per_call": 0.02,
        "endpoints": ["/api/scrape"]
    },
    "verify": {
        "name": "Verification Oracle",
        "description": "Truth verification service",
        "price_per_call": 0.015,
        "endpoints": ["/api/verify"]
    }
}

def get_service(name):
    return SERVICES.get(name)

def list_services():
    return SERVICES
