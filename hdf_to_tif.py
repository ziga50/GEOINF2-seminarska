import numpy as np
import os
import glob
from osgeo import gdal, gdalconst
from osgeo.gdalnumeric import *  
from osgeo.gdalconst import *

# input
rep_input = r"C:\Users\zigao\OneDrive - Univerza v Ljubljani\Documents\GEOINF2_podatki_hdf"

# output
rep_output = os.path.join(os.path.dirname(rep_input), 'images3_tif')

if not os.path.exists(rep_output):
    os.makedirs(rep_output)

list_images = glob.glob(os.path.join(rep_input, '*.hdf'))

for im in range(len(list_images)):
    image = gdal.Open(list_images[im]).GetSubDatasets()
    print(os.path.basename(list_images[im]))

    
    ndvi = image[0][0]
    ndvi_open = gdal.Open(ndvi)
    ndvi_band = ndvi_open.GetRasterBand(1)
    ndvi_array = ndvi_band.ReadAsArray().astype(np.int16)

    cols = ndvi_open.RasterXSize
    rows = ndvi_open.RasterYSize

    
    quality = image[0][0]
    quality_open = gdal.Open(quality)
    quality_band = quality_open.GetRasterBand(1)
    quality_array = quality_band.ReadAsArray().astype(np.int16)


    # GeoTIFF
    driver = gdal.GetDriverByName('GTIFF')
    driver.Register()

    output_path = os.path.join(rep_output, f"{os.path.basename(list_images[im])[:-4]}.tif")
    output_dataset = driver.Create(output_path, cols, rows, 1, gdal.GDT_Int16)

    CopyDatasetInfo(ndvi_open, output_dataset)
    output_band = output_dataset.GetRasterBand(1)
    output_band.SetNoDataValue(-3000)
    BandWriteArray(output_band, ndvi_array)

    
    del ndvi_array, output_dataset, image, output_band

                            


