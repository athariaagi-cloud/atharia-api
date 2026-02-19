# Nevermined Setup Guide (Local)

Since the VM can't reach Nevermined API directly, run this locally.

---

## Step 1: Get Your Info

From Nevermined Dashboard, find:
- **Builder Address** (your wallet connected to Nevermined)
- API Key: `live:eyJ...` ✅ (already have)

---

## Step 2: Install Dependencies

```bash
# On your local machine
pip install payments-py requests
```

---

## Step 3: Run Setup

```bash
# Set environment variables
export NVM_API_KEY="live:eyJhbGciOiJFUzI1NksifQ.eyJpc3MiOiIweDZCMTZEMGIzMzQ4MjQ1ODFCNGEyNEE0OUZkN2ZjYkQ2NTA5Q0U1ZGEiLCJzdWIiOiIweDlkOTk4ZGJjNjBkYUUwQWJENzQ0YzE2OGUzNTk3OTU2YTk5ZEMwNDQiLCJqdGkiOiIweDFlMDgzZTdmYzdmMDA2M2U2NTI0ZTk0NmY1MzQ5MzgzYWYwODUzOTM5M2VmMzFlMzQyNzE5MWM2NmEyN2I3YzUiLCJleHAiOjQ5MjcyNjg5MDksIm8xMXkiOiJzay1oZWxpY29uZS10cW5vNjRxLXl4NmVxcnEtdHBqeXJpcS1ybHY3aHVpIn0.FG5LIJ8NXGCZC17Ol9SLZfY3Nt03kGCPz1QF9DIFrlwaRd67p0ZkUNtRTsQlLeTID7w83jF6L8OvjABNqrtNfBs"

export BUILDER_ADDRESS="0xYourWalletAddressFromDashboard"

# Run
python /path/to/setup_local.py
```

---

## Step 4: What Happens

1. Nevermined registers your 4 services
2. Each gets Agent ID + Plan ID
3. Save these IDs for your API server

---

## Step 5: Deploy API Server

After registration, you'll have:
- Agent IDs
- Plan IDs

Use these to configure the payment middleware in server.py

---

## Alternative: Manual via Dashboard

You can also register agents manually via Nevermined Dashboard:
1. Go to nevermined.app/agents
2. Click "Register Agent"
3. Fill in details
4. Create pricing plan
5. Done!

No code needed! 🎯
