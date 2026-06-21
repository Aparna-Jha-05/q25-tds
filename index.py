from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
import numpy as np
import json

app = FastAPI()

# Enable CORS for POST from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok"}

@app.options("/api/latency")
async def options_handler():
    return Response(status_code=200)
TELEMETRY_DATA = json.loads("""

[
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 189.6,
    "uptime_pct": 97.852,
    "timestamp": 20250301
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 123.66,
    "uptime_pct": 97.616,
    "timestamp": 20250302
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 102.64,
    "uptime_pct": 97.288,
    "timestamp": 20250303
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 205.72,
    "uptime_pct": 97.825,
    "timestamp": 20250304
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 177.21,
    "uptime_pct": 99.271,
    "timestamp": 20250305
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 167.11,
    "uptime_pct": 98.179,
    "timestamp": 20250306
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 116.33,
    "uptime_pct": 98.018,
    "timestamp": 20250307
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 228.63,
    "uptime_pct": 97.954,
    "timestamp": 20250308
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 129.56,
    "uptime_pct": 97.229,
    "timestamp": 20250309
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 170.91,
    "uptime_pct": 98.527,
    "timestamp": 20250310
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 144.87,
    "uptime_pct": 98.133,
    "timestamp": 20250311
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 186.92,
    "uptime_pct": 97.455,
    "timestamp": 20250312
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 170.18,
    "uptime_pct": 97.444,
    "timestamp": 20250301
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 199.31,
    "uptime_pct": 97.29,
    "timestamp": 20250302
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 162.67,
    "uptime_pct": 97.655,
    "timestamp": 20250303
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 191.65,
    "uptime_pct": 97.649,
    "timestamp": 20250304
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 129.06,
    "uptime_pct": 98.694,
    "timestamp": 20250305
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 214.99,
    "uptime_pct": 98.026,
    "timestamp": 20250306
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 128.1,
    "uptime_pct": 99.471,
    "timestamp": 20250307
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 173.92,
    "uptime_pct": 97.384,
    "timestamp": 20250308
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 154.05,
    "uptime_pct": 99.236,
    "timestamp": 20250309
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 142.71,
    "uptime_pct": 99.266,
    "timestamp": 20250310
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 200.59,
    "uptime_pct": 98.339,
    "timestamp": 20250311
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 174.36,
    "uptime_pct": 97.447,
    "timestamp": 20250312
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 221.86,
    "uptime_pct": 98.366,
    "timestamp": 20250301
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 231.7,
    "uptime_pct": 98.909,
    "timestamp": 20250302
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 116.6,
    "uptime_pct": 98.872,
    "timestamp": 20250303
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 195.17,
    "uptime_pct": 98.149,
    "timestamp": 20250304
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 171.9,
    "uptime_pct": 98.769,
    "timestamp": 20250305
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 147.61,
    "uptime_pct": 98.945,
    "timestamp": 20250306
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 172.46,
    "uptime_pct": 99.341,
    "timestamp": 20250307
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 202.66,
    "uptime_pct": 97.657,
    "timestamp": 20250308
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 187.22,
    "uptime_pct": 97.874,
    "timestamp": 20250309
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 215.06,
    "uptime_pct": 98.278,
    "timestamp": 20250310
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 199.14,
    "uptime_pct": 98.006,
    "timestamp": 20250311
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 172.49,
    "uptime_pct": 97.127,
    "timestamp": 20250312
  }
]
""")

@app.post("/api/latency")
async def latency_analytics(request: Request):
    body = await request.json()
    regions = body.get("regions", [])
    threshold_ms = body.get("threshold_ms", 180)

    results = []
    for region in regions:
        records   = [r for r in TELEMETRY_DATA if r["region"] == region]
        latencies = [r["latency_ms"] for r in records]
        uptimes   = [r["uptime_pct"]  for r in records]
        results.append({
            "region":      region,
            "avg_latency": round(float(np.mean(latencies)), 2),
            "p95_latency": round(float(np.percentile(latencies, 95)), 2),
            "avg_uptime":  round(float(np.mean(uptimes)), 3),
            "breaches":    int(sum(1 for l in latencies if l > threshold_ms))
        })

    return {"regions": results}
