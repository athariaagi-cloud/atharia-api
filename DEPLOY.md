# Atharia Agentic Economy - Deployment Guide

## Agent Info (Nevermined)
- **Agent ID:** 90862586690191347294032671324260442607070963070407937654954874312956772111573
- **Checkout URL:** https://nevermined.app/checkout/90862586690191347294032671324260442607070963070407937654954874312956772111573
- **Plans:** Basic ($10/100 calls), Pro ($25/100 calls)

## Quick Deploy to Render.com

### Option 1: GitHub Deploy (Recommended)
1. Create GitHub repo: https://github.com/new
2. Push this code:
   ```bash
   cd agentic-economy
   git init
   git add .
   git commit -m "Atharia Research API"
   git remote add origin https://github.com/YOUR_USERNAME/atharia-api.git
   git push -u origin main
   ```
3. Go to https://render.com
4. Connect GitHub → Select repo
5. Create new Web Service:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn server:app --host 0.0.0.0 --port $PORT`
6. Deploy!

### Option 2: Manual Deploy
1. Clone repo locally
2. Run: `pip install -r requirements.txt`
3. Run: `python server.py`
4. Deploy to any Python hosting

## Environment Variables
Set in render dashboard:
- `NVM_API_KEY`: live:eyJ...
- `AGENT_ID`: 90862586690191347294032671324260442607070963070407937654954874312956772111573

## Update Endpoint URL
After deploying, update in Nevermined dashboard:
- Protected Endpoint: https://your-render-app.onrender.com/research

## Testing
```bash
curl -X POST https://your-app.onrender.com/research \
  -H "Content-Type: application/json" \
  -d '{"query": "AI agents"}'
```

## Expected Response (No Payment)
```json
{
  "error": "Payment Required",
  "price": "$0.10",
  "buy_at": "https://nevermined.app/checkout/..."
}
```

## Expected Response (With Payment)
```json
{
  "query": "AI agents",
  "results": [...],
  "credits_used": 1,
  "cost": "$0.10"
}
```
