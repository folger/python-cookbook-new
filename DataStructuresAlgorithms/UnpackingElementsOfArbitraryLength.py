import math


def drop_first_last_avg(grades):
    def avg(nn):
        return math.fsum(nn) / len(nn)

    _, *middle, _ = grades
    return avg(middle)


def extract_name_email_phonenumbers(record):
    name, email, *phonenumbers = record
    return name, email, phonenumbers


if __name__ == '__main__':
    print(drop_first_last_avg((89, 95, 100, 70, 65, 99)))
    print(extract_name_email_phonenumbers(('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')))
