import sqlite3, uuid, time, os

# Jobs database path
DB_PATH = os.path.join(os.path.dirname(__file__), "..", "database", "jobs.db")


def init_jobs_db():
    """Initialize the jobs database."""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        job_id TEXT PRIMARY KEY,
        session_id TEXT,
        state TEXT,
        payload TEXT,
        updated_at REAL
    )
    """)
    conn.commit()
    conn.close()


def create_job(session_id: str, payload: str):
    """Create a new long-running job."""
    job_id = uuid.uuid4().hex
    now = time.time()

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO jobs (job_id, session_id, state, payload, updated_at) VALUES (?, ?, ?, ?, ?)",
        (job_id, session_id, "PENDING", payload, now)
    )
    conn.commit()
    conn.close()

    return job_id


def update_job(job_id: str, state: str):
    """Update job state (PAUSED, RESUMED, CONFIRMED, etc.)."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "UPDATE jobs SET state = ?, updated_at = ? WHERE job_id = ?",
        (state, time.time(), job_id)
    )
    conn.commit()
    conn.close()


def get_job(job_id: str):
    """Retrieve job information."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "SELECT job_id, session_id, state, payload, updated_at FROM jobs WHERE job_id = ?",
        (job_id,)
    )
    row = cur.fetchone()
    conn.close()

    if not row:
        return {}

    return {
        "job_id": row[0],
        "session_id": row[1],
        "state": row[2],
        "payload": row[3],
        "updated_at": row[4]
    }
