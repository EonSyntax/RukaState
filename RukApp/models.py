from django.db import models

# Create your models here.

 #Dropdown choices
LISTING_TYPE_CHOICES = [
        ('rent', 'Rent'),
        ('sale', 'For Sale'),
    ]

PROPERTY_TYPE_CHOICES = [
        ('apartment','Apartment'),
        ('flat','Flat'),
        ('villa','Villa'),
    ]

RENT_DURATION_CHOICES = [
    ('month','Per Month'),
    ('year','Per Year',)
]



class Property(models.Model):
    property_name = models.TextField(max_length=50)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    property_size = models.DecimalField(max_digits=6, decimal_places=2)
    listing_type = models.CharField(max_length=10, choices=LISTING_TYPE_CHOICES)
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    year_built = models.PositiveIntegerField()
    garage = models.BooleanField(default=False)
    property_description = models.TextField()
    Features_and_amenities = models.TextField()
    rent_duration = models.CharField(max_length=10, choices=RENT_DURATION_CHOICES, blank=True, null=True)
    main_PropertyImage = models.ImageField(upload_to='property_images/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
   
    Address = models.OneToOneField('Address', on_delete=models.CASCADE, related_name='property', blank=True, null=True )

    def __str__(self):
        return self.property_name   

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.country}"
    
class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='Images', )
    images = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return f"Image for {self.property.property_name}"