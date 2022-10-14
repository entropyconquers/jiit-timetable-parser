# jiit-timetable-parser

A simple python script to parse the timetable of JIIT Noida from the excel file.

## Requirements
<!-- list the requirements -->

- Python 3.6 or above
- Pandas
- openpyxl


## Usage

<!-- run read_data.py and give the path to the excel file as the input -->

```bash
python read_data.py
```

## Output

File `timetable_<year_name>.json` will be created in the same directory.

## Sample Output
```JSON
{
    "F1": {
        "MON": {
            "9": {
                "type": "Lab",
                "room": "CL3",
                "faculty": "ARM",
                "course": "Open Source Software lab"
            },
            "11": {
                "type": "Lecture",
                "room": "254",
                "faculty": "ARM",
                "course": "Operating Systems and Systems Programming"
            },
            "12": {
                "type": "Lecture",
                "room": "254",
                "faculty": "BDJ",
                "course": "Computer Organisation and Architecture "
            },
            "14": {
                "type": "Lecture",
                "room": "254",
                "faculty": "AMS",
                "course": "Logical Reasoning and Inequalities"
            },
            "15": {
                "type": "Lab",
                "room": "238",
                "faculty": "RSK",
                "course": "Computer Organisation and Architecture Lab"
            }
        },
        "TUES": {
            "9": {
                "type": "Lecture",
                "room": "254",
                "faculty": "BDJ",
                "course": "Computer Organisation and Architecture "
            },
            "13": {
                "type": "Lecture",
                "room": "254",
                "faculty": "AMS",
                "course": "Logical Reasoning and Inequalities"
            },
            "14": {
                "type": "Tutorial",
                "room": "230",
                "faculty": "BDJ",
                "course": "Computer Organisation and Architecture "
            },
            "16": {
                "type": "Lecture",
                "room": "257",
                "faculty": "PRIYANKA",
                "course": "Indian Constitution & Traditional Knowledge"
            }
        },
        "WED": {
            "9": {
                "type": "Lecture",
                "room": "257",
                "faculty": "PRIYANKA",
                "course": "Indian Constitution & Traditional Knowledge"
            }
        },
        "THUR": {
            "11": {
                "type": "Lecture",
                "room": "259",
                "faculty": "ARM",
                "course": "Operating Systems and Systems Programming"
            },
            "12": {
                "type": "Lecture",
                "room": "254",
                "faculty": "AMS",
                "course": "Logical Reasoning and Inequalities"
            },
            "14": {
                "type": "Lecture",
                "room": "259",
                "faculty": "BDJ",
                "course": "Computer Organisation and Architecture "
            },
            "15": {
                "type": "Lab",
                "room": "CL2",
                "faculty": "MKG",
                "course": "Information Security Lab"
            }
        },
        "FRI": {
            "10": {
                "type": "Lecture",
                "room": "257",
                "faculty": "PRIYANKA",
                "course": "Indian Constitution & Traditional Knowledge"
            },
            "11": {
                "type": "Lecture",
                "room": "254",
                "faculty": "ARM",
                "course": "Operating Systems and Systems Programming"
            },
            "15": {
                "type": "Lab",
                "room": "CL2",
                "faculty": "GKN",
                "course": "Operating Systems and Systems Programming Lab"
            }
        },
        "SAT": {
            "11": {
                "type": "Tutorial",
                "room": "230",
                "faculty": "ARM",
                "course": "Operating Systems and Systems Programming"
            }
        }
    },
    "F2": {
        "MON": {
            "9": {
                "type": "Lab",
                "room": "CL3",
                "faculty": "ARM",
                "course": "Open Source Software lab"
            },
            "11": {
                "type": "Lecture",
                "room": "254",
                "faculty": "ARM",
                "course": "Operating Systems and Systems Programming"
            },
            "12": {
                "type": "Lecture",
                "room": "254",
                "faculty": "BDJ",
                "course": "Computer Organisation and Architecture "
            },
            "14": {
                "type": "Lecture",
                "room": "254",
                "faculty": "AMS",
                "course": "Logical Reasoning and Inequalities"
            },
            "15": {
                "type": "Lab",
                "room": "132",
                "faculty": "SLK",
                "course": "Computer Organisation and Architecture Lab"
            }
        },
        "TUES": {
            "9": {
                "type": "Lecture",
                "room": "254",
                "faculty": "BDJ",
                "course": "Computer Organisation and Architecture "
            },
            "13": {
                "type": "Lecture",
                "room": "254",
                "faculty": "AMS",
                "course": "Logical Reasoning and Inequalities"
            },
            "16": {
                "type": "Lecture",
                "room": "257",
                "faculty": "PRIYANKA",
                "course": "Indian Constitution & Traditional Knowledge"
            }
        },
        "WED": {
            "9": {
                "type": "Lecture",
                "room": "257",
                "faculty": "PRIYANKA",
                "course": "Indian Constitution & Traditional Knowledge"
            }
        },
        "THUR": {
            "11": {
                "type": "Lecture",
                "room": "259",
                "faculty": "ARM",
                "course": "Operating Systems and Systems Programming"
            },
            "12": {
                "type": "Lecture",
                "room": "254",
                "faculty": "AMS",
                "course": "Logical Reasoning and Inequalities"
            },
            "14": {
                "type": "Lecture",
                "room": "259",
                "faculty": "BDJ",
                "course": "Computer Organisation and Architecture "
            },
            "15": {
                "type": "Lab",
                "room": "CL2",
                "faculty": "MKG",
                "course": "Information Security Lab"
            }
        },
        "FRI": {
            "10": {
                "type": "Lecture",
                "room": "257",
                "faculty": "PRIYANKA",
                "course": "Indian Constitution & Traditional Knowledge"
            },
            "11": {
                "type": "Lecture",
                "room": "254",
                "faculty": "ARM",
                "course": "Operating Systems and Systems Programming"
            },
            "14": {
                "type": "Tutorial",
                "room": "121",
                "faculty": "BDJ",
                "course": "Computer Organisation and Architecture "
            },
            "15": {
                "type": "Lab",
                "room": "CL2",
                "faculty": "GKN",
                "course": "Operating Systems and Systems Programming Lab"
            }
        },
        "SAT": {
            "9": {
                "type": "Tutorial",
                "room": "256",
                "faculty": "ARM",
                "course": "Operating Systems and Systems Programming"
            }
        }
    },
    "E4": {
        "MON": {
            "9": {
                "type": "Lecture",
                "room": "254",
                "faculty": "RAGHVENDRA",
                "course": "Electromagnetic Field Theory"
            },
            "10": {
                "type": "Lecture",
                "room": "CR6",
                "faculty": "JV",
                "course": "Information Theory and Application"
            },
            "11": {
                "type": "Lab",
                "room": "237",
                "faculty": "134",
                "course": "Electromagnetic Field Theory Lab"
            }
        },
        "TUES": {
            "9": {
                "type": "Lecture",
                "room": "230",
                "faculty": "JV",
                "course": "Information Theory and Application"
            },
            "11": {
                "type": "Tutorial",
                "room": "113",
                "faculty": "RAGHVENDRA",
                "course": "Electromagnetic Field Theory"
            },
            "14": {
                "type": "Lecture",
                "room": "256",
                "faculty": "PRAVEEN",
                "course": "Indian Constitution & Traditional Knowledge"
            },
            "15": {
                "type": "Lab",
                "room": "142",
                "faculty": "VIMAL",
                "course": "Embedded Systems/IOT Lab"
            }
        },
        "WED": {
            "9": {
                "type": "Lecture",
                "room": "254",
                "faculty": "RJP",
                "course": "Data Structures and Algorithms"
            },
            "11": {
                "type": "Lecture",
                "room": "CR6",
                "faculty": "RAGHVENDRA",
                "course": "Electromagnetic Field Theory"
            },
            "15": {
                "type": "Lab",
                "room": "134",
                "faculty": "JV",
                "course": "Python for Signal Processing & Communication"
            }
        },
        "THUR": {
            "9": {
                "type": "Lecture",
                "room": "257",
                "faculty": "PRAVEEN",
                "course": "Indian Constitution & Traditional Knowledge"
            },
            "10": {
                "type": "Lecture",
                "room": "256",
                "faculty": "JV",
                "course": "Information Theory and Application"
            },
            "11": {
                "type": "Lecture",
                "room": "254",
                "faculty": "RJP",
                "course": "Data Structures and Algorithms"
            },
            "14": {
                "type": "Lecture",
                "room": "254",
                "faculty": "SQM",
                "course": "HSS"
            },
            "15": {
                "type": "Lab",
                "room": "CL3",
                "faculty": "RJP",
                "course": "Data Structures and Algorithms Lab"
            }
        },
        "FRI": {
            "9": {
                "type": "Lecture",
                "room": "259",
                "faculty": "RAGHVENDRA",
                "course": "Electromagnetic Field Theory"
            },
            "10": {
                "type": "Lecture",
                "room": "254",
                "faculty": "RJP",
                "course": "Data Structures and Algorithms"
            },
            "11": {
                "type": "Lecture",
                "room": "257",
                "faculty": "SQM",
                "course": "HSS"
            },
            "15": {
                "type": "Lecture",
                "room": "254",
                "faculty": "VIMAL",
                "course": "Microprocessors and Microcontrollers"
            }
        },
        "SAT": {
            "9": {
                "type": "Lecture",
                "room": "259",
                "faculty": "PRAVEEN",
                "course": "Indian Constitution & Traditional Knowledge"
            }
        }
    },
    "E1": {
        "MON": {
            "9": {
                "type": "Lecture",
                "room": "230",
                "faculty": "AKB",
                "course": "Data Structures and Algorithms"
            },
            "10": {
                "type": "Lecture",
                "room": "256",
                "faculty": "BAJRANG",
                "course": "Information Theory and Application"
            },
            "14": {
                "type": "Lecture",
                "room": "259",
                "faculty": "LKK",
                "course": "Logical Reasoning and Inequalities"
            },
            "15": {
                "type": "Lab",
                "room": "142",
                "faculty": "ABHAY",
                "course": "Embedded Systems/IOT Lab"
            }
        },
        "TUES": {
            "11": {
                "type": "Lecture",
                "room": "CR6",
                "faculty": "BHAGIRATH",
                "course": "Electromagnetic Field Theory"
            },
            "13": {
                "type": "Lecture",
                "room": "259",
                "faculty": "LKK",
                "course": "Logical Reasoning and Inequalities"
            },
            "14": {
                "type": "Lecture",
                "room": "259",
                "faculty": "EKTA",
                "course": "Indian Constitution & Traditional Knowledge"
            },
            "15": {
                "type": "Lecture",
                "room": "CR6",
                "faculty": "AKB",
                "course": "Data Structures and Algorithms"
            }
        },
        "WED": {
            "9": {
                "type": "Lecture",
                "room": "259",
                "faculty": "BHAGIRATH",
                "course": "Electromagnetic Field Theory"
            },
            "11": {
                "type": "Tutorial",
                "room": "113",
                "faculty": "BHAGIRATH",
                "course": "Electromagnetic Field Theory"
            },
            "15": {
                "type": "Lab",
                "room": "CL3",
                "faculty": "RJP",
                "course": "Data Structures and Algorithms Lab"
            }
        },
        "THUR": {
            "10": {
                "type": "Lecture",
                "room": "259",
                "faculty": "BAJRANG",
                "course": "Information Theory and Application"
            },
            "11": {
                "type": "Lecture",
                "room": "CR3",
                "faculty": "AKB",
                "course": "Data Structures and Algorithms"
            },
            "12": {
                "type": "Lecture",
                "room": "259",
                "faculty": "LKK",
                "course": "Logical Reasoning and Inequalities"
            },
            "14": {
                "type": "Lecture",
                "room": "254",
                "faculty": "SQM",
                "course": "HSS"
            },
            "15": {
                "type": "Lab",
                "room": "142",
                "faculty": "PARUL",
                "course": "Python for Signal Processing & Communication"
            }
        },
        "FRI": {
            "9": {
                "type": "Lab",
                "room": "237",
                "faculty": "134",
                "course": "Electromagnetic Field Theory Lab"
            },
            "11": {
                "type": "Lecture",
                "room": "257",
                "faculty": "SQM",
                "course": "HSS"
            },
            "14": {
                "type": "Lecture",
                "room": "254",
                "faculty": "BHAGIRATH",
                "course": "Electromagnetic Field Theory"
            },
            "15": {
                "type": "Lecture",
                "room": "259",
                "faculty": "BAJRANG",
                "course": "Information Theory and Application"
            }
        },
        "SAT": {
            "9": {
                "type": "Lecture",
                "room": "118",
                "faculty": "EKTA",
                "course": "Indian Constitution & Traditional Knowledge"
            }
        }
    },
    "E2": {
        "MON": {
            "9": {
                "type": "Lecture",
                "room": "230",
                "faculty": "AKB",
                "course": "Data Structures and Algorithms"
            },
            "10": {
                "type": "Lecture",
                "room": "CR6",
                "faculty": "JV",
                "course": "Information Theory and Application"
            },
            "11": {
                "type": "Lab",
                "room": "142",
                "faculty": "JV",
                "course": "Python for Signal Processing & Communication"
            },
            "14": {
                "type": "Lecture",
                "room": "259",
                "faculty": "LKK",
                "course": "Logical Reasoning and Inequalities"
            }
        },
        "TUES": {
            "9": {
                "type": "Lecture",
                "room": "230",
                "faculty": "JV",
                "course": "Information Theory and Application"
            },
            "11": {
                "type": "Lecture",
                "room": "CR3",
                "faculty": "ASHISHG",
                "course": "Electromagnetic Field Theory"
            },
            "13": {
                "type": "Lecture",
                "room": "259",
                "faculty": "LKK",
                "course": "Logical Reasoning and Inequalities"
            },
            "14": {
                "type": "Lecture",
                "room": "259",
                "faculty": "EKTA",
                "course": "Indian Constitution & Traditional Knowledge"
            },
            "15": {
                "type": "Lecture",
                "room": "CR6",
                "faculty": "AKB",
                "course": "Data Structures and Algorithms"
            },
            "16": {
                "type": "Tutorial",
                "room": "126",
                "faculty": "ASISHG",
                "course": "Electromagnetic Field Theory"
            }
        },
        "WED": {
            "9": {
                "type": "Lecture",
                "room": "256",
                "faculty": "ASHISHG",
                "course": "Electromagnetic Field Theory"
            },
            "15": {
                "type": "Lab",
                "room": "CL3",
                "faculty": "RJP",
                "course": "Data Structures and Algorithms Lab"
            }
        },
        "THUR": {
            "10": {
                "type": "Lecture",
                "room": "256",
                "faculty": "JV",
                "course": "Information Theory and Application"
            },
            "11": {
                "type": "Lecture",
                "room": "CR3",
                "faculty": "AKB",
                "course": "Data Structures and Algorithms"
            },
            "12": {
                "type": "Lecture",
                "room": "259",
                "faculty": "LKK",
                "course": "Logical Reasoning and Inequalities"
            },
            "14": {
                "type": "Lecture",
                "room": "254",
                "faculty": "SQM",
                "course": "HSS"
            },
            "15": {
                "type": "Lab",
                "room": "237134",
                "faculty": "",
                "course": "Electromagnetic Field Theory Lab"
            }
        },
        "FRI": {
            "9": {
                "type": "Lab",
                "room": "142",
                "faculty": "ABHAY",
                "course": "Embedded Systems/IOT Lab"
            },
            "11": {
                "type": "Lecture",
                "room": "257",
                "faculty": "SQM",
                "course": "HSS"
            },
            "14": {
                "type": "Lecture",
                "room": "259",
                "faculty": "ASISHG",
                "course": "Electromagnetic Field Theory"
            },
            "15": {
                "type": "Lecture",
                "room": "254",
                "faculty": "VIMAL",
                "course": "Microprocessors and Microcontrollers"
            }
        },
        "SAT": {
            "9": {
                "type": "Lecture",
                "room": "118",
                "faculty": "EKTA",
                "course": "Indian Constitution & Traditional Knowledge"
            }
        }
    },
    "F3": {
        "MON": {
            "9": {
                "type": "Lecture",
                "room": "256",
                "faculty": "RSK",
                "course": "Computer Organisation and Architecture "
            },
            "10": {
                "type": "Lecture",
                "room": "254",
                "faculty": "PRAVEEN",
                "course": "Indian Constitution & Traditional Knowledge"
            },
            "11": {
                "type": "Lecture",
                "room": "259",
                "faculty": "NRJ",
                "course": "Operating Systems and Systems Programming"
            },
            "12": {
                "type": "Tutorial",
                "room": "116",
                "faculty": "RSK",
                "course": "Computer Organisation and Architecture "
            },
            "14": {
                "type": "Lecture",
                "room": "254",
                "faculty": "AMS",
                "course": "Logical Reasoning and Inequalities"
            }
        },
        "TUES": {
            "9": {
                "type": "Lecture",
                "room": "259",
                "faculty": "RSK",
                "course": "Computer Organisation and Architecture "
            },
            "13": {
                "type": "Lecture",
                "room": "254",
                "faculty": "AMS",
                "course": "Logical Reasoning and Inequalities"
            },
            "15": {
                "type": "Lab",
                "room": "CL2",
                "faculty": "GKN",
                "course": "Operating Systems and Systems Programming Lab"
            }
        },
        "WED": {
            "14": {
                "type": "Tutorial",
                "room": "126",
                "faculty": "NRJ",
                "course": "Operating Systems and Systems Programming"
            },
            "15": {
                "type": "Lab",
                "room": "238",
                "faculty": "RSK",
                "course": "Computer Organisation and Architecture Lab"
            }
        },
        "THUR": {
            "11": {
                "type": "Lecture",
                "room": "257",
                "faculty": "RSK",
                "course": "Computer Organisation and Architecture "
            },
            "12": {
                "type": "Lecture",
                "room": "254",
                "faculty": "AMS",
                "course": "Logical Reasoning and Inequalities"
            },
            "14": {
                "type": "Lecture",
                "room": "254",
                "faculty": "NRJ",
                "course": "Operating Systems and Systems Programming"
            },
            "15": {
                "type": "Lecture",
                "room": "254",
                "faculty": "PRAVEEN",
                "course": "Indian Constitution & Traditional Knowledge"
            }
        },
        "FRI": {
            "9": {
                "type": "Lab",
                "room": "CL3",
                "faculty": "SLK",
                "course": "Open Source Software lab"
            },
            "11": {
                "type": "Lecture",
                "room": "259",
                "faculty": "NRJ",
                "course": "Operating Systems and Systems Programming"
            },
            "13": {
                "type": "Lecture",
                "room": "256",
                "faculty": "PRAVEEN",
                "course": "Indian Constitution & Traditional Knowledge"
            }
        },
        "SAT": {
            "9": {
                "type": "Lab",
                "room": "CL2",
                "faculty": "MKG",
                "course": "Information Security Lab"
            }
        }
    },
    "F4": {
        "MON": {
            "9": {
                "type": "Lecture",
                "room": "256",
                "faculty": "RSK",
                "course": "Computer Organisation and Architecture "
            },
            "10": {
                "type": "Lecture",
                "room": "254",
                "faculty": "PRAVEEN",
                "course": "Indian Constitution & Traditional Knowledge"
            },
            "11": {
                "type": "Lecture",
                "room": "259",
                "faculty": "NRJ",
                "course": "Operating Systems and Systems Programming"
            },
            "14": {
                "type": "Lecture",
                "room": "259",
                "faculty": "LKK",
                "course": "Logical Reasoning and Inequalities"
            }
        },
        "TUES": {
            "9": {
                "type": "Lecture",
                "room": "259",
                "faculty": "RSK",
                "course": "Computer Organisation and Architecture "
            },
            "13": {
                "type": "Lecture",
                "room": "259",
                "faculty": "LKK",
                "course": "Logical Reasoning and Inequalities"
            },
            "15": {
                "type": "Lab",
                "room": "CL2",
                "faculty": "GKN",
                "course": "Operating Systems and Systems Programming Lab"
            }
        },
        "WED": {
            "15": {
                "type": "Lab",
                "room": "132",
                "faculty": "SLK",
                "course": "Computer Organisation and Architecture Lab"
            }
        },
        "THUR": {
            "10": {
                "type": "Tutorial",
                "room": "230",
                "faculty": "RSK",
                "course": "Computer Organisation and Architecture "
            },
            "11": {
                "type": "Lecture",
                "room": "257",
                "faculty": "RSK",
                "course": "Computer Organisation and Architecture "
            },
            "12": {
                "type": "Lecture",
                "room": "259",
                "faculty": "LKK",
                "course": "Logical Reasoning and Inequalities"
            },
            "14": {
                "type": "Lecture",
                "room": "254",
                "faculty": "NRJ",
                "course": "Operating Systems and Systems Programming"
            },
            "15": {
                "type": "Lecture",
                "room": "254",
                "faculty": "PRAVEEN",
                "course": "Indian Constitution & Traditional Knowledge"
            }
        },
        "FRI": {
            "9": {
                "type": "Lab",
                "room": "CL3",
                "faculty": "SLK",
                "course": "Open Source Software lab"
            },
            "11": {
                "type": "Lecture",
                "room": "259",
                "faculty": "NRJ",
                "course": "Operating Systems and Systems Programming"
            },
            "13": {
                "type": "Lecture",
                "room": "256",
                "faculty": "PRAVEEN",
                "course": "Indian Constitution & Traditional Knowledge"
            },
            "14": {
                "type": "Tutorial",
                "room": "126",
                "faculty": "NRJ",
                "course": "Operating Systems and Systems Programming"
            }
        },
        "SAT": {
            "9": {
                "type": "Lab",
                "room": "CL2",
                "faculty": "MKG",
                "course": "Information Security Lab"
            }
        }
    },
    "E3": {
        "MON": {
            "10": {
                "type": "Lecture",
                "room": "256",
                "faculty": "BAJRANG",
                "course": "Information Theory and Application"
            },
            "12": {
                "type": "Lecture",
                "room": "CR6",
                "faculty": "ASHISHG",
                "course": "Electromagnetic Field Theory"
            },
            "14": {
                "type": "Lecture",
                "room": "259",
                "faculty": "LKK",
                "course": "Logical Reasoning and Inequalities"
            },
            "15": {
                "type": "Lab",
                "room": "237",
                "faculty": "134",
                "course": "Electromagnetic Field Theory Lab"
            }
        },
        "TUES": {
            "9": {
                "type": "Tutorial",
                "room": "113",
                "faculty": "ASISHG",
                "course": "Electromagnetic Field Theory"
            },
            "13": {
                "type": "Lecture",
                "room": "259",
                "faculty": "LKK",
                "course": "Logical Reasoning and Inequalities"
            },
            "14": {
                "type": "Lecture",
                "room": "256",
                "faculty": "PRAVEEN",
                "course": "Indian Constitution & Traditional Knowledge"
            },
            "15": {
                "type": "Lab",
                "room": "134",
                "faculty": "PARUL",
                "course": "Python for Signal Processing & Communication"
            }
        },
        "WED": {
            "9": {
                "type": "Lecture",
                "room": "254",
                "faculty": "RJP",
                "course": "Data Structures and Algorithms"
            },
            "15": {
                "type": "Lab",
                "room": "142",
                "faculty": "VIMAL",
                "course": "Embedded Systems/IOT Lab"
            }
        },
        "THUR": {
            "9": {
                "type": "Lecture",
                "room": "257",
                "faculty": "PRAVEEN",
                "course": "Indian Constitution & Traditional Knowledge"
            },
            "10": {
                "type": "Lecture",
                "room": "259",
                "faculty": "BAJRANG",
                "course": "Information Theory and Application"
            },
            "11": {
                "type": "Lecture",
                "room": "254",
                "faculty": "RJP",
                "course": "Data Structures and Algorithms"
            },
            "12": {
                "type": "Lecture",
                "room": "259",
                "faculty": "LKK",
                "course": "Logical Reasoning and Inequalities"
            },
            "14": {
                "type": "Lecture",
                "room": "254",
                "faculty": "SQM",
                "course": "HSS"
            },
            "15": {
                "type": "Lab",
                "room": "CL3",
                "faculty": "RJP",
                "course": "Data Structures and Algorithms Lab"
            }
        },
        "FRI": {
            "9": {
                "type": "Lecture",
                "room": "254",
                "faculty": "ASHISHG",
                "course": "Electromagnetic Field Theory"
            },
            "10": {
                "type": "Lecture",
                "room": "254",
                "faculty": "RJP",
                "course": "Data Structures and Algorithms"
            },
            "11": {
                "type": "Lecture",
                "room": "257",
                "faculty": "SQM",
                "course": "HSS"
            },
            "15": {
                "type": "Lecture",
                "room": "259",
                "faculty": "BAJRANG",
                "course": "Information Theory and Application"
            }
        },
        "SAT": {
            "9": {
                "type": "Lecture",
                "room": "259",
                "faculty": "PRAVEEN",
                "course": "Indian Constitution & Traditional Knowledge"
            }
        }
    },
    "F5": {
        "MON": {
            "10": {
                "type": "Lecture",
                "room": "257",
                "faculty": "PRIYANKA",
                "course": "Indian Constitution & Traditional Knowledge"
            },
            "11": {
                "type": "Lecture",
                "room": "256",
                "faculty": "GKN",
                "course": "Operating Systems and Systems Programming"
            },
            "12": {
                "type": "Lecture",
                "room": "256",
                "faculty": "SLK",
                "course": "Computer Organisation and Architecture "
            },
            "14": {
                "type": "Lecture",
                "room": "259",
                "faculty": "LKK",
                "course": "Logical Reasoning and Inequalities"
            },
            "15": {
                "type": "Lab",
                "room": "CL3",
                "faculty": "MKG",
                "course": "Information Security Lab"
            }
        },
        "TUES": {
            "9": {
                "type": "Lecture",
                "room": "256",
                "faculty": "SLK",
                "course": "Computer Organisation and Architecture "
            },
            "13": {
                "type": "Lecture",
                "room": "259",
                "faculty": "LKK",
                "course": "Logical Reasoning and Inequalities"
            },
            "14": {
                "type": "Lecture",
                "room": "257",
                "faculty": "PRIYANKA",
                "course": "Indian Constitution & Traditional Knowledge"
            }
        },
        "WED": {
            "15": {
                "type": "Lab",
                "room": "CL2",
                "faculty": "GKN",
                "course": "Operating Systems and Systems Programming Lab"
            }
        },
        "THUR": {
            "10": {
                "type": "Lecture",
                "room": "257",
                "faculty": "PRIYANKA",
                "course": "Indian Constitution & Traditional Knowledge"
            },
            "11": {
                "type": "Lecture",
                "room": "256",
                "faculty": "GKN",
                "course": "Operating Systems and Systems Programming"
            },
            "12": {
                "type": "Lecture",
                "room": "259",
                "faculty": "LKK",
                "course": "Logical Reasoning and Inequalities"
            },
            "14": {
                "type": "Lecture",
                "room": "256",
                "faculty": "SLK",
                "course": "Computer Organisation and Architecture "
            },
            "15": {
                "type": "Lab",
                "room": "238",
                "faculty": "RSK",
                "course": "Computer Organisation and Architecture Lab"
            }
        },
        "FRI": {
            "10": {
                "type": "Tutorial",
                "room": "217",
                "faculty": "NVK",
                "course": "Computer Organisation and Architecture "
            },
            "11": {
                "type": "Lecture",
                "room": "256",
                "faculty": "GKN",
                "course": "Operating Systems and Systems Programming"
            },
            "14": {
                "type": "Tutorial",
                "room": "118",
                "faculty": "GKN",
                "course": "Operating Systems and Systems Programming"
            },
            "15": {
                "type": "Lab",
                "room": "CL4",
                "faculty": "ARM",
                "course": "Open Source Software lab"
            }
        }
    },
    "F6": {
        "MON": {
            "10": {
                "type": "Lecture",
                "room": "257",
                "faculty": "PRIYANKA",
                "course": "Indian Constitution & Traditional Knowledge"
            },
            "11": {
                "type": "Lecture",
                "room": "256",
                "faculty": "GKN",
                "course": "Operating Systems and Systems Programming"
            },
            "12": {
                "type": "Lecture",
                "room": "256",
                "faculty": "SLK",
                "course": "Computer Organisation and Architecture "
            },
            "14": {
                "type": "Lecture",
                "room": "259",
                "faculty": "LKK",
                "course": "Logical Reasoning and Inequalities"
            }
        },
        "TUES": {
            "9": {
                "type": "Lecture",
                "room": "256",
                "faculty": "SLK",
                "course": "Computer Organisation and Architecture "
            },
            "13": {
                "type": "Lecture",
                "room": "259",
                "faculty": "LKK",
                "course": "Logical Reasoning and Inequalities"
            },
            "14": {
                "type": "Lecture",
                "room": "257",
                "faculty": "PRIYANKA",
                "course": "Indian Constitution & Traditional Knowledge"
            },
            "15": {
                "type": "Lab",
                "room": "CL3",
                "faculty": "KTR",
                "course": "Information Security Lab"
            }
        },
        "WED": {
            "9": {
                "type": "Tutorial",
                "room": "217",
                "faculty": "GKN",
                "course": "Operating Systems and Systems Programming"
            },
            "15": {
                "type": "Lab",
                "room": "CL2",
                "faculty": "GKN",
                "course": "Operating Systems and Systems Programming Lab"
            }
        },
        "THUR": {
            "10": {
                "type": "Lecture",
                "room": "257",
                "faculty": "PRIYANKA",
                "course": "Indian Constitution & Traditional Knowledge"
            },
            "11": {
                "type": "Lecture",
                "room": "256",
                "faculty": "GKN",
                "course": "Operating Systems and Systems Programming"
            },
            "12": {
                "type": "Lecture",
                "room": "259",
                "faculty": "LKK",
                "course": "Logical Reasoning and Inequalities"
            },
            "14": {
                "type": "Lecture",
                "room": "256",
                "faculty": "SLK",
                "course": "Computer Organisation and Architecture "
            },
            "15": {
                "type": "Lab",
                "room": "132",
                "faculty": "SLK",
                "course": "Computer Organisation and Architecture Lab"
            }
        },
        "FRI": {
            "11": {
                "type": "Lecture",
                "room": "256",
                "faculty": "GKN",
                "course": "Operating Systems and Systems Programming"
            },
            "14": {
                "type": "Tutorial",
                "room": "257",
                "faculty": "NVK",
                "course": "Computer Organisation and Architecture "
            },
            "15": {
                "type": "Lab",
                "room": "CL4",
                "faculty": "ARM",
                "course": "Open Source Software lab"
            }
        }
    },
    "F7": {
        "MON": {
            "11": {
                "type": "Lecture",
                "room": "CR60",
                "faculty": "PRAVEEN",
                "course": "Indian Constitution & Traditional Knowledge"
            },
            "12": {
                "type": "Lecture",
                "room": "257",
                "faculty": "NVK",
                "course": "Computer Organisation and Architecture "
            },
            "14": {
                "type": "Lecture",
                "room": "259",
                "faculty": "LKK",
                "course": "Logical Reasoning and Inequalities"
            },
            "15": {
                "type": "Lab",
                "room": "CL2",
                "faculty": "ARM",
                "course": "Open Source Software lab"
            }
        },
        "TUES": {
            "9": {
                "type": "Lecture",
                "room": "257",
                "faculty": "NVK",
                "course": "Computer Organisation and Architecture "
            },
            "13": {
                "type": "Lecture",
                "room": "259",
                "faculty": "LKK",
                "course": "Logical Reasoning and Inequalities"
            },
            "15": {
                "type": "Lecture",
                "room": "254",
                "faculty": "PRAVEEN",
                "course": "Indian Constitution & Traditional Knowledge"
            }
        },
        "WED": {
            "9": {
                "type": "Lecture",
                "room": "230",
                "faculty": "CGA",
                "course": "Operating Systems and Systems Programming"
            },
            "14": {
                "type": "Tutorial",
                "room": "225",
                "faculty": "BDJ",
                "course": "Computer Organisation and Architecture "
            },
            "15": {
                "type": "Lecture",
                "room": "254",
                "faculty": "PRAVEEN",
                "course": "Indian Constitution & Traditional Knowledge"
            }
        },
        "THUR": {
            "11": {
                "type": "Lecture",
                "room": "230",
                "faculty": "CGA",
                "course": "Operating Systems and Systems Programming"
            },
            "12": {
                "type": "Lecture",
                "room": "259",
                "faculty": "LKK",
                "course": "Logical Reasoning and Inequalities"
            },
            "14": {
                "type": "Lecture",
                "room": "257",
                "faculty": "NVK",
                "course": "Computer Organisation and Architecture "
            },
            "15": {
                "type": "Lab",
                "room": "CL2",
                "faculty": "ARM",
                "course": "Operating Systems and Systems Programming Lab"
            }
        },
        "FRI": {
            "9": {
                "type": "Lab",
                "room": "132",
                "faculty": "MKG",
                "course": "Information Security Lab"
            },
            "11": {
                "type": "Lecture",
                "room": "230",
                "faculty": "CGA",
                "course": "Operating Systems and Systems Programming"
            },
            "14": {
                "type": "Tutorial",
                "room": "230",
                "faculty": "CGA",
                "course": "Operating Systems and Systems Programming"
            },
            "15": {
                "type": "Lab",
                "room": "238",
                "faculty": "RSK",
                "course": "Computer Organisation and Architecture Lab"
            }
        }
    },
    "ALL": {
        "TUES": {
            "10": {
                "type": "Lecture",
                "room": "256",
                "faculty": "AA",
                "course": "Planning And Economic Development"
            },
            "11": {
                "type": "Lecture",
                "room": "254",
                "faculty": "ABS",
                "course": "Fundamentals of Machine learning"
            },
            "12": {
                "type": "Lecture",
                "room": "254",
                "faculty": "PKS",
                "course": "Basic Numerical Methods"
            }
        },
        "WED": {
            "10": {
                "type": "Lecture",
                "room": "228",
                "faculty": "ADV",
                "course": "Laser Technology and Applications"
            },
            "11": {
                "type": "Lecture",
                "room": "254",
                "faculty": "ABS",
                "course": "Fundamentals of Machine learning"
            },
            "12": {
                "type": "Lecture",
                "room": "256",
                "faculty": "AA",
                "course": "Planning And Economic Development"
            }
        },
        "THUR": {
            "9": {
                "type": "Lecture",
                "room": "254",
                "faculty": "ABS",
                "course": "Fundamentals of Machine learning"
            },
            "12": {
                "type": "Lecture",
                "room": "256",
                "faculty": "ADV",
                "course": "Laser Technology and Applications"
            },
            "13": {
                "type": "Lecture",
                "room": "257",
                "faculty": "PRIYANKA",
                "course": "Sociology of Media"
            }
        },
        "FRI": {
            "12": {
                "type": "Lecture",
                "room": "254",
                "faculty": "PKS",
                "course": "Basic Numerical Methods"
            }
        }
    },
    "E": {
        "WED": {
            "14": {
                "type": "L",
                "room": "254",
                "faculty": "SQM",
                "course": "HSS"
            }
        },
        "SAT": {
            "11": {
                "type": "P",
                "room": "CL4",
                "faculty": "SQM",
                "course": "HSS Lab"
            }
        }
    },
    "1": {
        "WED": {
            "14": {
                "type": "L",
                "room": "254",
                "faculty": "SQM",
                "course": "HSS"
            }
        },
        "SAT": {
            "11": {
                "type": "P",
                "room": "CL4",
                "faculty": "SQM",
                "course": "HSS Lab"
            }
        }
    },
    "2": {
        "WED": {
            "14": {
                "type": "L",
                "room": "254",
                "faculty": "SQM",
                "course": "HSS"
            }
        },
        "SAT": {
            "11": {
                "type": "P",
                "room": "CL4",
                "faculty": "SQM",
                "course": "HSS Lab"
            }
        }
    },
    "3": {
        "WED": {
            "14": {
                "type": "L",
                "room": "254",
                "faculty": "SQM",
                "course": "HSS"
            }
        },
        "SAT": {
            "11": {
                "type": "P",
                "room": "CL4",
                "faculty": "SQM",
                "course": "HSS Lab"
            }
        }
    },
    "4": {
        "WED": {
            "14": {
                "type": "L",
                "room": "254",
                "faculty": "SQM",
                "course": "HSS"
            }
        },
        "SAT": {
            "11": {
                "type": "P",
                "room": "CL4",
                "faculty": "SQM",
                "course": "HSS Lab"
            }
        }
    }
}
```


