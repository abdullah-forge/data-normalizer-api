import tracemalloc, logging

class MemoryProfiler:
    def start(self):
        tracemalloc.start()
        logging.info("Memory tracking started.")
    def stop(self):
        current, peak = tracemalloc.get_traced_memory()
        logging.info(f"Peak memory usage: {peak / 10**6} MB")
        tracemalloc.stop()
        logging.info("Memory tracking stopped.")
