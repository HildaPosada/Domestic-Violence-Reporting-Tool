from enum import Enum


class ReportProgress(str, Enum):
    Submitted = "Submitted"
    InProcessing = "In processing"
    Resolved = "Resolved"
