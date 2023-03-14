"""
python wrapper for whatsapp web. No Selenium nor gecko needed! 

setting up browser driver are not python-newcomers-friendly, and thus it makes your code soo laggy.

i knew that feeling. it was painful.

powered by golang based Whatsmeow WhatsApp library 'hopefully' 
will make this wrapper easy to use without sacrificing speed and perfomances.
"""

import os
import sys
import logging

from .whatsapp import WhatsApp

LOGGER = logging.getLogger()