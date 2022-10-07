from django.db import models
from admin_section.models import basemodel
from django.utils.text import slugify
# Create your models here.

TEAM_NAME_CHOICES = [
    ('mentorspanel', 'Mentors Panel'),
    ('eminentfaculties', 'Eminent Faculties'),
    ('executivecommittee', 'Executive Committee'),
    ('foundingmembers', 'Founding Members'),
    ('ourassociates', 'Our Associates'),
    ('ourpartners', 'Our Partners'),
    ('ourstudents', 'Our Students'),
    ('ouralumni', 'Our Alumni'),
    ('ourvolunteers', 'Our Volunteers'),
    ('oursponsors', 'Our Sponsors'),
    ('ourfellowshippers', 'Our Fellowshippers'),
    ('ourcontributors', 'Our Contributors'),
    ('ourcommunity', 'Our Community')
]

class team_members(basemodel):
    team_name = models.CharField(max_length=100, choices=TEAM_NAME_CHOICES)
    team_member_name = models.CharField(max_length=100)
    team_member_designation = models.CharField(max_length=100)
    team_member_image = models.ImageField(upload_to='team_images')
    team_member_description = models.TextField()
    team_member_status = models.BooleanField(default=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.team_member_name)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.team_member_name
    class Meta:
        db_table = 'team_members'
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'