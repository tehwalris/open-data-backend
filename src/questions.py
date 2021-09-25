from . import air_quality
from . import random_facts
from . import energy
from . import dogs

questions = [
  {
    'id': 1,
    'text': "How much carbon monoxide is there in Zurich?",
    'function': air_quality.make_answer_pollutant_over_time('CO'),
  },
  {
    'id': 6,
    'text': "How much nitrogen monoxide is there in Zurich?",
    'function': air_quality.make_answer_pollutant_over_time('NO'),
  },
  {
    'id': 7,
    'text': "How much nitrogen dioxide is there in Zurich?",
    'function': air_quality.make_answer_pollutant_over_time('NO2'),
  },
  {
    'id': [8, 9],
    'text': [
      "How much particulate matter is there in Zurich?",
      "How much PM10 is there in Zurich?",
    ],
    'function': air_quality.make_answer_pollutant_over_time('PM10'),
  },
  {
    'id': 10,
    'text': "How much PM2.5 is there in Zurich?",
    'function': air_quality.make_answer_pollutant_over_time('PM2.5'),
  },
  {
    'id': 11,
    'text': "How much sulfur dioxide is there in Zurich?",
    'function': air_quality.make_answer_pollutant_over_time('SO2'),
  },
  {
    'id': 2,
    'text': "How much ozone is there in Zurich?",
    'function': air_quality.make_answer_pollutant_over_time('O3'),
  },

  {
    'id': [3, 12],
    'text': [
      "Is air pollution in Zurich getting worse?",
      "How did air pollution in Zurich change over time?",
    ],
    'function': air_quality.answer_combined_over_time,
  },
  {
    'id': [4, 5],
    'text': [
      'How much pollution is there in Zurich?',
      'What contributes to air pollution?',
    ],
    'function': air_quality.answer_pollutant_table,
  },
  {
    'id': 13,
    'text': "How does air pollution in Zurich change throughout the year?",
    'function': air_quality.answer_over_year,
  },
  {
    'id': 14,
    'text': "How does air pollution in Zurich change throughout the day?",
    'function': air_quality.answer_over_day,
  },

  {
    'id': [18, 19],
    'text': [
      "How big are the districts of Zurich?",
      "What's the area of Zurich?",
    ],
    'function': random_facts.make_answer_fact('Fläche in Quadratkilometer', 'km²'),
  },
  {
    'id': [20, 21],
    'text': [
      "How much forest is there in Zurich?",
      "What area of Zurich is covered by forest?",
    ],
    'function': random_facts.make_answer_fact('Anteil der Waldfläche in %', '%'),
  },
  {
    'id': 22,
    'text': "What area of Zurich is covered by water?",
    'function': random_facts.make_answer_fact('Anteil der Gewässerfläche in %', '%'),
  },
  {
    'id': 23,
    'text': "How many drinking fountains are there in Zurich?",
    'function': random_facts.make_answer_fact('Brunnen', 'fountains'),
  },
  {
    'id': 24,
    'text': "How many trees are there on the streets of Zurich?",
    'function': random_facts.make_answer_fact('Bäume', 'trees'),
  },
  {
    'id': 25,
    'text': "How many primary schools are there in Zurich?",
    'function': random_facts.make_answer_fact('Schulen (Volksschule)', 'schools'),
  },
  {
    'id': 26,
    'text': "How many primary schools are there in Zurich?",
    'function': random_facts.make_answer_fact('Schulen (Volksschule)', 'schools'),
  },
  {
    'id': [27, 28],
    'text': [
      "What is the population of Zurich?",
      "How many people live in Zurich?",
    ],
    'function': random_facts.make_answer_fact('Wohnbevölkerung (Anzahl Personen)', 'people'),
  },
  {
    'id': 29,
    'text': "How many babies are born in Zurich every year?",
    'function': random_facts.make_answer_fact('Neugeborene pro Jahr', 'babies'),
  },
  {
    'id': 30,
    'text': "How many people die in Zurich every year?",
    'function': random_facts.make_answer_fact('Todesfälle pro Jahr', 'deaths'),
  },
  {
    'id': 31,
    'text': "How many people move to Zurich every year?",
    'function': random_facts.make_answer_fact('Zuziehende (Anzahl Personen pro Jahr)', 'people'),
  },
  {
    'id': 32,
    'text': "How many people move away from Zurich every year?",
    'function': random_facts.make_answer_fact('Wegziehende (Anzahl Personen pro Jahr)', 'people'),
  },
  {
    'id': 33,
    'text': "How many foreigners live in Zurich?",
    'function': random_facts.make_answer_fact('Ausländeranteil in %', '%'),
  },
  # TODO: "Häufigste ausländische Nationalität (Anzahl Personen)"
  {
    'id': 34,
    'text': "How old is the oldest woman in Zurich?",
    'function': random_facts.make_answer_fact('Älteste Frau (Alter)', 'years old'),
  },
  {
    'id': 35,
    'text': "How old is the oldest man in Zurich?",
    'function': random_facts.make_answer_fact('Ältester Mann (Alter)', 'years old'),
  },
  # TODO: Oldest person ignoring gender
  {
    'id': [36, 37],
    'text': [
      "How many single-member households are there in Zurich?",
      "How many people in Zurich live alone?", # HACK not the same question
    ],
    'function': random_facts.make_answer_fact('Einpersonen-Haushalte (Anteil an allen Haushalten in %)', '%'),
  },
  {
    'id': [37, 38],
    'text': [
      "How many households in Zurich have children?",
      "How many people in Zurich live with kids?", # HACK not the same question
    ],
    'function': random_facts.make_answer_fact('Haushalte mit Kindern (Anteil an allen Haushalten in %)', '%'),
  },
  {
    'id': 39,
    'text': "How many apartments are there in Zurich?",
    'function': random_facts.make_answer_fact('Wohnungen', 'apartments'),
  },
  {
    'id': 40,
    'text': "How many apartments were built in Zurich the last 5 years?",
    'function': random_facts.make_answer_fact('Neubauwohnungen der letzten fünf Jahre', 'apartments'),
  },
  {
    'id': 41,
    'text': "How many apartments were destroyed in Zurich the last 5 years?",
    'function': random_facts.make_answer_fact('Abgebrochene Wohnungen der letzten fünf Jahre', 'apartments'),
  },
  {
    'id': [42, 43],
    'text': [
      "What is the average living space in Zurich?",
      "How many square meters do people in Zurich live in?",
    ],
    'function': random_facts.make_answer_fact('Durchschnittliche Wohnfläche (Quadratmeter pro Person)', 'm²'),
  },
  {
    'id': 44,
    'text': "How many buildings in Zurich are older than 100?",
    'function': random_facts.make_answer_fact('Anzahl über 100-jährige Gebäude', 'buildings'),
  },
  {
    'id': [45, 46],
    'text': [
      "When was the oldest building in Zurich built?",
      "How old is the oldest building in Zurich?",
    ],
    'function': random_facts.make_answer_fact('Baujahr des ältesten Gebäudes (Adresse', ''),
  },
  {
    'id': [15, 16, 17],
    'text': [
      "How tall is the tallest building in Zurich?",
      "How many floors does the biggest building in Zurich have?",
      "Where is the tallest building in Zurich?",
    ],
    'function': random_facts.make_answer_fact('Anzahl Stockwerke des höchsten Gebäudes (Adresse', 'floors'),
  },
  {
    'id': [47, 48],
    'text': [
      "How many single-family houses are there in Zurich?",
      "How many detached houses are there in Zurich?",
    ],
    'function': random_facts.make_answer_fact('Einfamilienhäuser', 'houses'),
  },
  {
    'id': 49,
    'text': "How many tram and bus stops are there in Zurich?",
    'function': random_facts.make_answer_fact('Tram- und Buswartehäuschen', 'stops'),
  },
  {
    'id': 50,
    'text': "How many people work in zurich?",
    'function': random_facts.make_answer_fact('Beschäftigte', 'people'),
  },
  # TODO Beschäftigte im 1. Sektor, ...
  {
    'id': 51,
    'text': "How many people in zurich are unemployed?",
    'function': random_facts.make_answer_fact('Arbeitslose', 'people'),
  },
  {
    'id': 52,
    'text': "Whats the unemployment rate in Zurich?",
    'function': random_facts.make_answer_fact('Arbeitslosenquote in %', '%'),
  },
  {
    'id': 53,
    'text': "How many doctors offices are there in Zurich?",
    'function': random_facts.make_answer_fact('Arztpraxen (Allgemeinmedizin und Fachärzte)', 'offices'),
  },
  {
    'id': 54,
    'text': "How many dentists are there in Zurich?",
    'function': random_facts.make_answer_fact('Zahnarztpraxen', 'dentists'),
  },
  {
    'id': 55,
    'text': "How many motorbikes are there in Zurich?",
    'function': random_facts.make_answer_fact('Motorräder', 'motorbikes'),
  },
  {
    'id': 56,
    'text': "How many cars are there in Zurich?",
    'function': random_facts.make_answer_fact('Autos', 'cars'),
  },
  # TODO Autos pro hundert Personen (18 Jährige und Ältere)
  {
    'id': 57,
    'text': "How many Mobility statitions are there in Zurich?",
    'function': random_facts.make_answer_fact('Mobility Standorte', 'Mobility stations'),
  },
  # Energy data
   {
    'id': [58,59],
    'text': [
      "How much electricity does Zurich use?",
      "How did electricity use change during the pandemic?",
    ],
    'function': energy.power_weekly,
  },
  {
    'id': [60],
    'text': [
      "How does energy use change over the course of a day?"
    ],
    'function': energy.power_over_a_day,
  },
  {
    'id': [61],
    'text': [
      "How does energy use change over the course of a week?"
    ],
    'function': energy.power_over_a_week,
  }, 
  {
    'id': [62],
    'text': [
      "How does energy use change over the course of a year?"
    ],
    'function': energy.power_over_a_year,
  }, 
  {
    'id': [63],
    'text': [
      "Dog Gender"
    ],
    'function': dogs.dog_gender,
  }
]

_questions = questions
questions = []
for group in _questions:
  assert isinstance(group['id'], list) == isinstance(group['text'], list)
  if isinstance(group['id'], list):
    assert len(group['id']) == len(group['text'])
    for i in range(len(group['id'])):
      questions.append({ **group, 'id': group['id'][i], 'text': group['text'][i] })
  else:
    questions.append(group)
