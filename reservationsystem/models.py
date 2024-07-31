from django.db import models
from django.contrib.auth.models import User

TIME_SLOT = (

	('12:00', '12:00'),
    ('12:30', '12:30'),
    ('13:00', '13:00'),
    ('13:30', '13:30'),
    ('14:00', '14:00'),
    ('14:30', '14:30'),
    ('15:00', '15:00'),
    ('15:30', '15:30'),
    ('16:00', '16:00'),
    ('16:30', '16:30'),
    ('17:00', '17:00'),
    ('17:30', '17:30'),
    ('18:00', '18:00'),
    ('18:30', '18:30'),
    ('19:00', '19:00'),
    ('19:30', '19:30'),
    ('20:00', '20:00'),
    ('20:30', '20:30'),
    ('21:00', '21:00'),
    
)

TABLE_AMOUNT_NUMBER = (

    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),

)



class reservationsystem (models.Model):

    """
    A model to create and manage bookings at restaurant
    """

    user = models.ForeignKey(User, related_name='booking_owner', on_delete=models.CASCADE)

    booking_name = models.CharField(max_length=40, null=False, blank=False)
    telephone_number = models.CharField(max_length=15, null=False, blank=False, default='')
    number_of_people = models.CharField(
        blank=False, max_length=5,
        choices=TABLE_AMOUNT_NUMBER,
        help_text='For bookings greater than 8 people, please call us at 01 2340000.'
    )
    date = models.DateField()   
    time = models.CharField(max_length=5, choices=TIME_SLOT, null=False, blank=False)
    comments = models.CharField(max_length=1000, null=True, blank=True)
    reservation_date = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-reservation_date']

    
    

    #def __str__(self):
      #  return self.booking_name

