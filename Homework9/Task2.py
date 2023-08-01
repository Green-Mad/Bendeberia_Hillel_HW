class Worker:
    """A class representing a worker."""

    def __init__(self, name, company, position):
        """Initialize the worker."""
        self.name = name
        self.company = company
        self.position = position

    def __repr__(self):
        """Return a string representation of the worker."""
        return f"Worker(name={self.name}, company={self.company}, position={self.position})"

    @property
    def full_name(self):
        """Return the full name of the worker."""
        return f"{self.name} ({self.company})"

    # Class attributes
    num_workers = 0

    # Class method
    @classmethod
    def get_total_number_of_workers(cls):
        """Return the total number of workers across all companies."""
        return sum(worker.num_workers for worker in cls._workers)

    # Static method
    @staticmethod
    def is_worker_valid(name, company, position):
        """Return True if the worker is valid, False otherwise."""
        if not isinstance(name, str):
            return False
        if not isinstance(company, str):
            return False
        if not isinstance(position, str):
            return False
        return True
