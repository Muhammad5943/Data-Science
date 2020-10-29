import pandas as pd

from sas7bdat import SAS7BDAT
with SAS7BDAT('music.sas7bdat') as file:
    sas_1 = file.to_data_frame()

data = pd.read_stata('music.dta')