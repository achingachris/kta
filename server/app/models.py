from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField("Category Name", max_length=150, unique=True)
    description = models.CharField("Category Description", max_length=250)
    slug = models.SlugField(max_length=150, unique=True, editable=False)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):
        # Auto-generate the slug based on the name if not provided
        if not self.slug:
            self.slug = slugify(self.name)

        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Award(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField("Award Name", max_length=150)
    description = models.CharField("Award Description", max_length=250)
    slug = models.SlugField(max_length=150, unique=True, editable=False)

    class Meta:
        verbose_name = "Award"
        verbose_name_plural = "Awards"

    def save(self, *args, **kwargs):
        # Auto-generate the slug based on the name if not provided
        if not self.slug:
            self.slug = slugify(self.name)

        super(Award, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Nominee(models.Model):
    award = models.ForeignKey(Award, on_delete=models.CASCADE)

    # Nominee Information
    full_name = models.CharField("Full Name", max_length=150)
    email = models.EmailField("Email")
    phone = models.CharField("Phone", max_length=20, blank=True, null=True)
    affiliation_company = models.CharField(
        "Affiliation or Company", max_length=150, blank=True, null=True
    )
    position_job_title = models.CharField(
        "Position/Job Title", max_length=150, blank=True, null=True
    )
    linkedin_profile = models.URLField(
        "LinkedIn Profile", max_length=200, blank=True, null=True
    )

    # Nomination Details
    brief_description = models.TextField(
        "Brief Description of the Nomination", blank=True, null=True
    )
    achievements_contributions = models.TextField(
        "Specific Achievements or Contributions", blank=True, null=True
    )

    # Qualifications and Experience
    educational_background = models.TextField(
        "Educational Background", blank=True, null=True
    )
    professional_certifications = models.TextField(
        "Professional Certifications", blank=True, null=True
    )
    work_experience = models.TextField(
        "Relevant Work Experience", blank=True, null=True
    )
    notable_projects_products = models.TextField(
        "Notable Projects or Products", blank=True, null=True
    )

    # Impact and Innovation
    impact_description = models.TextField(
        "Description of the impact of the nominee's work", blank=True, null=True
    )
    innovations_introduced = models.TextField(
        "Innovations introduced by the nominee", blank=True, null=True
    )
    patents_publications_contributions = models.TextField(
        "Any patents, publications, or open-source contributions", blank=True, null=True
    )

    # Recommendation or Endorsement
    recommendation_letters = models.TextField(
        "Letters of Recommendation or Endorsement (if applicable)",
        blank=True,
        null=True,
    )
    testimonials_quotes = models.TextField(
        "Testimonials or Quotes from colleagues, clients, or industry experts",
        blank=True,
        null=True,
    )

    # Portfolio or Work Samples
    project_links = models.TextField(
        "Links to relevant projects, products, or code repositories",
        blank=True,
        null=True,
    )
    screenshots_demos = models.TextField(
        "Screenshots, demos, or other visual representations of their work",
        blank=True,
        null=True,
    )

    # Professional Development
    participation_in_events = models.TextField(
        "Participation in conferences, workshops, or seminars", blank=True, null=True
    )
    ongoing_professional_development = models.TextField(
        "Any ongoing commitment to professional development", blank=True, null=True
    )

    # Community Involvement
    tech_community_involvement = models.TextField(
        "Involvement in tech communities or organizations", blank=True, null=True
    )
    open_source_contributions = models.TextField(
        "Contributions to open-source projects", blank=True, null=True
    )
    volunteering_mentorship = models.TextField(
        "Volunteering or mentorship activities", blank=True, null=True
    )

    # Additional Information
    additional_information = models.TextField(
        "Any other information that supports the nominee's candidacy",
        blank=True,
        null=True,
    )
    awards_recognitions_received = models.TextField(
        "Relevant awards or recognitions received", blank=True, null=True
    )

    slug = models.SlugField(max_length=150, unique=True, editable=False)

    class Meta:
        verbose_name = "Nominee"
        verbose_name_plural = "Nominees"

    def save(self, *args, **kwargs):
        # Auto-generate the slug based on the name if not provided
        if not self.slug:
            self.slug = slugify(self.full_name)

        super(Nominee, self).save(*args, **kwargs)

    def __str__(self):
        return self.full_name
