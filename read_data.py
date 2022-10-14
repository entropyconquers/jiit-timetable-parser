# convert excel to json using pandas and print it
from pprint import pprint
import pandas as pd
import json
from goto import with_goto

course_code_dataX = '''
15B11MA111	Mathematics-1
15B11PH111	Physics-I
15B11HS112	English 
15B11CI111	Software Development Fundamentals-I
15B17CI171	Software development lab-I
15B17PH171	Physics Lab-I
15B11PH171	Physics Lab-I
18B15GE111	Engineering Drawing & Design
21B19GE111 	BRIDGE COURSE
'''


# append to course_dict.json (key = course_code, value = course_name)
def append_to_course_dict(course_code_data):
    # split course_code_data
    course_code_data = course_code_data.split("\n")
    # remove last empty string
    if course_code_data[-1] == "":
        course_code_data = course_code_data[:-1]
    # create a dictionary
    # get data from course_dict.json
    with open("course_dict.json", "r") as f:
        courses = json.load(f)

    for i in course_code_data:
        if len(i) < 10:
            continue
        i = i.split("\t")
        courses[i[0]] = i[1]
    # append to course_dict.json
    with open("course_dict.json", "w") as f:
        json.dump(courses, f)


append_to_course_dict(course_code_dataX)


# convert excel to json using pandas and print it
def excel_to_json():
    #get excel file from user
    excel_file = input("Enter excel file name: ")

    # read excel file using pandas
    df = pd.read_excel(excel_file)
    # convert excel to json
    json_records = df.reset_index().to_json()
    # load json data
    data = []
    data = json.loads(json_records)
    # print json data
    return data


raw_data = excel_to_json()
pprint(raw_data)
days = ["MON", "TUES", "WED", "THUR", "FRI", "SAT"]
day_slot_range = {

}
last_day = days[0]
for day in days:
    day_key_dict = raw_data['Unnamed: 0']
    # days are values of day_key_dict find the key for the day
    for key, value in day_key_dict.items():
        if value == day:
            if day not in day_slot_range:
                day_slot_range[day] = {
                    "start": "",
                    "end": ""
                }
            day_slot_range[day]['start'] = key
            day_slot_range[last_day]["end"] = str(int(key) - 1)
            break
    last_day = day
day_slot_range[days[-1]]["end"] = str(len(raw_data['Unnamed: 0']) - 1)
pprint(day_slot_range)
# remove keys that are not needed ('Unnamed: 0' and 'index') from the raw_data
for key in list(raw_data.keys()):
    if key == 'Unnamed: 0' or key == 'index':
        del raw_data[key]

tt_data = {}
for day in list(day_slot_range.keys()):
    tt_data[day] = {}
    for timeslot in list(raw_data.keys()):
        tt_data[day][timeslot] = []
        for i in range(int(day_slot_range[day]['start']), int(day_slot_range[day]['end']) + 1):
            if raw_data[timeslot][str(i)] is not None:
                tt_data[day][timeslot].append(raw_data[timeslot][str(i)])


# time parser
def time_parser(time_str):
    # time_str is a time range
    # time_str = "9 - 9:50 AM"
    # time_str = "4 PM -4:50  PM"
    # time_str = "12 NOON - 12:50 PM"

    # parse time_str
    time_str = time_str.replace(" ", "")
    time_str = time_str.replace("NOON", "")
    # remove AM and PM
    time_str = time_str.replace("AM", "")
    time_str = time_str.replace("PM", "")
    # split time_str
    time_str = time_str.split("-")
    if 9 <= int(str(time_str[0])) <= 12:
        time_str[0] = str(time_str[0])
    else:
        time_str[0] = str(int(time_str[0]) + 12)
    return time_str[0]


final_tt_data = {}
for day in list(tt_data.keys()):
    final_tt_data[day] = {}
    for timeslot in list(tt_data[day].keys()):
        final_tt_data[day][int(time_parser(timeslot))] = tt_data[day][timeslot]

print("Final Time Table Data")
pprint(final_tt_data)

with open('course_dict.json') as f:
    courses = json.load(f)
    f.close()


def data_parser(data):
    data = data.replace(" ", "")
    try:
        incorrect = False
        lt = data[0]
        if lt == "L":
            lt = "Lecture"
        elif lt == "P":
            lt = "Lab"
        elif lt == "T":
            lt = "Tutorial"
        else:
            print("Invalid lecture type")
            incorrect = True
        # split data
        data = data.replace("---", "-")
        data = data.replace("--", "-")
        data = data.replace("\\", "/")
        data = data.replace("))", ")")
        data = data.replace("((", "(")
        data = data.split("-")

        '''
        data[0] = LF5F6(15B11CI212)
        data[1] = 148/MKG
        '''
        # get all batches
        batch_data = data[0][1:].split("(")[0]
        if batch_data == "ALL":
            batches = ["ALL"]
        else:
            # get batches from batch_data
            batches = []
            for i in range(0, len(batch_data), 2):
                batches.append(batch_data[i:i + 2])
        # get course code
        course_code = data[0].split("(")[1][:-1]
        # get room number
        room = data[1].split("/")[0]
        # get faculty name
        faculty = data[1].split("/")[1]
        # check if course code is valid
        if course_code not in courses:
            print("Invalid course code")
            incorrect = True
        if incorrect:
            return None
        return {
            "course_code": course_code,
            "course_name": courses[course_code],
            "lecture_type": lt,
            "batches": batches,
            "room": room,
            "faculty": faculty
        }
    except:
        return None


timetable = {}

for dd in list(final_tt_data.keys()):
    for hour in list(final_tt_data[dd].keys()):
        for hour_data in final_tt_data[dd][hour]:
            dataX = hour_data
            fetched = False
            while not fetched:
                data = data_parser(dataX)
                if data is not None:
                    batches = data['batches']
                    course_code = data['course_code']
                    course = data['course_name']
                    room = data['room']
                    faculty = data['faculty']
                    lt = data['lecture_type']
                    for batch in batches:
                        if batch not in timetable:
                            timetable[batch] = {}
                        if dd not in timetable[batch]:
                            timetable[batch][dd] = {}
                        if hour not in timetable[batch][dd]:
                            timetable[batch][dd][hour] = {}
                        timetable[batch][dd][hour] = \
                            {"type": lt, "room": room, "faculty": faculty, "course": course}
                    fetched = True
                else:
                    print("Invalid data: ", dataX)
                    print("Press s to skip, e to edit, m to add manually")
                    choice = input()
                    if choice == "s":
                        fetched = True
                        continue
                    elif choice == "e":
                        dataX = input("Enter data: ")
                    elif choice == "m":
                        print("Enter data: ")
                        course_code = input("Course Code: ")
                        course = input("Course Name: ")
                        lt = input("Lecture Type: ")
                        batches = input("Batches: ")
                        room = input("Room: ")
                        faculty = input("Faculty: ")
                        for batch in batches:
                            if batch not in timetable:
                                timetable[batch] = {}
                            if dd not in timetable[batch]:
                                timetable[batch][dd] = {}
                            if hour not in timetable[batch][dd]:
                                timetable[batch][dd][hour] = {}
                            timetable[batch][dd][hour] = \
                                {"type": lt, "room": room, "faculty": faculty, "course": course}
                        if course_code not in courses:
                            courses[course_code] = course
                            with open('course_dict.json', 'w') as f:
                                json.dump(courses, f)
                                f.close()
                        fetched = True
                    else:
                        print("Invalid choice")
                        continue

print("Timetable")
pprint(timetable)
# save to json
# get year
year = input("Enter year: ")

with open('timetable_' + year + '.json', 'w') as f:
    json.dump(timetable, f)
    f.close()

'''if course_code not in courses:
    courses[course_code] = course
    with open('course_dict.json', 'w') as f:
        json.dump(courses, f)
        f.close()'''
