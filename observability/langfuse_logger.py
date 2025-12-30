class LangfuseLogger:
    """
    Stubbed Langfuse logger.
    Observability is architecturally integrated but disabled for local demo
    due to dependency conflicts.
    """

    def __init__(self):
        self.enabled = False
        print("Langfuse disabled (demo-safe mode)")

    def log_agent_call(self, *args, **kwargs):
        return


# Global instance
logger = LangfuseLogger()