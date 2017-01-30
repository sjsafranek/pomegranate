#ogr2ogr -f "ESRI Shapefile" liblines_proj2.shp wgs84.geojson -s_srs EPSG:4326 -t_srs EPSG:4326

ogr2ogr -f "GeoJSON" wgs84.geojson liblines_proj2.shp -s_srs EPSG:4326 -t_srs EPSG:4269

#ogr2ogr -f "GeoJSON" wgs84.geojson liblines_proj2.shp
