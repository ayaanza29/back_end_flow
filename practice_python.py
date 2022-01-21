"""
import rpy2


pi = robjects.r["pi"]
pi[0]"""

from cytopy.data.setup import global_init
global_init('MyDatabase')