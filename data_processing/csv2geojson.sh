#!/bin/bash

# command line args
inFile="$1"
outFile="$2"
longitude="$3"
latitude="$4"

# get layer name
lyrName=$(basename "$inFile")
lyrName=$(echo "$lyrName" | sed -e 's/.csv//g' )
# echo "${lyrName}"

# create vrt file
vrt='<OGRVRTDataSource>
    <OGRVRTLayer name="'$lyrName'">
        <SrcDataSource>'$inFile'</SrcDataSource>
        <GeometryType>wkbPoint</GeometryType>
        <LayerSRS>WGS84</LayerSRS>
        <GeometryField encoding="PointFromColumns" x="'$longitude'" y="'$latitude'"/>
    </OGRVRTLayer>
</OGRVRTDataSource>'
echo "$vrt" > tmp.vrt

# remove existing geojson file
if [ -f "$outFile.geojson" ]; then
    rm "$outFile.geojson"
fi

# create geojson from csv
ogr2ogr -f GeoJSON "$outFile.geojson" tmp.vrt

# cleanup tmp files
rm tmp.vrt

# ./csv2geojson.sh model_events.csv test location_longitude location_latitude
