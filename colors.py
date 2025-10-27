from enum import Enum

# Is there better? Maybe. Do I care? No. I only need to do this once.
class Horse(Enum):
    KING_HALO = ('King Halo', '#4CAF7D', '#6A89D9') # Outfit
    NICE_NATURE = ('Nice Nature', '#D62A2C', '#0F7F49') # Outfit
    MATIKANEFUKUKITARU = ('Matikanefukukitaru', '#EC9361', '#4D60D3')  # Hair, Collar
    HARU_URARA = ('Haru Urara', '#FFA9AD', '#E14C7C')  # Hair, Outfit
    SAKURA_BAKUSHIN_O = ('Sakura Bakushin O', '#FF78A7', '#FECA85')  # Outfit
    WINNING_TICKET = ('Winning Ticket', '#EF1D23', '#0CA4FF') # Outfit
    AGNES_TACHYON = ('Agnes Tachyon', '#EFDC9A', '#94150F')  # Outfit, Eyecolor
    MEJIRO_RYAN = ('Mejiro Ryan', '#63BBBD', '#EFDCC4')  # Outfit
    SUPER_CREEK = ('Super Creek', '#4175B9', '#DADAE1')  # Outfit
    MAYANO_TOP_GUN = ('Mayano Top Gun', '#F78A42', '#615637')  # Hair, Outfit
    AIR_GROOVE = ('Air Groove', '#414362', '#FDF48C') # Outfit
    EL_CONDOR_PASA = ('El Condor Pasa', '#D72A13', '#F4D755') # Outfit
    GRASS_WONDER = ('Grass Wonder', '#4D64AA', '#FDCE7F') # Outfit
    DAIWA_SCARLET = ('Daiwa Scarlet', '#2C2996', '#BE132C') # Outfit, Eye
    VODKA = ('Vodka', '#FFFF64', '#52C7C8') # Outfit
    GOLD_SHIP = ('Gold Ship', '#F83846', '#FFFBCA') # Outfit
    RICE_SHOWER = ('Rice Shower', '#5357A4', '#9F365B') # Outfit
    SYMBOLI_RUDOLF = ('Symboli Rudolf', '#387055', '#C63030') # Outfit
    MEJIRO_MCQUEEN = ('Mejiro McQueen', '#7A63D1', '#1E171D') # Hair, Outfit
    TAIKI_SHUTTLE = ('Taiki Shuttle', '#86CC48', '#E4A26C') # Hair, Outfit
    OGURI_CAP = ('Oguri Cap', '#DAD8DD', '#293D8D') # Hair, Outfit
    MARUZENSKY = ('Maruzensky', '#DC4B27', '#FFDD22') # Outfit
    TOKAI_TEIO = ('Tokai Teio', '#4268D3', '#EE68A6') # Outfit
    SILENCE_SUZUKA = ('Silence Suzuka', '#42B069', 'F8D07A') # Outfit
    SPECIAL_WEEK = ('Special Week', '#E978D3', '#77457A') # Outfit
    TM_OPERA_O = ('TM Opera O', '#FD6EB6', '#FEC772') # Crown
    MIHONO_BOURBON = ('Mihono Bourbon', '#FF5FFF', '#40FFFF') # Outfit
    BIWA_HAYAHIDE = ('Biwa Hayahide', '#5A3B5A', '#E5A5DA') # Outfit
    MEJIRO_MCQUEEN_ANIME = ('Mejiro McQueen (Anime Collab)', '#7A63D1', '#E2F4F6') # Outfit
    TOKAI_TEIO_ANIME = ('Tokai Teio (Anime Collab)', '#A61227', '#74E7EE') # Outfit
    CURREN_CHAN = ('Curren Chan', '#4D3B29', '#F10B0F') # Outfit
    NARITA_TAISHIN = ('Narita Taishin', '#FFA1BF', '#FFE894') # Outfit
    SMART_FALCON = ('Smart Falcon', '#FF73B5', '#FA2521') # Outfit
    NARITA_BRIAN = ('Narita Brian', '#CC669A', '#6D5C73') # Outfit, hair
    MAYANO_TOP_GUN_WEDDING = ('Mayano Top Gun (Wedding)', '#F78A42', '#FFF6EE') # Hair, Outfit
    AIR_GROOVE_WEDDING = ('Air Groove (Wedding)', '#E1A6FE', '#4650D5') # Flowers, Lace
    SEIUN_SKY = ('Seiun Sky', '#FFFEED', '#A5C894') # Outfit, Ears
    HISHI_AMAZON = ('Hishi Amazon', '#3344B7', '#EFB371') # Outfit, Skin
    EL_CONDOR_PASA_FANTASY = ('El Condor Pasa (Fantasy)', '#F58A29', '#FFDB4D') # Outfit
    GRASS_WONDER_FANTASY = ('Grass Wonder (Fantasy)', '#69B6A4', '#E7EABC') # Outfit
    FUJI_KISEKI = ('Fuji Kiseki', '#8FEEFF', '#5C5663') #Eye, Outfit
    GOLD_CITY = ('Gold City', '#8299D9', '#333340') # Ribbon, Outfit
    MARUZENSKY_SUMMER = ('Maruzensky (Summer)', '#E60708', '#92D458') # Flowers
    SPECIAL_WEEK_SUMMER = ('Special Week (Summer)', '#FFD5F9', '#FFBC6E') # Eye, Outfit
    MEISHO_DOTO = ('Meisho Doto', '#5A5EDE', '#C568AA') # Outfit, Eye

    def __init__(self, name, main_color, sub_color):
        self.name = name
        self.main_color = main_color
        self.sub_color = sub_color

# Arbitrary colors
class RunnerType(Enum):
    FRONT_RUNNER = ('Front Runner', '#324376')
    PACE_CHASER = ('Pace Chaser', '#F5DD90')
    LATE_SURGER = ('Late Surger', '#F68E5F')
    END_CLOSER = ('End Closer', '#F76C5E')

    def __init__(self, name, main_color):
        self.name = name
        self.main_color = main_color