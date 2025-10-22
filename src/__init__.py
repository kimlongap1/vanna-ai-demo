"""
Vanna AI Demo Package

A comprehensive demonstration of Vanna AI with Google Gemini, PostgreSQL, and ChromaDB.
"""

from .config import config, Config
from .vanna_setup import VannaDemo, create_vanna_instance, setup_demo

__version__ = "1.0.0"
__author__ = "Vanna AI Demo Project"

__all__ = [
    'config',
    'Config', 
    'VannaDemo',
    'create_vanna_instance',
    'setup_demo'
]
