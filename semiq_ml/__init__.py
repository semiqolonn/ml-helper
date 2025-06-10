"""
Semiq-ML helper Package

This package provides helper functions and classes to simplify common machine learning workflows,
including baseline model training and hyperparameter tuning.
"""

__version__ = "0.2.1"

# Import main classes for easy access
from .baseline_model import BaselineModel
from .tuning import OptunaOptimizer

# Define what's available when using "from ml_helper import *"
__all__ = [
    'BaselineModel',
    'OptunaOptimizer',
]