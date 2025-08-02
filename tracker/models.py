from django.db import models

class Device(models.Model):
    device_id = models.CharField(max_length=100, unique=True)  # e.g., "DEV001"
    name = models.CharField(max_length=50)
    registered_at = models.DateTimeField(auto_now_add=True)  # Timestamp when device is registered

    def __str__(self):
        return self.device_id

class LocationData(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)  # Link to Device
    latitude = models.DecimalField(max_digits=9, decimal_places=6)  # High precision for GPS
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    speed = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Optional
    timestamp = models.DateTimeField(auto_now_add=True)  # Auto-set when data is added

    def __str__(self):
        return f"{self.device.device_id} at {self.timestamp}"


