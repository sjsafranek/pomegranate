ogr2ogr -f "ESRI Shapefile" liblines.shp wgs84.geojson -s_srs EPSG:4326 -t_srs EPSG:4326


ogr2ogr -f "GeoJSON" wgs84.geojson liblines.shp -s_srs EPSG:4326 -t_srs EPSG:3857