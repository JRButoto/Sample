# Generated by Django 5.0.3 on 2024-05-15 16:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Mother",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("healthcare_centre_name", models.CharField(max_length=255)),
                ("mother_name", models.CharField(max_length=255)),
                ("registration_number", models.IntegerField()),
                ("mosquito_net_voucher_number", models.IntegerField()),
                ("mother_age", models.IntegerField()),
                ("mother_education", models.CharField(max_length=255)),
                ("mother_employment", models.CharField(max_length=255)),
                ("Height", models.IntegerField()),
                ("partner_name", models.CharField(max_length=255)),
                ("partner_age", models.IntegerField()),
                ("partner_work", models.CharField(max_length=255)),
                ("partner_education", models.CharField(max_length=255)),
                ("address", models.CharField(max_length=255)),
                ("Chairperson_name", models.CharField(max_length=255)),
                ("pregnancies", models.IntegerField()),
                ("alive_children", models.IntegerField()),
                ("miscarriages", models.IntegerField()),
                ("births", models.IntegerField()),
                ("miscarriage_age", models.IntegerField()),
                ("miscarriage_year", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Mother_visit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("visit_number", models.IntegerField()),
                ("visit_date", models.DateField()),
                ("body_temperature", models.IntegerField()),
                ("blood_pressure", models.IntegerField()),
                ("hb_percentage", models.IntegerField()),
                ("pmtct_nutrition", models.CharField(max_length=255)),
                ("breastfeeding", models.CharField(max_length=255)),
                ("milk_coming_out", models.CharField(max_length=255)),
                ("breastfeeding_within_hour", models.CharField(max_length=255)),
                ("sore_nipples", models.CharField(max_length=255)),
                ("full_nipples", models.CharField(max_length=255)),
                ("abscesses", models.CharField(max_length=255)),
                ("breastfeeding_advice", models.CharField(max_length=255)),
                ("uterus_shrinking", models.CharField(max_length=255)),
                ("uterus_pain", models.CharField(max_length=255)),
                ("incision_did_not_tear", models.CharField(max_length=255)),
                ("incision_type", models.CharField(max_length=255)),
                ("wound_healed", models.CharField(max_length=255)),
                ("pus", models.CharField(max_length=255)),
                ("wound_open", models.CharField(max_length=255)),
                ("bad_smell", models.CharField(max_length=255)),
                ("lochia_amount", models.CharField(max_length=255)),
                ("lochia_color", models.CharField(max_length=255)),
                ("mental_state", models.CharField(max_length=255)),
                ("mental_issues", models.CharField(max_length=255)),
                ("advice_given", models.CharField(max_length=255)),
                ("ferrous_sulphate", models.BooleanField()),
                ("folic_acid", models.BooleanField()),
                ("tetanus_toxoid_doses", models.CharField(max_length=255)),
                ("pmtct_ctx", models.CharField(max_length=255)),
                ("postpartum_medications", models.CharField(max_length=255)),
                ("vitamin_a", models.CharField(max_length=255)),
                ("date_of_next_visit", models.CharField(max_length=255)),
                ("provider_name", models.CharField(max_length=255)),
                ("provider_title", models.CharField(max_length=255)),
                (
                    "mother",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="mother.mother"
                    ),
                ),
            ],
        ),
    ]
