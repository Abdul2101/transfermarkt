from django.db import models
from datetime import date

class League(models.Model):
    title = models.CharField(max_length=250)
    earth_choices = [
        ('EU', 'Europe'),
        ('Eng', 'England'),
        ('ES', 'Spain'),
    ]
    earth = models.CharField(
        max_length=15,
        choices=earth_choices,
        default='none'
    )

    def __str__(self):
        return f"{self.title} - {self.earth}"


class Club(models.Model):
    title = models.CharField(max_length=250)
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='clubs')
    price = models.DecimalField(max_digits=14, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.title}"


class National(models.Model):
    title = models.CharField(max_length=250)

    continent_choices = [
        ('Asia', 'Asia'),
        ('Europe', 'Europe'),
        ('Africa', 'Africa'),
        ('North America', 'North America'),
        ('South America', 'South America'),
    ]

    continent = models.CharField(
        max_length=25,
        choices=continent_choices,
        default='none'
    )

    def __str__(self):
        return self.title


class Player(models.Model):
    name = models.CharField(max_length=250)
    birth = models.DateField()

    position_choices = [
        ('GK', 'GK'),
        ('CB', 'CB'),
        ('CM', 'CM'),
        ('ST', 'ST'),
    ]
    position = models.CharField(
        max_length=15,
        choices=position_choices,
        default='none'
    )

    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='players', null=True, blank=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='players', null=True, blank=True)

    games = models.IntegerField(default=0)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    yellow_c = models.IntegerField(default=0)
    red_c = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def get_age(self):
        today = date.today()
        age = today.year - self.birth.year

        if today.month < self.birth.month or (today.month == self.birth.month and today.day < self.birth.day):
            age -= 1
        return age

    def __str__(self):
        return f"{self.name}"


class Tournament(models.Model):
    name = models.CharField(max_length=150)
    season = models.CharField(max_length=9, default="2023/24")
    is_national = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} {self.season}"


class TournamentParticipant(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='participants')
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='tournaments')

    points = models.IntegerField(default=0)
    position = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        unique_together = ('tournament', 'club')

    def __str__(self):
        return f"{self.club.title} in {self.tournament.name} ({self.tournament.season})"
