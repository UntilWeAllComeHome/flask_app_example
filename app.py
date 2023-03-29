from flask import Flask
import geopandas as gpd
from shapely.geometry import Polygon

app = Flask(__name__)

@app.route('/')
def hello():
    return 'General API description here.'

@app.route('/calculate_center/<path:filepath>')
def calculate_center(filepath):
    """Calculates the center of a passed geosjon file."""

    gdf = gpd.read_file(('/' + filepath))
    center = gdf.dissolve().centroid
    return(str(center.to_json()))

@app.route('/calculate_bounds/<path:filepath>')
def calculate_bounds(filepath):
    """Calculates the total bounds of a passed geosjon file."""

    gdf = gpd.read_file(('/' + filepath))
    t_bounds = gdf.total_bounds
    return(str(t_bounds))

@app.route('/calculate_boundry/<path:filepath>')
def calculate_boundry(filepath):
    """Calculates the total bounds of a passed geosjon file."""

    gdf = gpd.read_file(('/' + filepath))
    bound = gdf.boundary

    return(str(bound.to_json()))

@app.route('/calculate_area/<path:filepath>')
def calculate_area(filepath):
    """Calculates the total bounds of a passed geosjon file."""

    gdf = gpd.read_file(('/' + filepath))
    area = gdf.area

    return(str(area))