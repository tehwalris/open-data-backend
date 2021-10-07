from . import air_quality
from . import random_facts
from . import energy
from . import dogs

questions = [
    {
        "id": 1,
        "text": "How much carbon monoxide is there in Zurich?",
        "function": air_quality.make_answer_pollutant_over_time("CO"),
        "frontend_settings": {
            "id": 1,
            "chart_type": "line",
            "x_axis_time": True,
            "graph_label": "CO in [mg/m3] over time",
            "src_label": "https://data.stadt-zuerich.ch/dataset/ugz_luftschadstoffmessung_stundenwerte",
        },
    },
    {
        "id": 6,
        "text": "How much nitrogen monoxide is there in Zurich?",
        "function": air_quality.make_answer_pollutant_over_time("NO"),
        "frontend_settings": {
            "id": 6,
            "chart_type": "line",
            "x_axis_time": True,
            "graph_label": "Nitrogen Monoxide in [µg/m3] over time",
            "src_label": "https://data.stadt-zuerich.ch/dataset/ugz_luftschadstoffmessung_stundenwerte",
        },
    },
    {
        "id": 7,
        "text": "How much nitrogen dioxide is there in Zurich?",
        "function": air_quality.make_answer_pollutant_over_time("NO2"),
        "frontend_settings": {
            "id": 7,
            "chart_type": "line",
            "x_axis_time": True,
            "graph_label": "Nitrogen Dioxide in [µg/m3] over time",
            "src_label": "https://data.stadt-zuerich.ch/dataset/ugz_luftschadstoffmessung_stundenwerte",
        },
    },
    {
        "id": [8, 9],
        "text": [
            "How much particulate matter is there in Zurich?",
            "How much PM10 is there in Zurich?",
        ],
        "function": air_quality.make_answer_pollutant_over_time("PM10"),
        "frontend_settings": {
            "id": 8,
            "chart_type": "line",
            "x_axis_time": True,
            "graph_label": "Particulate Matter in [Unit] over time",
            "src_label": "https://data.stadt-zuerich.ch/dataset/ugz_luftschadstoffmessung_stundenwerte",
        },
    },
    {
        "id": 10,
        "text": "How much PM2.5 is there in Zurich?",
        "function": air_quality.make_answer_pollutant_over_time("PM2.5"),
        "frontend_settings": {
            "id": 10,
            "chart_type": "line",
            "x_axis_time": True,
            "graph_label": "PM2.5 in [µg/m3] over time",
            "src_label": "https://data.stadt-zuerich.ch/dataset/ugz_luftschadstoffmessung_stundenwerte",
        },
    },
    {
        "id": 11,
        "text": "How much sulfur dioxide is there in Zurich?",
        "function": air_quality.make_answer_pollutant_over_time("SO2"),
        "frontend_settings": {
            "id": 11,
            "chart_type": "line",
            "x_axis_time": True,
            "graph_label": "Sulphur Dioxide in [µg/m3] over time",
            "src_label": "https://data.stadt-zuerich.ch/dataset/ugz_luftschadstoffmessung_stundenwerte",
        },
    },
    {
        "id": 2,
        "text": "How much ozone is there in Zurich?",
        "function": air_quality.make_answer_pollutant_over_time("O3"),
        "frontend_settings": {
            "id": 2,
            "chart_type": "line",
            "x_axis_time": True,
            "graph_label": "Ozone in [µg/m3] over time",
            "src_label": "https://data.stadt-zuerich.ch/dataset/ugz_luftschadstoffmessung_stundenwerte",
        },
    },
    {
        "id": [3, 12],
        "text": [
            "Is air pollution in Zurich getting worse?",
            "How did air pollution in Zurich change over time?",
        ],
        "function": air_quality.answer_combined_over_time,
        "frontend_settings": {
            "id": 3,
            "chart_type": "line",
            "x_axis_time": True,
            "graph_label": "Air pollution [normalized] over time",
            "src_label": "https://data.stadt-zuerich.ch/dataset/ugz_luftschadstoffmessung_stundenwerte",
        },
    },
    {
        "id": [4, 5],
        "text": [
            "How much pollution is there in Zurich?",
            "What contributes to air pollution?",
        ],
        "function": air_quality.answer_pollutant_table,
        "frontend_settings": {
            "id": 4,
            "chart_type": "table",
            "x_axis_time": True,
            "graph_label": "Current air pollution in Zurich",
            "src_label": "https://data.stadt-zuerich.ch/dataset/ugz_luftschadstoffmessung_stundenwerte",
        },
    },
    {
        "id": 13,
        "text": "How does air pollution in Zurich change throughout the year?",
        "function": air_quality.answer_over_year,
        "frontend_settings": {
            "id": 13,
            "chart_type": "multi-line",
            "x_axis_time": True,
            "graph_label": "Air pollution [normalized] over the course of a year",
            "src_label": "https://data.stadt-zuerich.ch/dataset/ugz_luftschadstoffmessung_stundenwerte",
        },
    },
    {
        "id": 14,
        "text": "How does air pollution in Zurich change throughout the day?",
        "function": air_quality.answer_over_day,
        "frontend_settings": {
            "id": 14,
            "chart_type": "multi-line",
            "x_axis_hours": True,
            "graph_label": "Air pollution [normalized] over the course of a day",
            "src_label": "https://data.stadt-zuerich.ch/dataset/ugz_luftschadstoffmessung_stundenwerte",
        },
    },
    {
        "id": [18, 19],
        "text": ["How big are the districts of Zurich?", "What's the area of Zurich?",],
        "function": random_facts.make_answer_fact("Fläche in Quadratkilometer", "km²"),
        "frontend_settings": {
            "id": 18,
            "chart_type": "map",
            "src_label": "https://data.stadt-zuerich.ch/dataset/prd_ssz_gang-dur-zueri_od1005",
        },
    },
    {
        "id": [20, 21],
        "text": [
            "How much forest is there in Zurich?",
            "What area of Zurich is covered by forest?",
        ],
        "function": random_facts.make_answer_fact("Anteil der Waldfläche in %", "%"),
        "frontend_settings": {
            "id": 20,
            "chart_type": "map",
            "src_label": "https://data.stadt-zuerich.ch/dataset/prd_ssz_gang-dur-zueri_od1005",
        },
    },
    {
        "id": 22,
        "text": "What area of Zurich is covered by water?",
        "function": random_facts.make_answer_fact(
            "Anteil der Gewässerfläche in %", "%"
        ),
        "frontend_settings": {
            "id": 22,
            "chart_type": "map",
            "src_label": "https://data.stadt-zuerich.ch/dataset/prd_ssz_gang-dur-zueri_od1005",
        },
    },
    {
        "id": 23,
        "text": "How many drinking fountains are there in Zurich?",
        "function": random_facts.make_answer_fact("Brunnen", "fountains"),
        "frontend_settings": {
            "id": 23,
            "chart_type": "map",
            "src_label": "https://data.stadt-zuerich.ch/dataset/prd_ssz_gang-dur-zueri_od1005",
        },
    },
    {
        "id": 24,
        "text": "How many trees are there on the streets of Zurich?",
        "function": random_facts.make_answer_fact("Bäume", "trees"),
        "frontend_settings": {
            "id": 24,
            "chart_type": "map",
            "src_label": "https://data.stadt-zuerich.ch/dataset/prd_ssz_gang-dur-zueri_od1005",
        },
    },
    {
        "id": 25,
        "text": "How many primary schools are there in Zurich?",
        "function": random_facts.make_answer_fact("Schulen (Volksschule)", "schools"),
        "frontend_settings": {
            "id": 25,
            "chart_type": "map",
            "src_label": "https://data.stadt-zuerich.ch/dataset/prd_ssz_gang-dur-zueri_od1005",
        },
    },
    {
        "id": 26,
        "text": "How many primary schools are there in Zurich?",
        "function": random_facts.make_answer_fact("Schulen (Volksschule)", "schools"),
        "frontend_settings": {
            "id": 26,
            "chart_type": "map",
            "src_label": "https://data.stadt-zuerich.ch/dataset/prd_ssz_gang-dur-zueri_od1005",
        },
    },
    {
        "id": [27, 28],
        "text": [
            "What is the population of Zurich?",
            "How many people live in Zurich?",
        ],
        "function": random_facts.make_answer_fact(
            "Wohnbevölkerung (Anzahl Personen)", "people"
        ),
        "frontend_settings": {
            "id": 27,
            "chart_type": "map",
            "src_label": "https://data.stadt-zuerich.ch/dataset/prd_ssz_gang-dur-zueri_od1005",
        },
    },
    {
        "id": 29,
        "text": "How many babies are born in Zurich every year?",
        "function": random_facts.make_answer_fact("Neugeborene pro Jahr", "babies"),
        "frontend_settings": {
            "id": 29,
            "chart_type": "map",
            "src_label": "https://data.stadt-zuerich.ch/dataset/prd_ssz_gang-dur-zueri_od1005",
        },
    },
    {
        "id": 30,
        "text": "How many people die in Zurich every year?",
        "function": random_facts.make_answer_fact("Todesfälle pro Jahr", "deaths"),
        "frontend_settings": {
            "id": 30,
            "chart_type": "map",
            "src_label": "https://data.stadt-zuerich.ch/dataset/prd_ssz_gang-dur-zueri_od1005",
        },
    },
    {
        "id": 31,
        "text": "How many people move to Zurich every year?",
        "function": random_facts.make_answer_fact(
            "Zuziehende (Anzahl Personen pro Jahr)", "people"
        ),
        "frontend_settings": {
            "id": 31,
            "chart_type": "map",
            "src_label": "https://data.stadt-zuerich.ch/dataset/prd_ssz_gang-dur-zueri_od1005",
        },
    },
    {
        "id": 32,
        "text": "How many people move away from Zurich every year?",
        "function": random_facts.make_answer_fact(
            "Wegziehende (Anzahl Personen pro Jahr)", "people"
        ),
        "frontend_settings": {
            "id": 32,
            "chart_type": "map",
            "src_label": "https://data.stadt-zuerich.ch/dataset/prd_ssz_gang-dur-zueri_od1005",
        },
    },
    {
        "id": 33,
        "text": "How many foreigners live in Zurich?",
        "function": random_facts.make_answer_fact("Ausländeranteil in %", "%"),
        "frontend_settings": {
            "id": 33,
            "chart_type": "map",
            "src_label": "https://data.stadt-zuerich.ch/dataset/prd_ssz_gang-dur-zueri_od1005",
        },
    },
    # TODO: "Häufigste ausländische Nationalität (Anzahl Personen)"
    {
        "id": 34,
        "text": "How old is the oldest woman in Zurich?",
        "function": random_facts.make_answer_fact("Älteste Frau (Alter)", "years old"),
        "frontend_settings": {
            "id": 34,
            "chart_type": "map",
            "src_label": "https://data.stadt-zuerich.ch/dataset/prd_ssz_gang-dur-zueri_od1005",
        },
    },
    {
        "id": 35,
        "text": "How old is the oldest man in Zurich?",
        "function": random_facts.make_answer_fact("Ältester Mann (Alter)", "years old"),
        "frontend_settings": {
            "id": 35,
            "chart_type": "map",
            "src_label": "https://data.stadt-zuerich.ch/dataset/prd_ssz_gang-dur-zueri_od1005",
        },
    },
    # TODO: Oldest person ignoring gender
    {
        "id": [36, 37],
        "text": [
            "How many single-member households are there in Zurich?",
            "How many people in Zurich live alone?",  # HACK not the same question
        ],
        "function": random_facts.make_answer_fact(
            "Einpersonen-Haushalte (Anteil an allen Haushalten in %)", "%"
        ),
        "frontend_settings": {
            "id": 36,
            "chart_type": "map",
            "src_label": "https://data.stadt-zuerich.ch/dataset/prd_ssz_gang-dur-zueri_od1005",
        },
    },
    {
        "id": [76, 38],
        "text": [
            "How many households in Zurich have children?",
            "How many people in Zurich live with kids?",  # HACK not the same question
        ],
        "function": random_facts.make_answer_fact(
            "Haushalte mit Kindern (Anteil an allen Haushalten in %)", "%"
        ),
        "frontend_settings": {
            "id": 38,
            "chart_type": "map",
            "src_label": "https://data.stadt-zuerich.ch/dataset/prd_ssz_gang-dur-zueri_od1005",
        },
    },
    {
        "id": 39,
        "text": "How many apartments are there in Zurich?",
        "function": random_facts.make_answer_fact("Wohnungen", "apartments"),
        "frontend_settings": {
            "id": 39,
            "chart_type": "map",
            "src_label": "https://data.stadt-zuerich.ch/dataset/prd_ssz_gang-dur-zueri_od1005",
        },
    },
    {
        "id": 40,
        "text": "How many apartments were built in Zurich the last 5 years?",
        "function": random_facts.make_answer_fact(
            "Neubauwohnungen der letzten fünf Jahre", "apartments"
        ),
        "frontend_settings": {
            "id": 40,
            "chart_type": "map",
            "src_label": "https://data.stadt-zuerich.ch/dataset/prd_ssz_gang-dur-zueri_od1005",
        },
    },
    {
        "id": 41,
        "text": "How many apartments were destroyed in Zurich the last 5 years?",
        "function": random_facts.make_answer_fact(
            "Abgebrochene Wohnungen der letzten fünf Jahre", "apartments"
        ),
        "frontend_settings": {
            "id": 41,
            "chart_type": "map",
            "src_label": "https://data.stadt-zuerich.ch/dataset/prd_ssz_gang-dur-zueri_od1005",
        },
    },
    {
        "id": [42, 43],
        "text": [
            "What is the average living space in Zurich?",
            "How many square meters do people in Zurich live in?",
        ],
        "function": random_facts.make_answer_fact(
            "Durchschnittliche Wohnfläche (Quadratmeter pro Person)", "m²"
        ),
        "frontend_settings": {
            "id": 42,
            "chart_type": "map",
            "src_label": "https://data.stadt-zuerich.ch/dataset/prd_ssz_gang-dur-zueri_od1005",
        },
    },
    {
        "id": 44,
        "text": "How many buildings in Zurich are older than 100?",
        "function": random_facts.make_answer_fact(
            "Anzahl über 100-jährige Gebäude", "buildings"
        ),
        "frontend_settings": {
            "id": 44,
            "chart_type": "map",
            "src_label": "https://data.stadt-zuerich.ch/dataset/prd_ssz_gang-dur-zueri_od1005",
        },
    },
    {
        "id": [45, 46],
        "text": [
            "When was the oldest building in Zurich built?",
            "How old is the oldest building in Zurich?",
        ],
        "function": random_facts.make_answer_fact(
            "Baujahr des ältesten Gebäudes (Adresse", ""
        ),
        "frontend_settings": {
            "id": 45,
            "chart_type": "map",
            "src_label": "https://data.stadt-zuerich.ch/dataset/prd_ssz_gang-dur-zueri_od1005",
        },
    },
    {
        "id": [15, 16, 17],
        "text": [
            "How tall is the tallest building in Zurich?",
            "How many floors does the biggest building in Zurich have?",
            "Where is the tallest building in Zurich?",
        ],
        "function": random_facts.make_answer_fact(
            "Anzahl Stockwerke des höchsten Gebäudes (Adresse", "floors"
        ),
        "frontend_settings": {
            "id": 15,
            "chart_type": "map",
            "src_label": "https://data.stadt-zuerich.ch/dataset/prd_ssz_gang-dur-zueri_od1005",
        },
    },
    {
        "id": [47, 48],
        "text": [
            "How many single-family houses are there in Zurich?",
            "How many detached houses are there in Zurich?",
        ],
        "function": random_facts.make_answer_fact("Einfamilienhäuser", "houses"),
        "frontend_settings": {
            "id": 47,
            "chart_type": "map",
            "src_label": "https://data.stadt-zuerich.ch/dataset/prd_ssz_gang-dur-zueri_od1005",
        },
    },
    {
        "id": 49,
        "text": "How many tram and bus stops are there in Zurich?",
        "function": random_facts.make_answer_fact(
            "Tram- und Buswartehäuschen", "stops"
        ),
        "frontend_settings": {
            "id": 49,
            "chart_type": "map",
            "src_label": "https://data.stadt-zuerich.ch/dataset/prd_ssz_gang-dur-zueri_od1005",
        },
    },
    {
        "id": 50,
        "text": "How many people work in zurich?",
        "function": random_facts.make_answer_fact("Beschäftigte", "people"),
        "frontend_settings": {
            "id": 50,
            "chart_type": "map",
            "src_label": "https://data.stadt-zuerich.ch/dataset/prd_ssz_gang-dur-zueri_od1005",
        },
    },
    # TODO Beschäftigte im 1. Sektor, ...
    {
        "id": 51,
        "text": "How many people in zurich are unemployed?",
        "function": random_facts.make_answer_fact("Arbeitslose", "people"),
        "frontend_settings": {
            "id": 51,
            "chart_type": "map",
            "src_label": "https://data.stadt-zuerich.ch/dataset/prd_ssz_gang-dur-zueri_od1005",
        },
    },
    {
        "id": 52,
        "text": "Whats the unemployment rate in Zurich?",
        "function": random_facts.make_answer_fact("Arbeitslosenquote in %", "%"),
        "frontend_settings": {
            "id": 52,
            "chart_type": "map",
            "src_label": "https://data.stadt-zuerich.ch/dataset/prd_ssz_gang-dur-zueri_od1005",
        },
    },
    {
        "id": 53,
        "text": "How many doctors offices are there in Zurich?",
        "function": random_facts.make_answer_fact(
            "Arztpraxen (Allgemeinmedizin und Fachärzte)", "offices"
        ),
        "frontend_settings": {
            "id": 53,
            "chart_type": "map",
            "src_label": "https://data.stadt-zuerich.ch/dataset/prd_ssz_gang-dur-zueri_od1005",
        },
    },
    {
        "id": 54,
        "text": "How many dentists are there in Zurich?",
        "function": random_facts.make_answer_fact("Zahnarztpraxen", "dentists"),
        "frontend_settings": {
            "id": 54,
            "chart_type": "map",
            "src_label": "https://data.stadt-zuerich.ch/dataset/prd_ssz_gang-dur-zueri_od1005",
        },
    },
    {
        "id": 55,
        "text": "How many motorbikes are there in Zurich?",
        "function": random_facts.make_answer_fact("Motorräder", "motorbikes"),
        "frontend_settings": {
            "id": 55,
            "chart_type": "map",
            "src_label": "https://data.stadt-zuerich.ch/dataset/prd_ssz_gang-dur-zueri_od1005",
        },
    },
    {
        "id": 56,
        "text": "How many cars are there in Zurich?",
        "function": random_facts.make_answer_fact("Autos", "cars"),
        "frontend_settings": {
            "id": 56,
            "chart_type": "map",
            "src_label": "https://data.stadt-zuerich.ch/dataset/prd_ssz_gang-dur-zueri_od1005",
        },
    },
    # TODO Autos pro hundert Personen (18 Jährige und Ältere)
    {
        "id": 57,
        "text": "How many Mobility statitions are there in Zurich?",
        "function": random_facts.make_answer_fact(
            "Mobility Standorte", "Mobility stations"
        ),
        "frontend_settings": {
            "id": 57,
            "chart_type": "map",
            "src_label": "https://data.stadt-zuerich.ch/dataset/prd_ssz_gang-dur-zueri_od1005",
        },
    },
    # Energy data
    {
        "id": [58, 59],
        "text": [
            "How much electricity does Zurich use?",
            "How did electricity use change during the pandemic?",
        ],
        "function": energy.power_weekly,
        "frontend_settings": {
            "id": 59,
            "chart_type": "line",
            "x_axis_time": True,
            "graph_label": "Power [kW] consumption (weekly average)",
            "domain_padding": {"y": 25},
            "src_label": "https://data.stadt-zuerich.ch/dataset/ewz_bruttolastgang_stadt_zuerich",
        },
    },
    {
        "id": [60],
        "text": ["How does energy use change over the course of a day?"],
        "function": energy.power_over_a_day,
        "frontend_settings": {
            "id": 60,
            "chart_type": "line",
            "graph_label": "Average power [kW] consumption by hour of day",
            "x_axis_hours": True,
            "src_label": "https://data.stadt-zuerich.ch/dataset/ewz_bruttolastgang_stadt_zuerich",
        },
    },
    {
        "id": [61],
        "text": ["How does energy use change over the course of a week?"],
        "function": energy.power_over_a_week,
        "frontend_settings": {
            "id": 61,
            "chart_type": "bar",
            "graph_label": "Average power [kW] consumption by weekday",
            "src_label": "https://data.stadt-zuerich.ch/dataset/ewz_bruttolastgang_stadt_zuerich",
        },
    },
    {
        "id": [62],
        "text": ["How does energy use change over the course of a year?"],
        "function": energy.power_over_a_year,
        "frontend_settings": {
            "id": 62,
            "chart_type": "line",
            "graph_label": "Average power [kW] consumption per day of year",
            "src_label": "https://data.stadt-zuerich.ch/dataset/sid_stapo_hundebestand",
        },
    },
    {
        "id": [63, 64, 65],
        "text": [
            "What is the dog gender distribution?",
            "How many male dogs are there?",
            "How many female dogs are there?",
        ],
        "function": dogs.dog_gender,
        "frontend_settings": {
            "id": 65,
            "chart_type": "pie",
            "src_label": "https://data.stadt-zuerich.ch/dataset/sid_stapo_hundebestand",
        },
    },
    {
        "id": [66, 67, 68],
        "text": [
            "What is the dog owner gender distribution?",
            "How many male dog owners are there?",
            "How many female dog owners are there?",
        ],
        "function": dogs.owner_gender,
        "frontend_settings": {
            "id": 68,
            "chart_type": "pie",
            "src_label": "https://data.stadt-zuerich.ch/dataset/sid_stapo_hundebestand",
        },
    },
    {
        "id": [69],
        "text": ["What dog breed is the most common?"],
        "function": dogs.dog_breed,
        "frontend_settings": {
            "id": 69,
            "chart_type": "bar",
            "hide_x_axis": True,
            "src_label": "https://data.stadt-zuerich.ch/dataset/sid_stapo_hundebestand",
        },
    },
    {
        "id": [70],
        "text": ["How many dogs are there in Zurich?"],
        "function": dogs.dogs_by_kreis,
        "frontend_settings": {
            "id": 70,
            "chart_type": "map",
            "src_label": "https://data.stadt-zuerich.ch/dataset/sid_stapo_hundebestand",
        },
    },
    {
        "id": [71, 72],
        "text": [
            "What age are dog owners in Zurich?",
            "How old are dog owners in Zurich?",
        ],
        "function": dogs.owner_age,
        "frontend_settings": {
            "id": 72,
            "chart_type": "bar",
            "hide_x_axis": True,
            "graph_label": "Number of owners per age group",
            "src_label": "https://data.stadt-zuerich.ch/dataset/sid_stapo_hundebestand",
        },
    },
    {
        "id": [73],
        "text": ["What is the highest number of dogs a person has in Zurich?"],
        "function": dogs.max_dog_count,
        "frontend_settings": {
            "id": 73,
            "chart_type": "number",
            "src_label": "https://data.stadt-zuerich.ch/dataset/sid_stapo_hundebestand",
        },
    },
    {
        "id": [74, 75],
        "text": ["When were dogs born in Zurich?", "What age are dogs in Zurich?"],
        "function": dogs.dog_age,
        "frontend_settings": {
            "id": 75,
            "chart_type": "bar",
            "graph_label": "Number of dogs born per year",
            "hide_x_axis": True,
            "src_label": "",
        },
    },
]

# print([question["id"][0] if isinstance(question["id"],list) else question["id"] for question in questions])

_questions = questions
questions = []
for group in _questions:
    assert isinstance(group["id"], list) == isinstance(group["text"], list)
    if isinstance(group["id"], list):
        assert len(group["id"]) == len(group["text"])
        for i in range(len(group["id"])):
            questions.append({**group, "id": group["id"][i], "text": group["text"][i]})
    else:
        questions.append(group)
