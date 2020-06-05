#!/usr/bin/env python3

import pandas as pd
import numpy as np
flight=pd.read_csv('flightdelays.csv')
print('The first 3 of the ArrDelay data for the flights that depart from SFO:')
print(flight[flight['Origin']=='SFO']['ArrDelay'].head(3))
print('The top 3 Dest airports:')
print(flight['Dest'].value_counts().head(3))
