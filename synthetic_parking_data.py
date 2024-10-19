import pandas as pd
import numpy as np

np.random.seed(42)

data_size = 20

hours = [8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 6, 7, 5, 10, 12, 14]  
days_of_week = [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6] 
location_ids = [1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 7, 8, 8, 9, 9, 10, 10] 
parking_lot_sizes = [100, 100, 100, 150, 150, 200, 200, 50, 50, 120, 120, 180, 250, 250, 75, 75, 90, 90, 60, 60]

vehicles_parked = [
    85, 95, 60, 110, 70, 90, 140, 30, 45, 110, 90, 150, 80, 140, 20, 40, 50, 75, 25, 50
]

availability = [(vehicles / lot_size < 0.75) for vehicles, lot_size in zip(vehicles_parked, parking_lot_sizes)]

df = pd.DataFrame({
    'hour': hours,
    'day_of_week': days_of_week,
    'location_id': location_ids,
    'parking_lot_size': parking_lot_sizes,
    'vehicles_parked': vehicles_parked,
    'availability': availability
})

df.to_csv('realistic_parking_data.csv', index=False)

print(df.head())
