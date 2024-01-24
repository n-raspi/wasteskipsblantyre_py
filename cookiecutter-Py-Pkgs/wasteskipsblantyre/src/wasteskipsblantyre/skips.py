from importlib import resources
import pandas as pd

def skips():
	with resources.path("wasteskipsblantyre.data", "skips_November_2023.csv") as f:
		df = pd.read_csv(f)
	return df

def dictionary():
	with resources.path("wasteskipsblantyre.data", "dictionary.csv") as f:
		df = pd.read_csv(f)
	return df
