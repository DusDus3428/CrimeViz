class Crime:
    def __init__(self, description, area, location, premise, victim_age, victim_sex, victim_descent, weapon_used,
                 status, report_date, occurrence_date, occurrence_time, latitude, longitude):
        self.description = description
        self.area = area
        self.location = location
        self.premise = premise
        self.victim_age = victim_age
        self.victim_sex = victim_sex
        self.victim_descent = victim_descent
        self.weapon_used = weapon_used
        self.status = status
        self.report_date = report_date
        self.occurrence_date = occurrence_date
        self.occurrence_time = occurrence_time
        self.latitude = latitude
        self.longitude = longitude
