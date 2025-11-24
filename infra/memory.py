from google.adk.sessions import InMemorySessionService

class MemoryBank:
    """
    A simple key-value store to attach additional long-term memory
    to user sessions beyond what ADK provides.
    """
    def __init__(self):
        self._storage = {}

    def set(self, session_id: str, key: str, value):
        if session_id not in self._storage:
            self._storage[session_id] = {}
        self._storage[session_id][key] = value

    def get(self, session_id: str, key: str, default=None):
        return self._storage.get(session_id, {}).get(key, default)

    def dump(self, session_id: str):
        """Optional: return all memory for debugging."""
        return self._storage.get(session_id, {})

# This is the primary memory bank used by all agents
memory_bank = MemoryBank()

# ADK's built-in stateful session service
session_service = InMemorySessionService()
