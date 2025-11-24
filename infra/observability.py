import logging, sys
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from fastapi import Response

# Configure logger
logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s"
)

logger = logging.getLogger("flight_booking")

# Prometheus metrics
REQUESTS = Counter(
    "app_requests_total",
    "Total requests processed",
    ["service", "endpoint"]
)

LATENCY = Histogram(
    "app_request_latency_seconds",
    "Latency of each request in seconds",
    ["service", "endpoint"]
)

def incr(service: str, endpoint: str):
    """Increment request counter."""
    REQUESTS.labels(service=service, endpoint=endpoint).inc()

def observe(service: str, endpoint: str, seconds: float):
    """Record latency."""
    LATENCY.labels(service=service, endpoint=endpoint).observe(seconds)

def metrics_response():
    """Return all metrics in Prometheus format."""
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)
