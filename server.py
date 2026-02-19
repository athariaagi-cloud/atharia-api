"""
Atharia Agentic Economy API Server
With Nevermined Payment Middleware
"""

from fastapi import FastAPI, HTTPException, Header, Request
from pydantic import BaseModel
from typing import Optional, List
import hashlib
import json
import os

app = FastAPI(title="Atharia Research API", version="1.0.0")

# NEVERMINED CONFIG
AGENT_ID = "90862586690191347294032671324260442607070963070407937654954874312956772111573"
NVM_API_KEY = "live:eyJhbGciOiJFUzI1NksifQ.eyJpc3MiOiIweDZCMTZEMGIzMzQ4MjQ1ODFCNGEyNEE0OUZkN2ZjYkQ2NTA5Q0U1ZGEiLCJzdWIiOiIweDlkOTk4ZGJjNjBkYUUwQWJENzQ0YzE2OGUzNTk3OTU2YTk5ZEMwNDQiLCJqdGkiOiIweDFlMDgzZTdmYzdmMDA2M2U2NTI0ZTk0NmY1MzQ5MzgzYWYwODUzOTM5M2VmMzFlMzQyNzE5MWM2NmEyN2I3YzUiLCJleHAiOjQ5MjcyNjg5MDksIm8xMXkiOiJzay1oZWxpY29uZS10cW5vNjRxLXl4NmVxcnEtdHBqeXJpcS1ybHY3aHVpIn0.FG5LIJ8NXGCZC17Ol9SLZfY3Nt03kGCPz1QF9DIFrlwaRd67p0ZkUNtRTsQlLeTID7w83jF6L8OvjABNqrtNfBs"

# SERVICE CONFIG
SERVICES = {
    "research": {
        "name": "Atharia Research",
        "price": 0.10,  # /bin/bash.10 per request
        "description": "Query 440+ AI research articles"
    },
    "scrape": {
        "name": "Atharia Stealth Scraper", 
        "price": 0.20,
        "description": "Undetectable web scraping"
    },
    "verify": {
        "name": "Atharia Verification",
        "price": 0.15,
        "description": "Fact verification service"
    }
}

# === HELPER FUNCTIONS ===

async def verify_payment(x_payment_token: Optional[str] = Header(None)) -> bool:
    """Verify payment via Nevermined"""
    if not x_payment_token:
        return False
    # In production: call Nevermined API to verify
    # For now: check if token exists
    return True

def build_payment_required(plan_id: str, endpoint: str):
    """Build payment requirement spec"""
    return {
        "planId": plan_id,
        "endpoint": endpoint,
        "agentId": AGENT_ID
    }

# === ROUTES ===

@app.get("/")
async def root():
    return {
        "service": "Atharia Research API",
        "version": "1.0.0",
        "status": "active",
        "agent_id": AGENT_ID,
        "nevermined": "connected"
    }

@app.get("/health")
async def health():
    return {"status": "healthy"}

# === RESEARCH SERVICE ===

class ResearchQuery(BaseModel):
    query: str
    max_results: int = 5

@app.post("/research")
async def research_query(
    request: ResearchQuery,
    x_payment_token: Optional[str] = Header(None)
):
    """
    Query research articles.
    Price: /bin/bash.10 per request
    """
    # Check payment
    if not await verify_payment(x_payment_token):
        payment_req = build_payment_required(
            "basic-plan-id",  # Will be updated with real plan ID
            "/research"
        )
        return {
            "error": "Payment Required",
            "payment_required": payment_req,
            "price": "/bin/bash.10",
            "buy_at": f"https://nevermined.app/checkout/{AGENT_ID}"
        }
    
    # Search articles
    results = search_articles(request.query, request.max_results)
    
    return {
        "query": request.query,
        "results": results,
        "credits_used": 1,
        "cost": "/bin/bash.10"
    }

@app.post("/summarize")
async def summarize(
    text: str,
    x_payment_token: Optional[str] = Header(None)
):
    """Summarize content. Price: /bin/bash.15"""
    if not await verify_payment(x_payment_token):
        return {"error": "Payment Required", "price": "/bin/bash.15"}
    
    return {
        "summary": f"Summary of: {text[:50]}...",
        "credits_used": 1,
        "cost": "/bin/bash.15"
    }

# === HELPER ===

def search_articles(query: str, max_results: int) -> List[dict]:
    """Search our article database"""
    # In production: search /home/mangai_desain/workspace/articles
    return [
        {
            "title": "AI Agents in 2026 - Complete Guide",
            "snippet": f"Results for: {query}",
            "url": "/articles/ai-agents-2026.md",
            "relevance": 0.95
        },
        {
            "title": "Machine Learning Best Practices",
            "snippet": f"Content about: {query}",
            "url": "/articles/ml-practices.md",
            "relevance": 0.85
        }
    ][:max_results]

if __name__ == "__main__":
    import uvicorn
    print(f"🚀 Atharia API Server")
    print(f"Agent ID: {AGENT_ID}")
    uvicorn.run(app, host="0.0.0.0", port=8080)
