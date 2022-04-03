from shutil import move
import arcpy
import os
from arcpy import env
from arcpy.sa import *
import numpy as np

#set project_dir
proj_dir = r"C:\GEOS456\FP"
#define name of gdb
gdb = "nairobi.gdb"

print("Processing has started")

print("Gdb created at", gdb)

#aprx = arcpy.mp.ArcGISProject("C:\GEOS456\FP\FinalProject\FinalProject\FinalProject.aprx")

# arcpy.Exists(gdb):
arcpy.Delete_management("C:\GEOS456\FP\cypresshills.gdb")

#check if gdb present in the system
arcpy.CreateFileGDB_management(proj_dir, gdb)

#set the default gdb of the project
Default_gdb = proj_dir + gdb

print("Default gdb set to", Default_gdb)

proj_components = r""

#shape files 
points = proj_components + ""
buildings = proj_components + ""
landuse = proj_components + ""
waterways = proj_components + ""
nature = proj_components + ""
roads = proj_components + ""
counties = proj_components + ""

#csv files
movement_speeds = ""
#json files
sublocations = ""

#dem file
dem = ""

class ArcAnalysis():
    def __init__(self):
        arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("NAD_1983_UTM_Zone_12N")
        arcpy.env.cellSize = 25
        arcpy.env.overwriteOutput = True

    def shpToFeatures(self):
        self.roads = arcpy.FeatureClassToFeatureClass_conversion(in_features=roads, out_path=Default_gdb, out_name="roads")
        self.buildings = arcpy.FeatureClassToFeatureClass_conversion(in_features=buildings, out_path=Default_gdb, out_name="buildings")
        self.waterways = arcpy.FeatureClassToFeatureClass_conversion(in_features=waterways, out_path=Default_gdb, out_name="waterways")
        self.counties = arcpy.FeatureClassToFeatureClass_conversion(in_features=counties, out_path=Default_gdb, out_name="counties")
        self.points = arcpy.FeatureClassToFeatureClass_conversion(in_features=points, out_path=Default_gdb, out_name="points")
        self.landuse = arcpy.FeatureClassToFeatureClass_conversion(in_features=landuse, out_path=Default_gdb, out_name="landuse")
        self.nature = arcpy.FeatureClassToFeatureClass_conversion(in_features=nature, out_path=Default_gdb, out_name="nature")

        where_county= arcpy.AddFieldDelimiters(self.facilities, "UFI")
        where_county_expression = where_county + " = 'A21605053'"
        #create start and end_point

        self.county = arcpy.FeatureClassToFeatureClass_conversion(
            in_features=self.counties,
            out_path = Default_gdb,
            out_name = "nairobi",
            where_clause = where_county_expression
        )

    def jsonToRaster(self):
        self.sublocations = arcpy.JSONToFeatures_conversion(sublocations, "sublocations")

    def clipLayer(self):
        self.roads_nairobi = arcpy.Clip_analysis("roads", "nairobi", "roads_nairobi")

    def joinRoads(self):
        movement_speeds_hourly_nairobi_2020_3_csv = "C:\\Users\\macsakini\\Documents\\GitHub\\nairobi-transport-analysis\\data\\movement-speeds-hourly-nairobi-2020-3.csv"
        # Process: Add Join (Add Join) 
        self.speed_roads = arcpy.AddJoin_management("roads_nairobi", in_field="osm_id", join_table=movement_speeds, join_field="osm_way_id", join_type="KEEP_ALL")[0]


    def run(self):
        pass


if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace = Default_gdb, mask = rec_park_shp, workspace = Default_gdb):
            ArcAnalysis().run()