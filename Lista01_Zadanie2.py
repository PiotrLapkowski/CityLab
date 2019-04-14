import json
from math import radians, cos, sin, asin, sqrt
# ******** DANE JSON ********
my_json = {
  "data": [
    {
      "name": "Stary Zdrój",
      "category_list": [
        {
          "id": "2500",
          "name": "Local Business"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.77861111,
        "longitude": 16.29722222
      },
      "id": "915608055147221"
    },
    {
      "name": "Wałbrzych",
      "category_list": [
        {
          "id": "2404",
          "name": "City"
        },
        {
          "id": "2401",
          "name": "City"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.766666666667,
        "longitude": 16.283333333333,
        "zip": "58-300 to 58-309, 58-316"
      },
      "id": "213989378619748"
    },
    {
      "name": "Wałbrzych Twoje Miasto",
      "category_list": [
        {
          "id": "2401",
          "name": "City"
        },
        {
          "id": "209889829023118",
          "name": "Landmark & Historical Place"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.7848511,
        "longitude": 16.2863598,
        "street": "Wroclawksa",
        "zip": "58-301"
      },
      "id": "100102620344853"
    },
    {
      "name": "Szczawno-Zdrój",
      "category_list": [
        {
          "id": "2404",
          "name": "City"
        },
        {
          "id": "2401",
          "name": "City"
        }
      ],
      "location": {
        "city": "Szczawno-Zdrój",
        "country": "Poland",
        "latitude": 50.8103,
        "longitude": 16.25016,
        "zip": "58-310"
      },
      "id": "219987148012129"
    },
    {
      "name": "Lubomin, Walbrzych, Poland",
      "category_list": [
        {
          "id": "2404",
          "name": "City"
        },
        {
          "id": "2401",
          "name": "City"
        }
      ],
      "location": {
        "city": "Lubomin",
        "country": "Poland",
        "latitude": 50.806706338419,
        "longitude": 16.207846558941
      },
      "id": "215126905183753"
    },
    {
      "name": "Jedlina-Zdrój",
      "category_list": [
        {
          "id": "2404",
          "name": "City"
        },
        {
          "id": "2401",
          "name": "City"
        }
      ],
      "location": {
        "city": "Jedlina-Zdrój",
        "country": "Poland",
        "latitude": 50.72198,
        "longitude": 16.33557,
        "zip": "58-330"
      },
      "id": "219832171375545"
    },
    {
      "name": "Modliszów",
      "category_list": [
        {
          "id": "2404",
          "name": "City"
        },
        {
          "id": "2401",
          "name": "City"
        }
      ],
      "location": {
        "city": "Modliszów",
        "country": "Poland",
        "latitude": 50.794302012211,
        "longitude": 16.391055863239
      },
      "id": "200264406675350"
    },
    {
      "name": "Pogorzała",
      "category_list": [
        {
          "id": "2404",
          "name": "City"
        },
        {
          "id": "2401",
          "name": "City"
        }
      ],
      "location": {
        "city": "Pogorzala",
        "country": "Poland",
        "latitude": 50.806651544423,
        "longitude": 16.366022332519
      },
      "id": "214896858540218"
    },
    {
      "name": "Boguszów-Gorce",
      "category_list": [
        {
          "id": "2404",
          "name": "City"
        },
        {
          "id": "2401",
          "name": "City"
        }
      ],
      "location": {
        "city": "Boguszów-Gorce",
        "country": "Poland",
        "latitude": 50.7569,
        "longitude": 16.20733,
        "zip": "58-370 to 58-372"
      },
      "id": "226343374046372"
    },
    {
      "name": "Struga, Walbrzych, Poland",
      "category_list": [
        {
          "id": "2404",
          "name": "City"
        },
        {
          "id": "2401",
          "name": "City"
        }
      ],
      "location": {
        "city": "Struga",
        "country": "Poland",
        "latitude": 50.822867576551,
        "longitude": 16.227406022022
      },
      "id": "212437702114345"
    },
    {
      "name": "Sobięcin, Walbrzych, Poland",
      "category_list": [
        {
          "id": "2404",
          "name": "City"
        },
        {
          "id": "2401",
          "name": "City"
        }
      ],
      "location": {
        "city": "Sobiecin",
        "country": "Poland",
        "latitude": 50.7667,
        "longitude": 16.2333
      },
      "id": "225340014146603"
    },
    {
      "name": "Chełmiec, Walbrzych, Poland",
      "category_list": [
        {
          "id": "2404",
          "name": "City"
        },
        {
          "id": "2401",
          "name": "City"
        }
      ],
      "location": {
        "city": "Chełmiec",
        "country": "Poland",
        "latitude": 50.778150294714,
        "longitude": 16.213191747856
      },
      "id": "212423755448786"
    },
    {
      "name": "Boguszów, Walbrzych, Poland",
      "category_list": [
        {
          "id": "2404",
          "name": "City"
        },
        {
          "id": "2401",
          "name": "City"
        }
      ],
      "location": {
        "city": "Boguszów",
        "country": "Poland",
        "latitude": 50.75,
        "longitude": 16.2
      },
      "id": "202461349792381"
    },
    {
      "name": "Wałbrzyski Rynek",
      "category_list": [
        {
          "id": "2500",
          "name": "Local Business"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.765856487021,
        "longitude": 16.282595126917,
        "street": "Rynek 1",
        "zip": "58-300"
      },
      "id": "1895095067427349"
    },
    {
      "name": "Nowe Miasto",
      "category_list": [
        {
          "id": "2500",
          "name": "Local Business"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.772524521732,
        "longitude": 16.297416022998,
        "street": "Piłsudskiego",
        "zip": "58-301"
      },
      "id": "2010013549324631"
    },
    {
      "name": "Nieder Bad Salzbrunn, Walbrzych, Poland",
      "category_list": [
        {
          "id": "2404",
          "name": "City"
        },
        {
          "id": "2401",
          "name": "City"
        }
      ],
      "location": {
        "city": "Nieder Bad Salzbrunn",
        "country": "Poland",
        "latitude": 50.8167,
        "longitude": 16.3
      },
      "id": "213644831992636"
    },
    {
      "name": "Zamek Książ w Wałbrzychu",
      "category_list": [
        {
          "id": "279433649070367",
          "name": "Castle"
        },
        {
          "id": "209889829023118",
          "name": "Landmark & Historical Place"
        }
      ],
      "location": {
        "city": "Waldenburg",
        "country": "Poland",
        "latitude": 50.84217,
        "longitude": 16.29158,
        "street": "ul. Piastów Śląskich 1 58-306 Wałbrzych",
        "zip": "58-306"
      },
      "id": "383460848345377"
    },
    {
      "name": "AQUA ZDRÓJ Wałbrzych - Centrum Aktywnego Wypoczynku",
      "category_list": [
        {
          "id": "124887510918208",
          "name": "Public Swimming Pool"
        },
        {
          "id": "183013211744255",
          "name": "Recreation Center"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.784333911232,
        "longitude": 16.252046478525,
        "street": "Ratuszowa 6",
        "zip": "58-304"
      },
      "id": "643701708980307"
    },
    {
      "name": "Szkoła Tenisa - Łukasz Nowik",
      "category_list": [
        {
          "id": "1802",
          "name": "Coach"
        },
        {
          "id": "189018581118681",
          "name": "Sports Club"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.81824,
        "longitude": 16.28461,
        "street": "ul. Ogrodowa 19",
        "zip": "58-304"
      },
      "id": "1544323329010818"
    },
    {
      "name": "Wałbrzych Piaskowa Góra",
      "category_list": [
        {
          "id": "2500",
          "name": "Local Business"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.8201654,
        "longitude": 16.2743483,
        "street": "Broniewskiego",
        "zip": "58-309"
      },
      "id": "1563733237015523"
    },
    {
      "name": "An Ka - fotografia",
      "category_list": [
        {
          "id": "191969860827280",
          "name": "Photography Videography"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.78494,
        "longitude": 16.28644
      },
      "id": "1477967059001013"
    },
    {
      "name": "Jurand Wójcik",
      "category_list": [
        {
          "id": "1335670856447673",
          "name": "Musician"
        }
      ],
      "location": {
        "city": "Waldenburg",
        "country": "Poland",
        "latitude": 50.785101685482,
        "longitude": 16.28173828125,
        "zip": "58-302"
      },
      "id": "1004746669675155"
    },
    {
      "name": "Praktyka Fizjoterapii i Osteopatii Dr Ewa Żeligowska",
      "category_list": [
        {
          "id": "181885068517499",
          "name": "Physical Therapist"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.78272,
        "located_in": "1207896269225873",
        "longitude": 16.28306,
        "street": "Armii Krajowej 7A",
        "zip": "58-302"
      },
      "id": "1480180992117848"
    },
    {
      "name": "Pokoje Gościnne \"Andrzejówka\" Andrzej Sikoń",
      "category_list": [
        {
          "id": "505091123022329",
          "name": "Hotel & Lodging"
        }
      ],
      "location": {
        "city": "Szczawno-Zdrój",
        "country": "Poland",
        "latitude": 50.80549,
        "longitude": 16.24908,
        "street": "Wita Stwosza 5/1",
        "zip": "59-310"
      },
      "id": "358648364932579"
    },
    {
      "name": "Szczawienko, Walbrzych, Poland",
      "category_list": [
        {
          "id": "2404",
          "name": "City"
        },
        {
          "id": "2401",
          "name": "City"
        }
      ],
      "location": {
        "city": "Szczawienko",
        "country": "Poland",
        "latitude": 50.8125834,
        "longitude": 16.2950032
      },
      "id": "224969414187241"
    },
    {
      "name": "Stara Kopalnia - Centrum Nauki i Sztuki",
      "category_list": [
        {
          "id": "261213210912085",
          "name": "Science Museum"
        },
        {
          "id": "384382644921530",
          "name": "Art Museum"
        },
        {
          "id": "619759428190024",
          "name": "Cultural Center"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.772219895272,
        "longitude": 16.261540491228,
        "street": "ul. Wysockiego 29",
        "zip": "58-304"
      },
      "id": "892737320743054"
    },
    {
      "name": "2NP DŻINS",
      "category_list": [
        {
          "id": "2500",
          "name": "Local Business"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.78494,
        "longitude": 16.28644
      },
      "id": "424680874936347"
    },
    {
      "name": "ALEX KEBAB",
      "category_list": [
        {
          "id": "273819889375819",
          "name": "Restaurant"
        }
      ],
      "location": {
        "city": "Szczawno-Zdrój",
        "country": "Poland",
        "latitude": 50.8,
        "longitude": 16.25111,
        "street": "Solicka 6a",
        "zip": "58310"
      },
      "id": "313039225994948"
    },
    {
      "name": "Lubiechów (województwo lubuskie)",
      "category_list": [
        {
          "id": "2404",
          "name": "City"
        },
        {
          "id": "2401",
          "name": "City"
        }
      ],
      "location": {
        "city": "Lubiechów",
        "country": "Poland",
        "latitude": 50.8333,
        "longitude": 16.2833
      },
      "id": "209484602405231"
    },
    {
      "name": "Borowa Góra, Dolnośląskie, Góry Wałbrzyskie",
      "category_list": [
        {
          "id": "194201147294761",
          "name": "Mountain"
        }
      ],
      "location": {
        "city": "Jedlina-Zdrój",
        "country": "Poland",
        "latitude": 50.722931888696,
        "longitude": 16.304530485176
      },
      "id": "901351506593109"
    },
    {
      "name": "7niebo",
      "category_list": [
        {
          "id": "2500",
          "name": "Local Business"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.78494,
        "longitude": 16.28644
      },
      "id": "2189010114669667"
    },
    {
      "name": "Nowak Nails",
      "category_list": [
        {
          "id": "198516863494646",
          "name": "Nail Salon"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.78494,
        "longitude": 16.28644
      },
      "id": "315164609212639"
    },
    {
      "name": "Park Sobieskiego Wałbrzych",
      "category_list": [
        {
          "id": "204506149664245",
          "name": "State Park"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.7715114,
        "longitude": 16.2926596,
        "street": "Al.Wyzwolenia",
        "zip": "58-300"
      },
      "id": "154753071384425"
    },
    {
      "name": "Tattoo Clinic",
      "category_list": [
        {
          "id": "551469561691940",
          "name": "Tattoo & Piercing Shop"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.80457,
        "longitude": 16.28214,
        "street": "Główna 9/16",
        "zip": "58-309"
      },
      "id": "349130365845135"
    },
    {
      "name": "DieveHandmade",
      "category_list": [
        {
          "id": "1601",
          "name": "Artist"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.782931042951,
        "longitude": 16.285343170166
      },
      "id": "207784243452143"
    },
    {
      "name": "Szkoła Akrobatyki Sportowej \"Dziewiątka\"",
      "category_list": [
        {
          "id": "189018581118681",
          "name": "Sports Club"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.75454,
        "longitude": 16.265
      },
      "id": "247548262668637"
    },
    {
      "name": "Salon urody Bonita Wałbrzych",
      "category_list": [
        {
          "id": "1644814599176740",
          "name": "Skin Care Service"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.7614,
        "longitude": 16.28384,
        "street": "ADAMA MICKIEWICZA 40",
        "zip": "58-300"
      },
      "id": "340888876522691"
    },
    {
      "name": "B-10 City Lab",
      "category_list": [
        {
          "id": "2612",
          "name": "Community"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.771696357687,
        "located_in": "892737320743054",
        "longitude": 16.262040138245,
        "street": "Wysockiego 29",
        "zip": "58-304"
      },
      "id": "489910351433569"
    },
    {
      "name": "Dworzysko, Walbrzych, Poland",
      "category_list": [
        {
          "id": "2404",
          "name": "City"
        },
        {
          "id": "2401",
          "name": "City"
        }
      ],
      "location": {
        "city": "Dworzysko",
        "country": "Poland",
        "latitude": 50.80923376,
        "longitude": 16.26410038
      },
      "id": "214322265264628"
    },
    {
      "name": "Auto Pasja Bartłomiej Ratajczak",
      "category_list": [
        {
          "id": "625688294262999",
          "name": "Automotive Dealership"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.77874,
        "longitude": 16.27848,
        "street": "B.Chrobrego 57",
        "zip": "58-300"
      },
      "id": "1249689841832306"
    },
    {
      "name": "Biały Kamien, Walbrzych, Poland",
      "category_list": [
        {
          "id": "2404",
          "name": "City"
        },
        {
          "id": "2401",
          "name": "City"
        }
      ],
      "location": {
        "city": "Biały Kamien",
        "country": "Poland",
        "latitude": 50.7833,
        "longitude": 16.25
      },
      "id": "208879119133092"
    },
    {
      "name": "Stary Julianow, Walbrzych, Poland",
      "category_list": [
        {
          "id": "2404",
          "name": "City"
        },
        {
          "id": "2401",
          "name": "City"
        }
      ],
      "location": {
        "city": "Stary Julianow",
        "country": "Poland",
        "latitude": 50.8,
        "longitude": 16.3667
      },
      "id": "209649699056150"
    },
    {
      "name": "Wałbrzych Podzamcze",
      "category_list": [
        {
          "id": "192049437499122",
          "name": "Residence"
        },
        {
          "id": "1713595685546855",
          "name": "City Infrastructure"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.822192349946,
        "longitude": 16.274418165829,
        "zip": "58-316"
      },
      "id": "197715116955539"
    },
    {
      "name": "Sępy Starożytności",
      "category_list": [
        {
          "id": "209889829023118",
          "name": "Landmark & Historical Place"
        }
      ],
      "location": {
        "city": "Waldenburg",
        "country": "Poland",
        "latitude": 50.772917649865,
        "longitude": 16.28922700882
      },
      "id": "864655960592240"
    },
    {
      "name": "Klinika Lakieru Detailing & Wrapping",
      "category_list": [
        {
          "id": "2205",
          "name": "Cars"
        },
        {
          "id": "1033987526649038",
          "name": "Auto Detailing Service"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.77749,
        "longitude": 16.27616,
        "street": "ul. Chrobrego 51",
        "zip": "58-300"
      },
      "id": "326036731355803"
    },
    {
      "name": "Strefa Emocji",
      "category_list": [
        {
          "id": "206714069358248",
          "name": "Psychologist"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.77343,
        "longitude": 16.28067
      },
      "id": "286264578757894"
    },
    {
      "name": "KEBAB CROWN 24H",
      "category_list": [
        {
          "id": "273819889375819",
          "name": "Restaurant"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.80811,
        "longitude": 16.2788,
        "street": "Kusocińskiego 21 Box 30",
        "zip": "58-309"
      },
      "id": "499821887095398"
    },
    {
      "name": "Lakiernia Proszkowa Gemmer",
      "category_list": [
        {
          "id": "176831012360626",
          "name": "Professional Service"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.815127607326,
        "longitude": 16.309225559235,
        "street": "Stacyjna 12",
        "zip": "58-306"
      },
      "id": "308868915927894"
    },
    {
      "name": "Cinema City Poland",
      "category_list": [
        {
          "id": "192511100766680",
          "name": "Movie Theater"
        },
        {
          "id": "109527622457518",
          "name": "Shopping Mall"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.766647097724,
        "located_in": "221357711212666",
        "longitude": 16.265458088158,
        "street": "1 Maja 64",
        "zip": "58 – 300"
      },
      "id": "132244357308884"
    },
    {
      "name": "Tam Gdzie Serce Bije Spokojniej",
      "category_list": [
        {
          "id": "635235176664335",
          "name": "Outdoor Recreation"
        },
        {
          "id": "2405",
          "name": "Neighborhood"
        }
      ],
      "location": {
        "city": "Polska",
        "country": "Poland",
        "latitude": 50.798892650015,
        "longitude": 16.249143300037
      },
      "id": "151636618554568"
    },
    {
      "name": "Egzaminator.com.pl - Nauka jazdy Wałbrzych",
      "category_list": [
        {
          "id": "200010220031917",
          "name": "Driving School"
        },
        {
          "id": "1758418281071392",
          "name": "Local Service"
        },
        {
          "id": "2601",
          "name": "School"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.77191,
        "longitude": 16.27754,
        "street": "Szmidta 4a/3",
        "zip": "58-300"
      },
      "id": "2181775538809683"
    },
    {
      "name": "Kuźnice Świdnickie, Walbrzych, Poland",
      "category_list": [
        {
          "id": "2404",
          "name": "City"
        },
        {
          "id": "2401",
          "name": "City"
        }
      ],
      "location": {
        "city": "Kuznice Swidnickie",
        "country": "Poland",
        "latitude": 50.7333,
        "longitude": 16.2333
      },
      "id": "208594145839335"
    },
    {
      "name": "Boguszów-Gorce Newsy i Informacje",
      "category_list": [
        {
          "id": "1404",
          "name": "TV Channel"
        }
      ],
      "location": {
        "city": "Boguszów-Gorce",
        "country": "Poland",
        "latitude": 50.757666357148,
        "longitude": 16.203648642862,
        "street": "Rynek 1",
        "zip": "58-370"
      },
      "id": "1516146475125125"
    },
    {
      "name": "OSTEO MED",
      "category_list": [
        {
          "id": "181885068517499",
          "name": "Physical Therapist"
        },
        {
          "id": "192781160749720",
          "name": "Chiropractor"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.76361,
        "located_in": "2114827288742701",
        "longitude": 16.283,
        "street": "Młynarska 24",
        "zip": "58-300"
      },
      "id": "1411490782247528"
    },
    {
      "name": "Wałbrzych - Nasze Miasto",
      "category_list": [
        {
          "id": "2233",
          "name": "Media/News Company"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.76576585235,
        "longitude": 16.282811164856,
        "street": "Rynek 9",
        "zip": "58-309"
      },
      "id": "2877831978909618"
    },
    {
      "name": "Loombard Wałbrzych Limanowskiego 1",
      "category_list": [
        {
          "id": "284922938257468",
          "name": "Pawn Shop"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.76805,
        "longitude": 16.27976,
        "street": "Limanowskiego 1",
        "zip": "58-300"
      },
      "id": "236650183697919"
    },
    {
      "name": "UL-KA Urszula Nowicka",
      "category_list": [
        {
          "id": "179576078750378",
          "name": "Fashion Designer"
        }
      ],
      "location": {
        "city": "Waldenburg",
        "country": "Poland",
        "latitude": 50.7667,
        "longitude": 16.2833
      },
      "id": "619950158460317"
    },
    {
      "name": "VapeStacja Wałbrzych",
      "category_list": [
        {
          "id": "200600219953504",
          "name": "Shopping & Retail"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.803401405,
        "longitude": 16.293095164,
        "street": "Wrocławska 45",
        "zip": "58-309"
      },
      "id": "200618017275677"
    },
    {
      "name": "Studio Graficzne Jarosław Grycaj",
      "category_list": [
        {
          "id": "164886566892249",
          "name": "Advertising Agency"
        },
        {
          "id": "162183907165552",
          "name": "Graphic Designer"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.78942,
        "longitude": 16.25507
      },
      "id": "316748455578604"
    },
    {
      "name": "Dobre-Rzeczy pracownia rękodzieła",
      "category_list": [
        {
          "id": "153635828025130",
          "name": "Arts & Crafts Store"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.76309,
        "longitude": 16.28366
      },
      "id": "521371144938061"
    },
    {
      "name": "Jubiler",
      "category_list": [
        {
          "id": "1758418281071392",
          "name": "Local Service"
        },
        {
          "id": "2201",
          "name": "Product/Service"
        },
        {
          "id": "188031587886173",
          "name": "Jewelry & Watches Store"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.81062,
        "located_in": "537255086643594",
        "longitude": 16.29252,
        "street": "Długa 5a",
        "zip": "58-309"
      },
      "id": "786657431674115"
    },
    {
      "name": "Oaza Piękna Wałbrzych",
      "category_list": [
        {
          "id": "1644814599176740",
          "name": "Skin Care Service"
        },
        {
          "id": "174177802634376",
          "name": "Hair Salon"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.78941,
        "longitude": 16.25574,
        "street": "ul. Andersa 132",
        "zip": "58-304"
      },
      "id": "940105282831666"
    },
    {
      "name": "MKS Szczawno-Zdrój - aktualna strona klubu",
      "category_list": [
        {
          "id": "189018581118681",
          "name": "Sports Club"
        }
      ],
      "location": {
        "city": "Szczawno-Zdrój",
        "country": "Poland",
        "latitude": 50.80646,
        "longitude": 16.25737,
        "street": "Topolowa 5",
        "zip": "58-310"
      },
      "id": "212095286282146"
    },
    {
      "name": "AlleKoszulki",
      "category_list": [
        {
          "id": "2201",
          "name": "Product/Service"
        },
        {
          "id": "186230924744328",
          "name": "Clothing Store"
        },
        {
          "id": "162183907165552",
          "name": "Graphic Designer"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.7667,
        "longitude": 16.2833
      },
      "id": "1417340361736366"
    },
    {
      "name": "Opium Salon Kosmetyczny",
      "category_list": [
        {
          "id": "174177802634376",
          "name": "Hair Salon"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.80878,
        "longitude": 16.28361,
        "street": "ul. Główna 9/17",
        "zip": "58-309"
      },
      "id": "920694018141202"
    },
    {
      "name": "Projekt odchudzający Nakurw#%&am i NIE patrzę NA NIC",
      "category_list": [
        {
          "id": "964585346994407",
          "name": "Sports"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.76932,
        "longitude": 16.27591,
        "street": "ul. Pługa 12a",
        "zip": "58-300"
      },
      "id": "623735644744184"
    },
    {
      "name": "Bad Salzbrunn, Walbrzych, Poland",
      "category_list": [
        {
          "id": "2404",
          "name": "City"
        },
        {
          "id": "2401",
          "name": "City"
        }
      ],
      "location": {
        "city": "Bad Salzbrunn",
        "country": "Poland",
        "latitude": 50.8167,
        "longitude": 16.2833
      },
      "id": "207734902591589"
    },
    {
      "name": "Myjnia Samochodowa Wałbrzych Cichy Cars",
      "category_list": [
        {
          "id": "162295707155272",
          "name": "Car Wash"
        }
      ],
      "location": {
        "city": "Waldenburg",
        "country": "Poland",
        "latitude": 50.7667,
        "longitude": 16.2833,
        "street": "ul. Kombatantów 2",
        "zip": "58-302"
      },
      "id": "2338019579775830"
    },
    {
      "name": "NATALIA SOBCZYK",
      "category_list": [
        {
          "id": "557045641143373",
          "name": "Design & Fashion"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.81116,
        "longitude": 16.278
      },
      "id": "508621552997643"
    },
    {
      "name": "U Mamuśki",
      "category_list": [
        {
          "id": "2500",
          "name": "Local Business"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.80957,
        "longitude": 16.28035,
        "street": "Broniewskiego 71",
        "zip": "58-309"
      },
      "id": "1889875074439123"
    },
    {
      "name": "Górnik Toyota Wałbrzych- koszykówka na wózkach",
      "category_list": [
        {
          "id": "1803",
          "name": "Amateur Sports Team"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.77104,
        "located_in": "1322232021172658",
        "longitude": 16.27342,
        "street": "Ul.Wysockiego 11 a",
        "zip": "58-300"
      },
      "id": "2240601489552364"
    },
    {
      "name": "Oskar Winiarski Swim&Ski",
      "category_list": [
        {
          "id": "186982054657561",
          "name": "Sports & Recreation"
        }
      ],
      "location": {
        "city": "Waldenburg",
        "country": "Poland",
        "latitude": 50.7667,
        "longitude": 16.2833
      },
      "id": "258105778432767"
    },
    {
      "name": "Kubek w kubek",
      "category_list": [
        {
          "id": "153635828025130",
          "name": "Arts & Crafts Store"
        }
      ],
      "location": {
        "city": "Waldenburg",
        "country": "Poland",
        "latitude": 50.7667,
        "longitude": 16.2833
      },
      "id": "212688979661071"
    },
    {
      "name": "Aqua Polis Akwarystyka morska",
      "category_list": [
        {
          "id": "635663076586942",
          "name": "Aquarium"
        },
        {
          "id": "209645989430607",
          "name": "Aquatic Pet Store"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.76007,
        "longitude": 16.27816,
        "street": "Moniuszki 66 II",
        "zip": "58-309"
      },
      "id": "506102056393394"
    },
    {
      "name": "MG Concept - Kuchnie na wymiar",
      "category_list": [
        {
          "id": "2219",
          "name": "Furniture"
        },
        {
          "id": "199438050070864",
          "name": "Interior Design Studio"
        },
        {
          "id": "192647794097278",
          "name": "Home Decor"
        }
      ],
      "location": {
        "city": "Waldenburg",
        "country": "Poland",
        "latitude": 50.811100860198,
        "located_in": "10150168641637974",
        "longitude": 16.291791200638,
        "street": "Długa 2",
        "zip": "58-309"
      },
      "id": "1224453824374870"
    },
    {
      "name": "MOTOBrothers",
      "category_list": [
        {
          "id": "1801",
          "name": "Sports Team"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.7667,
        "longitude": 16.2833
      },
      "id": "2035388496758891"
    },
    {
      "name": "Skup Sprzedaż \"Oskarini\"",
      "category_list": [
        {
          "id": "284922938257468",
          "name": "Pawn Shop"
        }
      ],
      "location": {
        "city": "Waldenburg",
        "country": "Poland",
        "latitude": 50.7667,
        "longitude": 16.2833,
        "street": "Piłsudskiego 54"
      },
      "id": "434982843908404"
    },
    {
      "name": "Taxi Wałbrzych 19191",
      "category_list": [
        {
          "id": "184395321600410",
          "name": "Cargo & Freight Company"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.77191,
        "located_in": "1517943258420323",
        "longitude": 16.27754,
        "street": "Szmidta 4A",
        "zip": "58-300"
      },
      "id": "2174969559251291"
    },
    {
      "name": "Loombard Wałbrzych Andersa 148",
      "category_list": [
        {
          "id": "284922938257468",
          "name": "Pawn Shop"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.79117,
        "longitude": 16.25508,
        "street": "Andersa 148",
        "zip": "58-304"
      },
      "id": "242056926475418"
    },
    {
      "name": "WorkProfi",
      "category_list": [
        {
          "id": "124736910930693",
          "name": "Recruiter"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.80536,
        "longitude": 16.28077,
        "street": "Broniewskiego 1B",
        "zip": "58-309"
      },
      "id": "398246167653036"
    },
    {
      "name": "Bardotka - Markowa odzież używana",
      "category_list": [
        {
          "id": "170241263022353",
          "name": "Men's Clothing Store"
        },
        {
          "id": "192614304101075",
          "name": "Baby & Children's Clothing Store"
        },
        {
          "id": "109512302457693",
          "name": "Footwear Store"
        }
      ],
      "location": {
        "city": "Szczawno-Zdrój",
        "country": "Poland",
        "latitude": 50.80174,
        "longitude": 16.25463,
        "street": "Zacisze, ul. Kościuszki 14/ Kusocińskiego 5 Wałbrzych",
        "zip": "58-310"
      },
      "id": "685084425160958"
    },
    {
      "name": "SR66 Design",
      "category_list": [
        {
          "id": "186712678028215",
          "name": "Automotive Customization Shop"
        },
        {
          "id": "2201",
          "name": "Product/Service"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.783527979692,
        "longitude": 16.284656524658
      },
      "id": "1537777652963736"
    },
    {
      "name": "SpawPol - Konstrukcje stalowe / spawanie precyzyjne",
      "category_list": [
        {
          "id": "1758418281071392",
          "name": "Local Service"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.7667,
        "longitude": 16.2833,
        "street": "11 Listopada"
      },
      "id": "278707722814979"
    },
    {
      "name": "Crochet Ornaments PL",
      "category_list": [
        {
          "id": "153635828025130",
          "name": "Arts & Crafts Store"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.788,
        "longitude": 16.27474,
        "street": "Zeromskiego 62",
        "zip": "58-302"
      },
      "id": "1467206666742806"
    },
    {
      "name": "Loombard Wałbrzych Główna 9",
      "category_list": [
        {
          "id": "284922938257468",
          "name": "Pawn Shop"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.80878,
        "longitude": 16.28361,
        "street": "Główna 9",
        "zip": "58-309"
      },
      "id": "286139772209980"
    },
    {
      "name": "Rol Okna Drzwi Rolety",
      "category_list": [
        {
          "id": "192041444166324",
          "name": "Window Installation Service"
        },
        {
          "id": "530126207179123",
          "name": "Construction Company"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.77228,
        "longitude": 16.2631,
        "street": "ul. Wysockiego 27",
        "zip": "58-300"
      },
      "id": "2051827734884985"
    },
    {
      "name": "Waldenburg In Schlesien, Walbrzych, Poland",
      "category_list": [
        {
          "id": "2404",
          "name": "City"
        },
        {
          "id": "2401",
          "name": "City"
        }
      ],
      "location": {
        "city": "Waldenburg in Schlesien",
        "country": "Poland",
        "latitude": 50.7667,
        "longitude": 16.2833
      },
      "id": "208354045852084"
    },
    {
      "name": "KUKIZ'15 • Wałbrzych",
      "category_list": [
        {
          "id": "373543049350668",
          "name": "Political Organization"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.76876,
        "longitude": 16.27919,
        "street": "Słowackiego 8",
        "zip": "58-300"
      },
      "id": "327354054521879"
    },
    {
      "name": "Pracownia Meblovelove",
      "category_list": [
        {
          "id": "1758418281071392",
          "name": "Local Service"
        }
      ],
      "location": {
        "city": "Szczawno-Zdrój",
        "country": "Poland",
        "latitude": 50.79762,
        "longitude": 16.25599,
        "street": "Okrężna 24",
        "zip": "58-310"
      },
      "id": "328618114647744"
    },
    {
      "name": "Broda t-shirt",
      "category_list": [
        {
          "id": "1758418281071392",
          "name": "Local Service"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.80738,
        "longitude": 16.27612
      },
      "id": "268627540654100"
    },
    {
      "name": "Weissstein, Walbrzych, Poland",
      "category_list": [
        {
          "id": "2404",
          "name": "City"
        },
        {
          "id": "2401",
          "name": "City"
        }
      ],
      "location": {
        "city": "Weissstein",
        "country": "Poland",
        "latitude": 50.7833,
        "longitude": 16.25
      },
      "id": "225451600802567"
    },
    {
      "name": "Spa dla Psa",
      "category_list": [
        {
          "id": "144982405562750",
          "name": "Pet Service"
        }
      ],
      "location": {
        "city": "Wałbrzych",
        "country": "Poland",
        "latitude": 50.8,
        "longitude": 16.28386,
        "street": "Orłowicza 61",
        "zip": "58-309"
      },
      "id": "995123927543666"
    }
  ],
  "paging": {
    "cursors": {
      "after": "OTkZD"
    },
    "next": "https://graph.facebook.com/v3.2/search?access_token=1418473451755042%7CSJ2jUAD3JfcMulM0u83o6Sd9pSQ&pretty=0&fields=%5B%27name%27%2C+%27category_list%27%2C+%27location%27%5D&type=place&center=50.7840092%2C16.2843553&distance=8000&limit=100&after=OTkZD"
  }
}
# ******** PROCEDURY ********

def SprawdzenieLiczby(tekst_zachety, komunikat_bledu):
    liczba = ''
    while not liczba.replace('.','',1).isdigit():
        liczba = input(tekst_zachety)
        if not liczba.replace('.','',1).isdigit():
            print(komunikat_bledu)
            liczba = ''
        else:
            return float(liczba)
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 

    # 6371 km is the radius of the Earth
    km = 6371 * c
    return km 

w = my_json ['data']
print ("Witaj użytkowniku! Z okolicy znajduje się " + str(len(w)) + " miejsca, które warto odwiedzić")
print ("Podaj współrzędne swojego położenia celem wyznaczenia ciekawych obiektów w twojej okolicy (1000m)")
wsp_dlugosc = SprawdzenieLiczby("Długość geograficzna:"," Błędnie podana długość")
wsp_szerokosc = SprawdzenieLiczby("Szerokość geograficzna:","Błędnie podana Szerokość")
#print (wsp_dlugosc, wsp_szerokosc)
#wsp_dlugosc=16.2843553 
#wsp_szerokosc= 50.7840092
print ("W okolicy 1 kilometra od podanej lokalizacji znajdują się:")
j=1
for i in range(len(w)):    
    wsp_szer = w[i]['location']['latitude']
    wsp_dlug =w[i]['location']['longitude']
    odl = haversine(wsp_dlugosc, wsp_szerokosc, wsp_dlug, wsp_szer)
    if odl <= 1.0:
        nazwa =w[i]['name']
        print ( str(j) + ". " + nazwa + " odległość "+ str(f"{odl:.2f}") + " km")
        j += 1

