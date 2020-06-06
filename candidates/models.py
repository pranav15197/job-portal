from django.db import models


GENDER_MALE = 'male'
GENDER_FEMALE = 'female'
GENDER_CHOICES = (
    (GENDER_MALE, 'Male'),
    (GENDER_FEMALE, 'Female'),
)

STATUS_PENDING = 'pending'
STATUS_ACCEPTED = 'accepted'
STATUS_REJECTED = 'rejected'
STATUS_CHOICES = (
    (STATUS_PENDING, 'Pending'),
    (STATUS_ACCEPTED, 'Accepted'),
    (STATUS_REJECTED, 'Rejected'),
)


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(
        max_length=20, choices=GENDER_CHOICES, default=GENDER_MALE)
    mobile = models.CharField(max_length=20)
    city = models.CharField(max_length=30)
    expected_salary = models.IntegerField()
    will_relocate = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {}".format(self.name, self.mobile)

    def is_engaged(self):
        status_engaged = [
            STATUS_PENDING,
            STATUS_ACCEPTED
        ]
        jobs = CandidateJobMap.objects.filter(
            candidate=self,
            status__in=status_engaged
        ).all()
        if len(jobs) == 0:
            return "No"
        else:
            return "Yes"



class CandidateJobMap(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    job = models.ForeignKey('jobs.Job', on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
    feedback = models.TextField(blank=True, null=True)

    def age(self):
        return self.candidate.age

    def gender(self):
        return self.candidate.gender

    def city(self):
        return self.candidate.city

    def __str__(self):
        return "{} - {}".format(self.candidate.name, self.job.position_name)

    class Meta:
        verbose_name_plural = "Review Candidates"
