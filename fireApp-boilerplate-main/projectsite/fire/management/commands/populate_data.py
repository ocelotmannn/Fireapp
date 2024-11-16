from django.core.management.base import BaseCommand
import random
from datetime import datetime, timedelta
from decimal import Decimal
from fire.models import Locations, Incident, FireStation, Firefighters, FireTruck, WeatherConditions

class Command(BaseCommand):
    help = 'Populates the database with random data'

    def handle(self, *args, **kwargs):
        # Create Locations
        for i in range(5):
            location = Locations.objects.create(
                name=f"Location {i + 1}",
                latitude=Decimal(f"{random.uniform(-90.0, 90.0):.6f}"),
                longitude=Decimal(f"{random.uniform(-180.0, 180.0):.6f}"),
                address=f"{i + 1} Random Street",
                city=f"City {i + 1}",
                country=f"Country {i + 1}"
            )

        # Create Incidents
        for i in range(5):
            location = Locations.objects.order_by('?').first()  # Get a random location
            incident = Incident.objects.create(
                location=location,
                date_time=self.random_date(datetime(2023, 1, 1), datetime(2024, 12, 31)),
                severity_level=random.choice(['Minor Fire', 'Moderate Fire', 'Major Fire']),
                description=f"Description of incident {i + 1}"
            )

        # Create Fire Stations
        for i in range(5):
            fire_station = FireStation.objects.create(
                name=f"Fire Station {i + 1}",
                latitude=Decimal(f"{random.uniform(-90.0, 90.0):.6f}"),
                longitude=Decimal(f"{random.uniform(-180.0, 180.0):.6f}"),
                address=f"{i + 1} Fire Station Rd",
                city=f"City {i + 1}",
                country=f"Country {i + 1}"
            )

        # Create Firefighters
        xp_choices = ['Probationary Firefighter', 'Firefighter I', 'Firefighter II', 'Firefighter III', 'Driver', 'Captain', 'Battalion Chief']
        for i in range(5):
            firefighter = Firefighters.objects.create(
                name=f"Firefighter {i + 1}",
                rank=random.choice(xp_choices),
                experience_level=f"Experience Level {i + 1}",
                station=random.choice(xp_choices)
            )

        # Create Fire Trucks
        for i in range(5):
            fire_station = FireStation.objects.order_by('?').first()  # Get a random fire station
            fire_truck = FireTruck.objects.create(
                truck_number=f"FT-{i + 1}",
                model=f"Model {i + 1}",
                capacity=f"{random.randint(2000, 10000)} liters",
                station=fire_station
            )

        # Create Weather Conditions
        for i in range(5):
            incident = Incident.objects.order_by('?').first()  # Get a random incident
            weather_conditions = WeatherConditions.objects.create(
                incident=incident,
                temperature=Decimal(f"{random.uniform(-30.0, 50.0):.2f}"),
                humidity=Decimal(f"{random.uniform(0.0, 100.0):.2f}"),
                wind_speed=Decimal(f"{random.uniform(0.0, 100.0):.2f}"),
                weather_description=f"Weather condition {i + 1}"
            )

    def random_date(self, start, end):
        return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))
