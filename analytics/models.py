from django.db import models
from users.models import User
# Entity Model
class Entity(models.Model):
    ENTITY_TYPES = [
        ('mine_owner', 'Mine Owner/Operator'),
        ('exploration', 'Exploration Company'),
        ('drilling', 'Drilling Service Provider'),
        ('equipment', 'Equipment Manufacturer'),
    ]
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True,default=True)
    entity_type = models.CharField(max_length=50, choices=ENTITY_TYPES)

    def __str__(self):
        return f"{self.name} ({self.get_entity_type_display()})"

# GeospatialData Model
class GeospatialData(models.Model):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, related_name="geospatial_data",default=1)
    location = models.CharField(max_length=255, default="Unknown")
    site_name = models.CharField(max_length=255, default="Unknown")
    site_type = models.CharField(max_length=255, default="Unknown")

    ortho = models.FileField(upload_to="geospatial/ortho/",null=True,blank=True)
    dem = models.FileField(upload_to="geospatial/dem/",null=True,blank=True)
    stockpile_geojson = models.FileField(upload_to="geospatial/stokpilegeojson/",null=True,blank=True)
    model_3d_ply = models.FileField(upload_to="geospatial/3dmodel/",null=True,blank=True)
    object_3d = models.FileField(upload_to="geospatial/3dobject/",null=True,blank=True)
    tin_ply = models.FileField(upload_to="geospatial/tin/",null=True,blank=True)
    pit_boundary_geojson = models.FileField(upload_to="geospatial/pitboundry/",null=True,blank=True)
    dem_boundary_geojson = models.FileField(upload_to="geospatial/demboundry/",null=True,blank=True)
    rainfall_data = models.FileField(upload_to="geospatial/rainfall/",null=True,blank=True)
    soil_raster = models.FileField(upload_to="geospatial/soilraster/",null=True,blank=True)
    water_depth = models.FileField(upload_to="geospatial/waterdepthjson/",null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.site_name} - {self.location}"
