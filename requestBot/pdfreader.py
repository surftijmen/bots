import pandas as pd
import tabula
from tabulate import tabulate

tabula.convert_into("requestBot/zs.pdf", "requestBot/output.csv", output_format="csv",  lattice=True, stream=False, pages='all')

file = open("requestBot/output.csv", encoding="ISO-8859-1")
data=pd.read_csv(file)

