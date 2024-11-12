import numpy as np
data_type = [("Name", "S20"), ("Age", int), ("Class", float)]
Details = [("Drohn", 14, 1.1), ("Prasham", 15, 2.3), ("Ronak", 15, 8.1)]
DisplayDetails = np.array(Details, dtype = data_type)
print(DisplayDetails)
print(np.sort(DisplayDetails, order="Age"))
print(np.sort(DisplayDetails, order="Class"))