from ast import And
from osgeo import gdal
import numpy as np
import os


data_folder = r"C:\Users\zigao\OneDrive - Univerza v Ljubljani\Documents\krevs_23_clipped"
output_folder = r"C:\Users\zigao\OneDrive - Univerza v Ljubljani\Documents\VCI_krevs"  


min_raster = r"C:\Users\zigao\OneDrive - Univerza v Ljubljani\Documents\krevs_min_max\min_2000_2023.tif"
max_raster = r"C:\Users\zigao\OneDrive - Univerza v Ljubljani\Documents\krevs_min_max\max_2000_2023.tif"


min_ds = gdal.Open(min_raster)
max_ds = gdal.Open(max_raster)

# for loop
for raster in os.listdir(data_folder):
    if raster.endswith(".tif"):
        
        current_ds = gdal.Open(os.path.join(data_folder, raster))

        min_array = min_ds.GetRasterBand(1).ReadAsArray().astype(np.float32)
        max_array = max_ds.GetRasterBand(1).ReadAsArray().astype(np.float32)
        current_array = current_ds.GetRasterBand(1).ReadAsArray().astype(np.float32)

        # VCI20
        vci20 = (current_array < 20) And (current_array > 0.1) 

    
        geo_transform = current_ds.GetGeoTransform()
        projection = current_ds.GetProjection()

        
        output_raster = os.path.join(output_folder, f"VCI_{raster}")
        driver = gdal.GetDriverByName("GTiff")
        vci_ds = driver.Create(output_raster, current_ds.RasterXSize, current_ds.RasterYSize, 1, gdal.GDT_Float32)

        
        vci_ds.GetRasterBand(1).WriteArray(vci)

        
        vci_ds.SetGeoTransform(geo_transform)
        vci_ds.SetProjection(projection)

        
        vci_ds = None
        current_ds = None


min_ds = None
max_ds = None


