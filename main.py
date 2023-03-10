import cairo
import uuid
import time
import math
import random
import argparse
from PIL import Image, ImageDraw, ImageFont
import numpy as np



def solarsystem():

    list_of_colors = [
        (145, 185, 141), (229, 192, 121), (210, 191, 88), (140, 190, 178), (255, 183, 10), (189, 190, 220),
        (221, 79, 91), (16, 182, 98), (227, 146, 80), (241, 133, 123), (110, 197, 233), (235, 205, 188), (197, 239, 247), (190, 144, 212),
        (41, 241, 195), (101, 198, 187), (255, 246, 143), (243, 156, 18), (189, 195, 199), (243, 241, 239)
        ]

    list_of_sun_colors = [
        (255, 95, 83), (253, 209, 162), (255, 243, 161), (252, 255, 212), (248, 247, 253), (201, 216, 255), (154, 175, 255)
        ]

    list_of_planet_textures = ['craters', 'fibers', 'nubi', 'perlin_poly', 'stripes', 'voronoi']
    def planet_name():
        part1 = [
            "Æ",
            "Arc",
            "A",
            "Ab",
            "Ag",
            "At",
            "Am",
            "Amon",
            "An",
            "Ant",
            "Aer",
            "Aeria",
            "Ar",
            "Aria",
            "Atar",
            "Astar",
            "Ana",
            "Av",
            "Ba",
            "Ban",
            "Bant",
            "Bar",
            "Be",
            "Bet",
            "Bi",
            "Bro",
            "Bo",
            "Bon",
            "Brum",
            "B’",
            "Ca",
            "Camp",
            "Car",
            "Carr",
            "Ce",
            "Cer",
            "Ci",
            "Clo",
            "Chur",
            "Cold",
            "Con",
            "Coper",
            "Corr",
            "Cu",
            "Cy",
            "C’",
            "Da",
            "Dark",
            "De",
            "Del",
            "Deep",
            "Dep",
            "Der",
            "Dikar",
            "Du",
            "Dur",
            "Dun",
            "E",
            "Ea",
            "El",
            "Er",
            "Exo",
            "Far",
            "Fox",
            "Fog",
            "Fon",
            "Fur",
            "Fun",
            "Fung",
            "Galad",
            "Gan",
            "Gunt",
            "Gren",
            "H",
            "Hub",
            "Har",
            "Haar",
            "Hark",
            "Hel",
            "Hon",
            "Hed",
            "Ib",
            "Ich",
            "Ian",
            "Int",
            "Iv",
            "Jan",
            "Ko",
            "K'",
            "Kaan",
            "Khan",
            "Kne",
            "Ken",
            "Ket",
            "Kep",
            "Ku",
            "Klin",
            "Lad",
            "Leg",
            "Lig",
            "Lo",
            "Lo",
            "Lone",
            "Long",
            "L'",
            "Ll'",
            "Majest",
            "Maz",
            "Mer",
            "Merg",
            "Merc",
            "Miran",
            "Mun",
            "Nar",
            "Nan",
            "Nad",
            "Nas",
            "Night",
            "Nir",
            "Nit",
            "Nib",
            "Non",
            "No",
            "Ob",
            "Ox",
            "Out",
            "Ov",
            "Oz",
            "Pa",
            "Pat",
            "Pap",
            "Pan",
            "Pert",
            "Plane",
            "Plu",
            "Plo",
            "Pro",
            "Pra",
            "Pran",
            "Por",
            "Pool",
            "Pling",
            "Py",
            "Pyro",
            "Rem",
            "Ran",
            "Rus",
            "Sai",
            "S'",
            "So'",
            "Sat",
            "Sen",
            "Sev",
            "Shan",
            "Shandak",
            "Siden",
            "Sizen",
            "Sot",
            "Sop",
            "Sot Ank",
            "Sot Lo",
            "Son",
            "Scar",
            "Steep",
            "Suil",
            "Sul",
            "Sum",
            "Sun",
            "Sva",
            "Syn",
            "T",
            "Tac",
            "Tad",
            "Taf",
            "Tag",
            "Tai",
            "Tal",
            "Talm",
            "Tam",
            "Tar",
            "Tas",
            "Tash",
            "Tav",
            "Tax",
            "Tat",
            "Tap",
            "Tep",
            "Tha",
            "Than",
            "Than Dok",
            "Thry",
            "Trel",
            "Treep",
            "Ter Threp",
            "Tol",
            "Ur",
            "Uran",
            "Um",
            "Vab",
            "Vad",
            "Vak",
            "Vak",
            "Vam",
            "Vad",
            "Ven",
            "Ves",
            "Ver",
            "Vis",
            "Viv",
            "Vul",
            "Vop",
            "War",
            "Won",
            "Wo",
            "Won",
            "What",
            "Whim",
            "Wim",
            "Win",
            "War",
            "Wad",
            "Wan",
            "Wun",
            "X'",
            "Xe'",
            "Xen",
            "Xio",
            "Xy",
            "Zing",
            "Zed",
            "Zer",
            "Zem",
            "Zeng"
        ]
        part2 = [
            "-o",
            "acalla",
            "addon",
            "adon",
            "acan",
            "aroid",
            "anbula",
            "angolia",
            "angalia",
            "ankor",
            "aldi",
            "aka",
            "aleko",
            "alis",
            "alla",
            "alos",
            "an",
            "andia",
            "anella",
            "ania",
            "amis",
            "arnia",
            "aran",
            "ara",
            "arth",
            "arius",
            "atoid",
            "avera",
            "budram",
            "budria",
            "burto",
            "borto",
            "bongo",
            "can",
            "cania",
            "cania",
            "caris",
            "cury",
            "chil",
            "chin",
            "chia",
            "chania",
            "con",
            "da",
            "dai",
            "dania",
            "daleko",
            "dalekon",
            "doria",
            "donia",
            "dikar",
            "eko",
            "ella",
            "elos",
            "elius",
            "elerth",
            "elialia",
            "eria",
            "era",
            "enia",
            "enella",
            "erebus",
            "es",
            "esh",
            "eaux",
            "ebus",
            "eus",
            "eran",
            "fall",
            "far",
            "finer",
            "gania",
            "gatis",
            "gill",
            "golia",
            "ian",
            "ion",
            "illian",
            "illa",
            "idian",
            "inax",
            "iman",
            "itas",
            "ius",
            "iza",
            "iru",
            "ix",
            "kail",
            "kien",
            "las",
            "lax",
            "lak",
            "ler",
            "land",
            "lejos",
            "lok",
            "los",
            "lox",
            "lon",
            "miniar",
            "nar",
            "nia",
            "nicus",
            "nor",
            "nt",
            "ntos",
            "oda",
            "oid",
            "oin",
            "ol",
            "omi",
            "on",
            "onine",
            "ong",
            "ongolia",
            "onia",
            "ornia",
            "ornania",
            "opa",
            "opia",
            "opia",
            "olok",
            "os",
            "oros",
            "orox",
            "orkon",
            "ovin",
            "ox",
            "pidor",
            "pid",
            "pod",
            "rax",
            "reus",
            "rock",
            "roid",
            "rog",
            "ryn",
            "sea",
            "shaa",
            "tan",
            "tara",
            "taria",
            "ton",
            "tes",
            "tep",
            "thra",
            "tania",
            "to",
            "tos",
            "tose",
            "tonia",
            "tronia",
            "topia",
            "tos",
            "trock",
            "tropic",
            "tus",
            "udros",
            "ule",
            "um",
            "umi",
            "uram",
            "urn",
            "urrinia",
            "ury",
            "urdan",
            "uria",
            "uridan",
            "uridian",
            "us",
            "utlis",
            "va",
            "vana",
            "vas",
            "vav",
            "vin",
            "vis",
            "viz",
            "za",
            "'am",
            "'an",
            "'us",
            "al"
        ]
        return f"{random.choice(part1)}{random.choice(part2)}"

    def generate_planet_name():
        prefix = [
            "Alpha",
            "Alpha Omega",
            "Beta",
            "Gamma",
            "Ceti",
            "Delta",
            "Epsilon",
            "Theta",
            "Zeta",
            "Omega",
            "Tau",
            "Tau Ceti",
            "The planet of",
            "The moon of",
            "The ringed planet of",
            "The robot world of",
            "The mountainous planet of",
            "The mist planet of",
            "The lava world of",
            "The ghost world of",
            "The desert planet of",
            "The ancient planet of",
            "The rock of",
            "New",
            "White",
            "East",
            "West",
            "North",
            "Old",
            "Las",
            "Los",
            "La"
        ]
        suffix = [
            "Alpha",
            "Beta",
            "Gamma",
            "Kappa",
            "Sigma",
            "Prime",
            "Major",
            "Minor",
            "One",
            "Two",
            "Epsilon",
            "Zeta",
            "Quintus",
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12",
            "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIV", "XV", "XVI",
            "World", "Moon", "gas giant",
            "e1", "e2", "e3", "e4"
        ]
        posession = [
            "Haven",
            "Hope",
            "World",
            "Forge",
            "Paradise",
            "Fall",
            "Reach",
            "Stronghold",
            "Beacon",
            "Outpost",
            "Sanctum",
            "Refuge",
            "Retreat",
            "Terminus",
            "Moon",
            "World",
            "Planetoid"
        ]
        planetname = planet_name()

        prefix_chance = random.randint(0, 100)
        suffix_chance = random.randint(0, 100)

        random_prefix = random.choice(prefix)
        random_suffix = random.choice(suffix)
        second_word_chance = random.choice(suffix)

        if prefix_chance <= 20:
            planetname = f"{random_prefix} {planetname}"

        if second_word_chance in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]:
            planetname = f"{planetname} {planet_name()}"

        if suffix_chance <= 25:
            planetname = f"{planetname} {random_suffix}"
        elif suffix_chance <= 45:
            planetname = f"{planetname} {random.randint(0, 400)}"
        elif suffix_chance <= 50:
            planetname = f"{planetname}'s {random.choice(posession)}"

        return planetname

    def generate_system():
        def gen_system_prefix():
            prefixes = [
                "Alpha",
                "Beta",
                "Gamma",
                "Ceti",
                "Picon",
                "Delta",
                "Epsilon",
                "Theta",
                "Zeta",
                "Omega",
                "Tau",
                "Nebulon",
                "Las",
                "Los",
                "La",
                "Far",
                "Deep",
                "Ultra",
                "Mega",
                "Super",
                "Über",
                "Omicron",
                "Sigma",
                "Kappa",
                "Rho",
                "Minor",
                "Major",
                "Greater"
                ]
            return random.choice(prefixes)  

        def gen_system_name():
            systems = [
                "Arf",
                "Alf",
                "Aeron",
                "Andromeda",
                "Apius",
                "Aquarius",
                "Ara",
                "Alpha Andromeda",
                "Alpha Centauri",
                "Alpha Persei",
                "Alcor",
                "Algol",
                "Antares",
                "Basri",
                "Behram",
                "Beta Picoris",
                "Boötes",
                "Cancri",
                "Canes Venatici",
                "Canis",
                "Capricorn",
                "Cassiopeia",
                "Castor",
                "Cebus",
                "Centaurus",
                "Ceti",
                "Cetus",
                "Columbus",
                "Coma Berenices",
                "Copurnicus",
                "Corona Borealis",
                "Corot",
                "Cygnus",
                "Cygni",
                "Dorado",
                "Draco",
                "Eridanus",
                "Eridanus",
                "Fikes",
                "Fornax",
                "Fomalhaut",
                "Gilese",
                "Goddard",
                "HD",
                "Hat",
                "Hercules",
                "Herculis",
                "Horologium",
                "Holbrook",
                "Hydra",
                "Hydrus",
                "Leo",
                "Leonis",
                "Libra",
                "Librae",
                "Lupus",
                "Luyten",
                "Lyra",
                "Mensa",
                "Mensae",
                "Monocerus",
                "Orion",
                "Pavo",
                "Pi Mensae",
                "Piccard",
                "Pictor",
                "Pisces",
                "Puppis",
                "Raleigh",
                "Reticulum",
                "Regulus",
                "Rho Corona Borealis",
                "Rosa",
                "Rouse",
                "Sagittarius",
                "Scorpius",
                "Serpens",
                "Sextan",
                "Spica",
                "Tau Geminorum",
                "Trappist",
                "Triangulum Australe",
                "Tucana",
                "Tyson",
                "Upsilon Andromedae",
                "Ursa Major",
                "Ursa Minor",
                "Ursae Majoris",
                "Vela",
                "Virgo",
                "Wasp",
                "Kepler",
                "Procyon",
                "Procyon",
                "Vorach",
                "Vorash",
                "Tobin",
                "Adara",
                "Doranda",
                "Copernicus",
                "Newton",
                "Ptolemy",
                "Hubble",
                "Herschel",
                "Sagan",
                "Einstein",
                "Messier",
                "Huygens",
                "Cannon",
                "Samos",
                "Laplace",
                "Burnell",
                "Bell",
                "Leavitt",
                "Penzias",
                "Payne",
                "Hawking",
                "Moore",
                "Rees",
                "Halley",
                "Burbidge",
                "Flamsteed",
                "Couper",
                "Marsden",
                "Gill",
                "Chandra",
                "Chan",
                "Chung",
                "Wickramasinghe",
                "Narlikar",
                "Brahmagupta",
                "Gupta",
                "Somayaji",
                "Bappu",
                "Ball",
                "Saha",
                "Das Gupta",
                "Lalla",
                "Jani",
                "Natarajan",
                "Subramaniam",
                "Fairall",
                "Knox",
                "Paraskevopoulos",
                "Weiss",
                "Wilkins",
                "Llewelyn",
                "Gomez",
                "Evans",
                "Myanmar",
                "Dilhan",
                "Eryurt"
            ]
            return random.choice(systems)

        def gen_system_suffix():
            suffixes = [
                "Expanse",
                "Expanse",
                "Expanse",
                "Nebula",
                "Nebula",
                "Stellar Nursery",
                "Passage",
                "Pass",
                "Phenomenon",
                "Space",
                "Sector",
                "Sector",
                "Sector",
                "Zone",
                "Zone",
                "Region",
                "Region",
                "Quadrant",
                "Quadrant",
                "Territory",
                "Belt",
                "Field",
                "Section",
                "Vicinity",
                "Proximity",
                "Cluster",
                "Cluster",
                "Spiral",
                "Halo Zone",
                "Coronal Stream",
                "Pulsar System",
                "Cloud Node",
                "Supercluster",
                "Vortex",
                "Star System",
                "Cluster System",
            ]
            return random.choice(suffixes)

        system_name = ""
        s_type = random.randint(0, 100)
        s_suffix_type = random.randint(0, 100)
        s_the_chance = random.randint(0, 100)

        if s_type <= 35:
            system_name = planet_name()
        elif s_type <= 65:
            system_name = f"{gen_system_prefix()} {planet_name()}" 
        elif s_type <= 85:
            system_name = f"{planet_name()} {planet_name()}"
        else:
            system_name = gen_system_name()

        if s_suffix_type <= 80:
            system_name += f" {gen_system_suffix()}"
        else:
            system_name += f" System"

        if s_the_chance <= 75:
            system_name = f"The {system_name}"
        return system_name

    def draw_ring(cr, x, y, rad_min, rad_max, r, g, b, a=1.0, gradient=False):
        if GRADIENTS and gradient:
            pattern = cairo.RadialGradient(x, y, rad_min, x, y, rad_max)
            pattern.add_color_stop_rgba(0, r - 0.3, g - 0.3, b - 0.3, a - 0.3)
            pattern.add_color_stop_rgba(1, r, g, b, a)
            cr.set_source(pattern)
        else:
            cr.set_source_rgba(r, g, b, a)
        cr.arc(x, y, rad_max, 0, 2 * math.pi)
        cr.close_path()
        cr.arc(x, y, rad_min, 0, 2 * math.pi)
        cr.close_path()
        cr.set_fill_rule(cairo.FILL_RULE_EVEN_ODD)
        cr.fill()
        cr.set_fill_rule(cairo.FILL_RULE_WINDING)

    def draw_orbit(cr, line, x, y, radius, r, g, b, a=1.0):
        cr.set_source_rgba(r, g, b, a)
        cr.set_line_width(line)
        cr.arc(x, y, radius, 0, 2 * math.pi)
        cr.stroke()

    def draw_circle_fill(cr, x, y, radius, r, g, b, a=1.0, gradient=False):
        if GRADIENTS and gradient:
            orbit_angle = random.randint(0, 20)
            pattern = cairo.LinearGradient(x + orbit_angle, y + radius, x -orbit_angle, y - radius)
            n_colors = random.randint(2, 4)
            for i in range(n_colors):
                rand_color = random.choice(list_of_colors)
                r, g, b = rand_color[0] / 255.0, rand_color[1] / 255.0, rand_color[2] / 255.0
                pattern.add_color_stop_rgb(i, r, g, b)
            cr.set_source(pattern)
        else:
            cr.set_source_rgba(r, g, b, a)

        cr.arc(x, y, radius, 0, 2 * math.pi)
        cr.fill()

    def draw_planet(cr, x, y, radius, r, g, b, a=1.0, gradient=False, texture_file=None):

        if GRADIENTS and gradient:
            orbit_angle = random.randint(0, 20)
            pattern = cairo.LinearGradient(x + orbit_angle, y + radius, x -orbit_angle, y - radius)
            n_colors = random.randint(2, 4)
            for i in range(n_colors):
                rand_color = random.choice(list_of_colors)
                r, g, b = rand_color[0] / 255.0, rand_color[1] / 255.0, rand_color[2] / 255.0
                pattern.add_color_stop_rgb(i, r, g, b)
            cr.set_source(pattern)
        else:
            cr.set_source_rgba(r, g, b, a)

        cr.arc(x, y, radius, 0, 2 * math.pi)
        cr.fill()

        if TEXTURES and random.randint(1, 100) < 40:
            
            texture_file = random.choice(list_of_planet_textures)

        if texture_file:
            # Load the texture
            texture = cairo.ImageSurface.create_from_png(f'textures/{texture_file}.png')

            # Set the composition operator to multiply
            cr.set_operator(cairo.Operator.MULTIPLY)
            
            # Create a pattern from the texture
            texture_pattern = cairo.SurfacePattern(texture)

            texture_pattern.set_extend(cairo.EXTEND_REPEAT)
            texture_pattern.set_filter(cairo.FILTER_NEAREST)

            # Matrix transformation: random rotation angle
            angle = math.radians(random.randint(1, 360))
            rotation_matrix = cairo.Matrix(math.cos(angle),math.sin(angle),-math.sin(angle),math.cos(angle),x-math.cos(angle)*x+math.sin(angle)*y,y-math.sin(angle)*x-math.cos(angle)*y)

            # Matrix transformation: scaling the texture to the planet
            texture_width, texture_height = 400, 400
            scale_factor = max(texture_width, texture_height) / (radius*2)
            scale_matrix = cairo.Matrix(scale_factor, 0, 0, scale_factor, 0, 0)

            # Matrix transformation: aligning the texture to the planet
            move_matrix = cairo.Matrix(1, 0, 0, 1, -x-radius, -y-radius)

            # Matrix transformation: combining all the transformations
            move_scale_matrix = rotation_matrix * move_matrix * scale_matrix
            texture_pattern.set_matrix(move_scale_matrix)


            # Apply the texture to the circle
            cr.set_source(texture_pattern)
            cr.arc(x, y, radius, 0, 2 * math.pi)
            cr.fill()

            # Set the composition operator back to default
            cr.set_operator(cairo.Operator.OVER)

            # Set the opacity of the texture
            cr.set_source_rgba(1, 1, 1, 0) # Set the color with alpha value (RGBA)
            cr.paint_with_alpha(0) # Set the opacity of the texture

    def draw_border(cr, size, r, g, b, width, height):
        cr.set_source_rgb(r, g, b)
        cr.rectangle(0, 0, size, height)
        cr.rectangle(0, 0, width, size)
        cr.rectangle(0, height - size, width, size)
        cr.rectangle(width - size, 0, size, height)
        cr.fill()

    def draw_background(cr, r, g, b, width, height):
        cr.set_source_rgb(r, g, b)
        cr.rectangle(0, 0, width, height)
        cr.fill()

    def random_bg_color(min, max):
        return round(random.uniform(min, max), 2)

    def get_random_points_on_circle(xc, yc, r, n=100):
        points_list = []
        for _ in range(0, n):
            angle = math.tau * random.random()
            p = (int(xc + r * math.cos(angle)), int(yc + r * math.sin(angle)))
            points_list.append(p) 
        return points_list

    def get_uniform_points_on_circle(xc, yc, r, n=360):
        return [
            (
                int(xc + (math.cos(2 * math.pi / n * x) * r)),  # x
                int(yc + (math.sin(2 * math.pi / n * x) * r)),  # y
            )
            for x in range(0, n + 1)
        ]

    def get_random_gaps_segments(total_space, n_segs):
        """
        seleziona n_segs-1 punti casuali, con una distanza minima tra loro pari a un quarto del segmento medio
        crea i gap in quei punti di larghezza random ma piccola (min 1px, max 20% del segmento medio)
        """

        segments = []
        min_distance_between_gaps = math.ceil((total_space / n_segs) / 4)
        gaps = [min_distance_between_gaps * i + x for i, x in enumerate(sorted(random.sample(range(5, total_space - 10), k=n_segs - 1)))]
        gaps.sort()

        seg_start = 0

        for gap in gaps:
            gap_size = random.randint(1, math.ceil((total_space / n_segs) * 0.2))  # gap between segments, 1px - 20% of average segment 
            half_gap_1 = round(gap_size / 2)
            half_gap_2 = gap_size - half_gap_1
            gap_start = gap - half_gap_1
            gap_end = gap + half_gap_2
            segments.append(gap_start - seg_start)
            segments.append(gap_size)
            seg_start = gap_end

        segments.append(total_space - seg_start)  # aggiunge l'ultimo segmento
        return segments

    def draw_black_hole2(cr, x, y, radius, r, b, g, a=1.0, gradient=True):
        hole_radius = radius * 0.8
        sfumatura_min = radius * 0.8
        sfumatura_max = radius * 1

        cr.set_source_rgba(0, 0, 0)
        cr.arc(x, y, hole_radius, 0, 2 * math.pi)
        cr.fill()

        if GRADIENTS and gradient:
            pattern = cairo.RadialGradient(x, y, sfumatura_min, x, y, sfumatura_max)
            pattern.add_color_stop_rgba(0, r, g, b, a)
            # pattern.add_color_stop_rgba(1, bgr, bgb, bgg, bga)
            pattern.add_color_stop_rgba(1, r, g, b, 0)
            cr.set_source(pattern)
        else:
            cr.set_source_rgba(r, g, b, a)

        cr.arc(x, y, sfumatura_min, 0, 2 * math.pi)
        cr.close_path()
        cr.arc(x, y, sfumatura_max, 0, 2 * math.pi)
        cr.close_path()
        cr.set_fill_rule(cairo.FILL_RULE_EVEN_ODD)
        cr.fill()
        cr.set_fill_rule(cairo.FILL_RULE_WINDING)

    def draw_sun(cr, x, y, radius, r, b, g, a=1.0, gradient=True):
        hole_radius = radius * 0.6
        sfumatura_min = radius * 0.55
        sfumatura_max = radius * 1


        cr.set_source_rgba(r, g, b, a)

        cr.arc(x, y, hole_radius, 0, 2 * math.pi)
        cr.fill()

        if GRADIENTS and gradient:
            pattern_halo = cairo.RadialGradient(x, y, sfumatura_min, x, y, sfumatura_max)
            pattern_halo.add_color_stop_rgba(0, r, g, b, a)
            # pattern.add_color_stop_rgba(1, bgr, bgb, bgg, bga)
            pattern_halo.add_color_stop_rgba(0.3, r, g, b, 0.5)
            pattern_halo.add_color_stop_rgba(1, r, g, b, 0)
            cr.set_source(pattern_halo)
        else:
            cr.set_source_rgba(r, g, b, a)

        cr.arc(x, y, sfumatura_min, 0, 2 * math.pi)
        cr.close_path()
        cr.arc(x, y, sfumatura_max, 0, 2 * math.pi)
        cr.close_path()
        cr.set_fill_rule(cairo.FILL_RULE_EVEN_ODD)
        cr.fill()
        cr.set_fill_rule(cairo.FILL_RULE_WINDING)

    def draw_star(cr, x, y, size, r, b, g, a=1.0):
        p1 = (x + size, y)
        p2 = (x, y - size)
        p3 = (x - size, y)
        p4 = (x, y + size)
        cr.set_source_rgba(r, g, b, a)
        cr.move_to(p1[0], p1[1])
        cr.curve_to(x, y, x, y, p2[0], p2[1])
        cr.curve_to(x, y, x, y, p3[0], p3[1])
        cr.curve_to(x, y, x, y, p4[0], p4[1])
        cr.curve_to(x, y, x, y, p1[0], p1[1])
        cr.fill()
        # cr.new_sub_path() 
        # cr.arc(p1[0], p1[1], size, 0, math.pi / 2)
        # cr.new_sub_path() 
        # cr.arc(p2[0], p2[1], size, math.pi / 2, math.pi)
        # cr.new_sub_path()
        # cr.arc(p3[0], p3[1], size, math.pi, math.pi * 3 / 2)
        # cr.new_sub_path()
        # cr.arc(p4[0], p4[1], size, math.pi * 3 / 2, 0)
        cr.fill()
        return

    def asteroid_density(r, r_min, r_max, max_density):
        """
        Calculates the density of asteroids at a given distance r from the center of an asteroid belt.

        Args:
            r (float): distance from the center of the asteroid belt
            r_min (float): minimum radius of the asteroid belt
            r_max (float): maximum radius of the asteroid belt
            max_density (float): maximum density at the center of the belt

        Returns:
            float: density of asteroids at distance r
        """
        if r < r_min or r > r_max:
            return 1.0
        else:
            midpoint = (r_max - r_min) / 2.0 + r_min
            inner_range = 0.6 * (r_max - r_min) / 2.0
            if r <= midpoint - inner_range or r >= midpoint + inner_range:
                # Calculate the density at the edges of the belt using a modified
                # formula that gradually decreases the density from max_density to 1.0
                # as we move away from the center of the belt towards the edges.
                width = r_max - r_min
                density_range = max_density - 1.0
                peak_location = midpoint
                density = 1.0 + density_range * (math.exp(-((r - peak_location) ** 2) / (2 * ((width / 4) ** 2))))
                density = min(density, max_density)
                density = max(density, 1.0)
            else:
                # The density is constant within the inner 70% of the belt.
                density = max_density
            return density


    def write_planet_name(cr, x, y, radius, name, type="planet"):
        if type == "planet":
            x1 = x + radius + 20
            y1 = y - 10
        elif type == "moon":
            x1 = x + radius + 35
            y1 = y - 10
        elif type == "rings":
            x1 = x + radius + 20
            y1 = y - 10
        elif type == "belt":
            x1 = x
            y1 = y - radius - 10
        cr.close_path()
        cr.set_font_size(30)
        cr.select_font_face("GeosansLight-NMS", cairo.FONT_SLANT_OBLIQUE, cairo.FONT_WEIGHT_BOLD)
        cr.set_source_rgba(1, 1, 1, 0.8)
        cr.move_to(x1, y1)
        cr.show_text(name.upper())
        cr.move_to(x, y)
        cr.set_source_rgba(0, 0, 0, 0.0)
        return

    WIDTH = 1080
    HEIGHT = 1920

    ORBIT = True
    LINE = True

    RINGS = True
    MOONS = True
    BELTS = True
    STARFIELD = True
    BINARY = True
    BLACKHOLES = True
    SKIPS = True

    GRADIENTS = True
    TEXTURES = True

    STARS = 500
    BORDERSIZE = 50
    NOISE = 3

    seed = uuid.uuid4()
    # seed = 'test'


    class ArgumentParser(argparse.ArgumentParser):
        """
        The default (and only) argparse behavior is to throw error to sys.stderr via the error method.
        """

        def error(self, message):
            raise ParserError(message)

    class ParserError(Exception): pass

    parser = argparse.ArgumentParser()
    parser.add_argument("--width", help="larghezza in pixel", nargs='?', default=WIDTH)
    parser.add_argument("--height", help="altezza in pixel",nargs='?', default=HEIGHT)
    parser.add_argument("--seed", help="specifica un seed", default=seed)
    parser.add_argument("--tinyborder", help="bordo sottile", action="store_true")
    parser.add_argument("--noborder", help="non generare il bordo", action="store_true")
    parser.add_argument("--nostars", help="non generare le stelline sullo sfondo", action="store_true")
    parser.add_argument("--origin", help="disattiva tutte le feature random", action="store_true")

    args, unknown = parser.parse_known_args()

    WIDTH = int(args.width)
    HEIGHT = int(args.height)

    tinyborder = args.tinyborder
    noborder = args.noborder
    nostars = args.nostars
    origin = args.origin
    seed = args.seed

    if args:
        if nostars:
            STARFIELD = False

        if origin:
            STARFIELD = False
            BELTS = False
            MOONS = False
            RINGS = False
            BINARY = False
            BLACKHOLES = False
            SKIPS = True

        if noborder:
            BORDERSIZE = 0

        if tinyborder:
            BORDERSIZE = 5

        if WIDTH > 5000:
            WIDTH = 5000

        if HEIGHT > 5000:
            HEIGHT = 5000


    random.seed(str(seed))

    print(f"Seed: {str(seed)}")


    SUNSIZE = random.randint(50, 400)

    width, height = WIDTH, HEIGHT
    border_size = BORDERSIZE
    sun_size = SUNSIZE
    system_name = generate_system()
    planets_list = f"<b>· {system_name.upper()} ·</b>\n<i>{random.randint(15, 10000)} UA</i>\n\n"


    ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    cr = cairo.Context(ims)

    # Sfondo
    bg_min = 0.05
    bg_max = 0.2
    bg_color = (random_bg_color(bg_min, bg_max), random_bg_color(bg_min, bg_max), random_bg_color(bg_min, bg_max),)

    draw_background(cr, *bg_color, width, height)

    # Starfield
    if STARFIELD:
        for _ in range(STARS):
            star_size = random.randint(1, 30)
            star_x = random.randint(0, 6000)
            star_y = random.randint(0, 6000)
            if star_size < 10:
                draw_circle_fill(cr, star_x, star_y, star_size, 1, 1, 1, a=random.uniform(0.2, 0.4))
            else:
                draw_star(cr, star_x, star_y, star_size, 1, 1, 1, a=random.uniform(0.2, 0.4))

    # Stella
    sun_color = random.choice(list_of_sun_colors)
    sun_center = height - border_size
    sun_r, sun_g, sun_b = sun_color[0] / 255.0, sun_color[1] / 255.0, sun_color[2] / 255.0

    if random.randint(1, 100) < 30 and BLACKHOLES:
        draw_black_hole2(cr, width / 2, sun_center, sun_size, sun_r, sun_g, sun_b, a=1.0, gradient=True)
    else:
        if sun_size > 300 and random.randint(1, 100) > 10 and BINARY:  # binary
            BINARY_PADDING = 5
            sun_color_1 = random.choice(list_of_sun_colors)
            sun_color_2 = random.choice(list_of_sun_colors)
            sun_r_1, sun_g_1, sun_b_1 = sun_color_1[0] / 255.0, sun_color_1[1] / 255.0, sun_color_1[2] / 255.0
            sun_r_2, sun_g_2, sun_b_2 = sun_color_2[0] / 255.0, sun_color_2[1] / 255.0, sun_color_2[2] / 255.0
            ratio = random.uniform(0.1, 0.9)
            r1 = sun_size * ratio
            r2 = sun_size * (1 - ratio)
            # draw_circle_fill(cr, ((width / 2) - (sun_size - r1)), sun_center, int(r1 * 0.9), sun_r_1, sun_g_1, sun_b_1, a=1, gradient=True)
            draw_sun(cr, ((width / 2) - (sun_size - r1)), sun_center, int(r1 * 0.9), sun_r_1, sun_g_1, sun_b_1, a=1, gradient=True)
            # draw_circle_fill(cr, ((width / 2) + (sun_size - r2)), sun_center, int(r2 * 0.9), sun_r_2, sun_g_2, sun_b_2, a=1, gradient=True)
            draw_sun(cr, ((width / 2) + (sun_size - r2)), sun_center, int(r2 * 0.9), sun_r_2, sun_g_2, sun_b_2, a=1, gradient=True)
        else:
            # draw_circle_fill(cr, width / 2, sun_center, sun_size, sun_r, sun_g, sun_b, gradient=True)
            draw_sun(cr, width / 2, sun_center, sun_size, sun_r, sun_g, sun_b, gradient=True)

    distance_between_planets = 20
    last_center = sun_center
    last_size = sun_size
    last_color = sun_color

    min_size = 20
    max_size = 150


    for x in range(1, 20):
        distance_between_planets = random.randint(20, 100)
        next_size = random.randint(min_size, max_size)
        next_center = last_center - last_size - (next_size * 2) - distance_between_planets

        # Seleziono un colore random
        rand_color = random.choice(list_of_colors)
        while (rand_color is last_color):
            rand_color = random.choice(list_of_colors)
        r, g, b = rand_color[0] / 255.0, rand_color[1] / 255.0, rand_color[2] / 255.0

        if not(next_center - next_size < border_size):
            if random.randint(0, 100) <= 10 and SKIPS:  # SKIP!
                # if context.args:
                #     if "-star" in context.args:
                #         draw_star(cr, width / 2, next_center, next_size, 1, 1, 1)
                last_color = rand_color
                last_center = next_center
                last_size = next_size
                continue
            p_name = generate_planet_name()
            planets_list += f"— {p_name}\n"
            planet_size = next_size
            if random.randint(0, 100) <= 30 and planet_size >= 50 and BELTS:   # asteroid belt
                # draw_orbit(cr, next_size, width / 2, sun_center, height - next_center - border_size, r, g, b, a=0.05)  # sfondo
                belt_radius_min = int(height - next_center - border_size - (planet_size / 2))
                belt_radius_max = int(height - next_center - border_size + (planet_size / 2))
                # draw_orbit(cr, 2, width / 2, sun_center, belt_radius_min, r, g, b, a=1)  # bordi netti - inferiore
                # draw_orbit(cr, 2, width / 2, sun_center, belt_radius_max, r, g, b, a=1)  # bordi netti - superiore
                belt_points = []
                midpoint = (belt_radius_max - belt_radius_min) / 2.0 + belt_radius_min
                inner_range = 0.6 * (belt_radius_max - belt_radius_min) / 2.0
                for x in range(belt_radius_min, belt_radius_max + 1, 2):
                    # xC = (belt_radius_max + belt_radius_min) / 2
                    # r = (belt_radius_max - belt_radius_min) / 2
                    # density = int(math.sqrt(r**2 - (x - xC)**2))*5

                    max_density = 120
                    density = int(asteroid_density(x, belt_radius_min, belt_radius_max, max_density))
                    
                    asteroid_size_min = 2
                    asteroid_size_max = 3
                                        # if density > 1500:
                    #     density = 1500
                    belt_points = get_random_points_on_circle(width / 2, sun_center, x, n=density)
                    # print(f"x: {x} - Density: {density} - belt_points: {len(belt_points)}")

                    for point in belt_points:
                        asteroid_size = random.randint(asteroid_size_min, asteroid_size_max)
                        if x <= midpoint - inner_range or x >= midpoint + inner_range:  # bordi esterni
                            asteroid_size = asteroid_size / 2
                            draw_circle_fill(cr, point[0], point[1], asteroid_size, r, g, b, a=random.uniform(0.4, 0.8))
                        else:
                            draw_circle_fill(cr, point[0], point[1], asteroid_size, r, g, b, a=random.uniform(0.8, 1))
                

                    # asteroid_size = 1
                    # print(point[0], point[1])

                # write_planet_name(cr=cr, x=width / 2, y=next_center, radius=planet_radius, name=p_name, type="belt")


                last_color = rand_color
                last_center = next_center
                last_size = next_size
                BELTS = False
                continue

            # Planets Generation
            if ORBIT:
                draw_orbit(cr, random.randint(4, max(4, round(planet_size / 10))), width / 2, sun_center, height - next_center - border_size, r, g, b, a=random.uniform(0.5, 1))

            elif LINE:
                cr.move_to(border_size * 2, next_center)
                cr.line_to(width - (border_size * 2), next_center)
                cr.stroke()

            # Padding
            draw_circle_fill(cr, width / 2, next_center, next_size + 8, *bg_color)  # vuoto

            planet_type = random.choices(["rings", "moons", "normal"], weights=(25, 25, 50), k=1)[0]
            planet_radius = next_size

            if planet_type == "rings" and RINGS and planet_radius >= 50:
                planet_size = round(next_size * random.uniform(0.2, 0.5))  # il pianeta è il 20-50% della dimensione totale.
                draw_planet(cr, width / 2, next_center, planet_size, r, g, b, gradient=True)  # pianeta
                empty_space = round(next_size * random.uniform(0.05, 0.2))  # il buffer è il 5-20% della dimensione totale.
                space_remaining = next_size - planet_size - empty_space
                n_rings = random.randint(1, 4)
                rings_list = get_random_gaps_segments(space_remaining, n_rings)
                ring_start = planet_size + empty_space
                for i, ring_size in enumerate(rings_list):
                    if i % 2 == 0:  # è pari, segment
                        draw_ring(cr, x=width / 2, y=next_center, rad_min=ring_start, rad_max=ring_start + ring_size, r=r, g=g, b=b, a=random.uniform(0.1, 1), gradient=True)
                    else:   # gap
                        pass
                    ring_start += ring_size
                # write_planet_name(cr=cr, x=width / 2, y=next_center, radius=planet_radius, name=p_name, type="rings")

            elif planet_type == "moons" and MOONS and planet_radius >= 50:
                n_moons = random.randint(1, 3)

                moons = []
                for i in range(n_moons):
                    moon_radius = round(planet_radius * random.uniform(0.1, 0.3))  # la luna è il 10%-30% del pianeta
                    orbit_radius = planet_radius + moon_radius + (10 * (i + 1))  # orbita sempre più grande ogni luna
                    moon_pos = get_uniform_points_on_circle(width / 2, next_center, orbit_radius, n=5)[i + 3]  # seleziono n posizioni sull'orbita e piazzo le lune in ordine
                    mr, mg, mb = r + random.uniform(-0.1, 0.1), g + random.uniform(-0.1, 0.1), b + random.uniform(-0.1, 0.1)  # modifico un po' il colore
                    moons.append((moon_radius, orbit_radius, moon_pos, mr, mg, mb))

                for m in moons:
                    moon_radius, orbit_radius, moon_pos, mr, mg, mb = m
                    draw_orbit(cr, 2, width / 2, next_center, orbit_radius, r=mr, g=mg, b=mb)  # mi disegno l'orbita della luna

                for m in moons:
                    moon_radius, orbit_radius, moon_pos, mr, mg, mb = m
                    draw_circle_fill(cr=cr, x=moon_pos[0], y=moon_pos[1], radius=moon_radius, r=mr, g=mg, b=mb, gradient=True)  # disegno luna
                # write_planet_name(cr=cr, x=width / 2, y=next_center, radius=planet_radius, name=p_name, type="moon")

            else:
                draw_planet(cr=cr, x=width / 2, y=next_center, radius=planet_radius, r=r, g=g, b=b, gradient=True)
                # write_planet_name(cr=cr, x=width / 2, y=next_center, radius=planet_radius, name=p_name, type="planet")

            last_color = rand_color
            last_center = next_center
            last_size = next_size
            if planet_type == "moons" and MOONS and planet_radius >= 50:
                last_size = orbit_radius

    draw_border(cr, border_size, sun_r, sun_g, sun_b, width, height)
    image_path = f'Stars-{int(time.time())}-{seed}-{str(width)}x{str(height)}.png'
    ims.write_to_png(image_path)
    
    if BORDERSIZE >= 20:
        img = Image.open(image_path)
    
        font_size = BORDERSIZE - 10

        rgb_bgcolor = tuple(int(x) for x in bg_color)

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('fonts/geonms-font.ttf', font_size)

        anchor = (int(WIDTH / 2), int((HEIGHT - (BORDERSIZE / 2))))

        draw.text(anchor, system_name.upper(), font=font, anchor="mm", fill=rgb_bgcolor, stroke_width=0)
        
        img.save(image_path)

    if NOISE:
        # Load image
        img = np.array(Image.open(image_path))

        # Define mean and standard deviation
        mean = 0
        stddev = NOISE

        # Create grayscale Gaussian noise array and add it to image
        noise = np.random.normal(mean, stddev, img.shape[:2])
        noisy_img = np.zeros(img.shape, dtype=np.uint8)
        noisy_img[:,:,0] = np.clip(img[:,:,0] + noise, 0, 255)
        noisy_img[:,:,1] = np.clip(img[:,:,1] + noise, 0, 255)
        noisy_img[:,:,2] = np.clip(img[:,:,2] + noise, 0, 255)

        # Convert to grayscale
        noisy_img_gray = np.dot(noisy_img[...,:3], [0.2989, 0.5870, 0.1140])

        # Add opacity to the noisy image
        alpha = np.random.randint(0, 255, img.shape[:2]).astype(np.uint8)
        noisy_img_gray = np.stack((noisy_img_gray,)*3, axis=-1)
        noisy_img_gray = np.concatenate((noisy_img_gray, alpha[:,:,np.newaxis]), axis=2)

        # Save the noisy image
        noisy_img_pil = Image.fromarray(noisy_img)
        noisy_img_pil.save(image_path)


    print(f"Finito!\n{image_path}")
    # planets_list += f"\nSeed:\n<code>{seed}</code>"




if __name__ == '__main__':
    solarsystem()