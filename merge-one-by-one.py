import os
import subprocess

#to se spremeni
data_folder = r"C:\Users\zigao\OneDrive - Univerza v Ljubljani\Documents\images3_tif"


rasters = [os.path.join(data_folder, raster) for raster in os.listdir(data_folder) if raster.endswith('.tif')]

# Output 
output_folder = r"C:\Users\zigao\OneDrive - Univerza v Ljubljani\Documents\Output"


for i in range(0, len(rasters), 2):
    if i + 1 < len(rasters):
        raster1 = rasters[i]
        raster2 = rasters[i + 1]
        
        
        output_raster = os.path.join(output_folder, f"merged_{i + 1}_{i + 2}.tif")
        
        # Merge 
        gdal_merge_cmd = f"gdal_merge.py -o {output_raster} {raster1} {raster2}"
        subprocess.call(gdal_merge_cmd, shell=True)
        print(f"Merged {raster1} and {raster2} into {output_raster}")










