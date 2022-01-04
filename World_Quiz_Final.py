"""
Marissa Flynn and Michael Piscione
CS021
World_Quiz.py Final Project-- This program tests users on their knowledge of capitals and official languages of sovereign states globally. 
"""
import random

# Define Constants
NUMBER_OF_QUESTIONS = 4
SECRET_DEVELOPER_OPTION_SHOW_ANSWERS = False

SOVEREIGN_STATES = {"abkhazia": [{"languages": ["abkhaz", "russian"]}, {"capitals": ["sokhumi"]}],
                    "afghanistan": [{"languages": ["pashto", "dari"]}, {"capitals": ["Kabul"]}],
                    "albania": [{"languages": ["albanian"]}, {"capitals": ["tirana"]}],
                    "algeria": [{"languages": ["arabic", "tamazight"]}, {"capitals": ["algiers"]}],
                    "andorra": [{"languages": ["catalan"]}, {"capitals": ["andorra la vella"]}],
                    "angola": [{"languages": ["portuguese"]}, {"capitals": ["luanda"]}],
                    "antigua and barbuda": [{"languages": ["english"]}, {"capitals": ["saint john's"]}],
                    "argentina": [{"languages": ["spanish"]}, {"capitals": ["buenos aires"]}],
                    "armenia": [{"languages": ["armenian"]}, {"capitals": ["yerevan"]}],
                    "australia": [{"languages": ["english"]}, {"capitals": ["canberra"]}],
                    "austria": [{"languages": ["german"]}, {"capitals": ["vienna"]}],
                    "azerbaijan": [{"languages": ["azerbaijani"]}, {"capitals": ["baku"]}],
                    "the bahamas": [{"languages": ["english"]}, {"capitals": ["nassau"]}],
                    "bahrain": [{"languages": ["arabic"]}, {"capitals": ["manama"]}],
                    "bangladesh": [{"languages": ["bengali"]}, {"capitals": ["dhaka"]}],
                    "barbados": [{"languages": ["english"]}, {"capitals": ["bridgetown"]}],
                    "belarus": [{"languages": ["belarusian", "russian"]}, {"capitals": ["minsk"]}],
                    "belgium": [{"languages": ["dutch", "french", "german"]}, {"capitals": ["brussels"]}],
                    "belize": [{"languages": ["english"]}, {"capitals": ["belmopan"]}],
                    "benin": [{"languages": ["french"]}, {"capitals": ["porto-novo"]}],
                    "bhutan": [{"languages": ["dzongkha"]}, {"capitals": ["thimphu"]}],
                    "bolivia": [{"languages": ["castilian", "aymara", "araona", "baure", "besiro", "canichana", "cavineno", "cayubaba", "chácobo", "chimán", "ese ejja", "guarani", "guarasu'we", "guarayu", "itonama", "leco", "machajuyai-Kallawaya", "machineri", "maropa", "mojeno-ignaciano", "mojeno-trinitario", "more", "moseten", "movima", "pacawara", "puquina", "quechua", "sirionó", "tacana", "tapiete", "toromona", "uru-chipaya", "weenhayek", "yaminawa", "yuki", "yuracare", "zamuco"]}, {"capitals": ["la paz"]}],
                    "bosnia and herzegovina": [{"languages": ["bosnian", "croatian", "serbian"]}, {"capitals": ["sarajevo"]}],
                    "botswana": [{"languages": ["english", "tswana"]}, {"capitals": ["gaborone"]}],
                    "brazil": [{"languages": ["portuguese"]}, {"capitals": ["brasilia"]}],
                    "brunei": [{"languages": ["malay", "english"]}, {"capitals": ["bandar seri begawan"]}],
                    "bulgaria": [{"languages": ["bulgarian"]}, {"capitals": ["sofia"]}],
                    "burkina faso": [{"languages": ["french"]}, {"capitals": ["ouagadougou"]}],
                    "burundi": [{"languages": ["french", "Kirundi", "english"]}, {"capitals": ["gitega"]}],
                    "cambodia": [{"languages": ["Khmer"]}, {"capitals": ["phnom penh"]}],
                    "cameroon": [{"languages": ["english", "french"]}, {"capitals": ["yaounde"]}],
                    "canada": [{"languages": ["english", "french"]}, {"capitals": ["ottawa"]}],
                    "cape verde": [{"languages": ["portuguese"]}, {"capitals": ["praia"]}],
                    "central african republic": [{"languages": ["french"]}, {"capitals": ["bangui"]}],
                    "chad": [{"languages": ["arabic", "french"]}, {"capitals": ["n'djamena"]}],
                    "chile": [{"languages": ["spanish"]}, {"capitals": ["santiago"]}],
                    "china": [{"languages": ["mandarin"]}, {"capitals": ["beijing"]}],
                    "colombia": [{"languages": ["spanish"]}, {"capitals": ["bogotá"]}],
                    "comoros": [{"languages": ["arabic", "comorian", "french"]}, {"capitals": ["moroni"]}],
                    "democratic republic of the congo": [{"languages": ["french"]}, {"capitals": ["Kinshasa"]}],
                    "republic of the congo": [{"languages": ["french"]}, {"capitals": ["brazzaville"]}],
                    "cook islands": [{"languages": ["english", "cook islands maori"]}, {"capitals": ["avarua"]}],
                    "costa rica": [{"languages": ["spanish"]}, {"capitals": ["san jose"]}],
                    "cote d'ivoire": [{"languages": ["french"]}, {"capitals": ["yamoussoukro"]}],
                    "croatia": [{"languages": ["croatian"]}, {"capitals": ["zagreb"]}],
                    "cuba": [{"languages": ["spanish"]}, {"capitals": ["havana"]}],
                    "cyprus": [{"languages": ["greek", "turkish"]}, {"capitals": ["nicosia"]}],
                    "czech republic": [{"languages": ["czech", "slovak"]}, {"capitals": ["prague"]}],
                    "denmark": [{"languages": ["danish"]}, {"capitals": ["copenhagen"]}],
                    "djibouti": [{"languages": ["arabic", "french"]}, {"capitals": ["djibouti"]}],
                    "dominica": [{"languages": ["english"]}, {"capitals": ["roseau"]}],
                    "dominican republic": [{"languages": ["spanish"]}, {"capitals": ["santo domingo"]}],
                    "east timor": [{"languages": ["portuguese", "tetum"]}, {"capitals": ["dili"]}],
                    "ecuador": [{"languages": ["spanish", "quechua"]}, {"capitals": ["quito"]}],
                    "egypt": [{"languages": ["arabic"]}, {"capitals": ["cairo"]}],
                    "el salvador": [{"languages": ["spanish"]}, {"capitals": ["san salvador"]}],
                    "equatorial guinea": [{"languages": ["french", "portuguese", "spanish"]}, {"capitals": ["malabo"]}],
                    "eritrea": [{"languages": ["tigrinya"]}, {"capitals": ["asmara"]}],
                    "estonia": [{"languages": ["estonian"]}, {"capitals": ["tallinn"]}],
                    "eswatini": [{"languages": ["english", "swazi"]}, {"capitals": ["mbabane"]}],
                    "ethiopia": [{"languages": ["amharic"]}, {"capitals": ["addis ababa"]}],
                    "fiji": [{"languages": ["english", "fijian", "fiji hindi"]}, {"capitals": ["suva"]}],
                    "finland": [{"languages": ["finnish", "swedish"]}, {"capitals": ["helsinki"]}],
                    "france": [{"languages": ["french"]}, {"capitals": ["paris"]}],
                    "gabon": [{"languages": ["french"]}, {"capitals": ["libreville"]}],
                    "the gambia": [{"languages": ["english"]}, {"capitals": ["banjul"]}],
                    "georgia": [{"languages": ["georgian"]}, {"capitals": ["tbilisi"]}],
                    "germany": [{"languages": ["german"]}, {"capitals": ["berlin"]}],
                    "ghana": [{"languages": ["english"]}, {"capitals": ["accra"]}],
                    "greece": [{"languages": ["greek"]}, {"capitals": ["athens"]}],
                    "grenada": [{"languages": ["english"]}, {"capitals": ["st. george's"]}],
                    "guatemala": [{"languages": ["spanish"]}, {"capitals": ["guatemala city"]}],
                    "guinea": [{"languages": ["french"]}, {"capitals": ["conakry"]}],
                    "guinea-bissau": [{"languages": ["portuguese"]}, {"capitals": ["bissau"]}],
                    "guyana": [{"languages": ["english"]}, {"capitals": ["georgetown"]}],
                    "haiti": [{"languages": ["french", "haitian creole"]}, {"capitals": ["port-au-prince"]}],
                    "honduras": [{"languages": ["spanish"]}, {"capitals": ["tegucigalpa"]}],
                    "hungary": [{"languages": ["hungarian"]}, {"capitals": ["budapest"]}],
                    "iceland": [{"languages": ["icelandic", "icelandic sign languages"]}, {"capitals": ["reykjavik"]}],
                    "india": [{"languages": ["hindi", "english"]}, {"capitals": ["new delhi"]}],
                    "indonesia": [{"languages": ["indonesian"]}, {"capitals": ["jakarta"]}],
                    "iran": [{"languages": ["persian"]}, {"capitals": ["tehran"]}],
                    "iraq": [{"languages": ["arabic"]}, {"capitals": ["baghdad"]}],
                    "ireland": [{"languages": ["english", "irish"]}, {"capitals": ["dublin"]}],
                    "israel": [{"languages": ["hebrew"]}, {"capitals": ["jerusalem"]}],
                    "italy": [{"languages": ["italian"]}, {"capitals": ["rome"]}],
                    "jamaica": [{"languages": ["english"]}, {"capitals": ["Kingston"]}],
                    "japan": [{"languages": ["japanese"]}, {"capitals": ["tokyo"]}],
                    "jordan": [{"languages": ["arabic"]}, {"capitals": ["amman"]}],
                    "Kazakhstan": [{"languages": ["Kazakh", "russian"]}, {"capitals": ["nur-sultan"]}],
                    "Kenya": [{"languages": ["english"]}, {"capitals": ["nairobi"]}],
                    "Kiribati": [{"languages": ["english"]}, {"capitals": ["tarawa"]}],
                    "Kosovo": [{"languages": ["albanian", "serbian"]}, {"capitals": ["pristina"]}],
                    "Kuwait": [{"languages": ["standard arabic"]}, {"capitals": ["Kuwait city"]}],
                    "Kyrgyzstan": [{"languages": ["Kyrgyz", "russian"]}, {"capitals": ["bishkek"]}],
                    "laos": [{"languages": ["lao"]}, {"capitals": ["vientiane"]}],
                    "latvia": [{"languages": ["latvian"]}, {"capitals": ["riga"]}],
                    "lebanon": [{"languages": ["arabic"]}, {"capitals": ["beirut"]}],
                    "lesotho": [{"languages": ["english"]}, {"capitals": ["maseru"]}],
                    "liberia": [{"languages": ["english"]}, {"capitals": ["monrovia"]}],
                    "libya": [{"languages": ["arabic"]}, {"capitals": ["tripoli"]}],
                    "liechtenstein": [{"languages": ["german"]}, {"capitals": ["vaduz"]}],
                    "lithuania": [{"languages": ["lithuanian"]}, {"capitals": ["vilnius"]}],
                    "luxembourg": [{"languages": ["french", "german", "luxembourgish"]}, {"capitals": ["luxembourg"]}],
                    "macau": [{"languages": ["cantonese", "portuguese"]}, {"capitals": ["macau"]}],
                    "madagascar": [{"languages": ["french", "malagasy"]}, {"capitals": ["antananarivo"]}],
                    "malawi": [{"languages": ["english", "chichewa"]}, {"capitals": ["lilongwe"]}],
                    "malaysia": [{"languages": ["malay"]}, {"capitals": ["Kuala lumpur"]}],
                    "maldives": [{"languages": ["dhivehi"]}, {"capitals": ["male"]}],
                    "mali": [{"languages": ["french"]}, {"capitals": ["bamako"]}],
                    "malta": [{"languages": ["english", "maltese"]}, {"capitals": ["valletta"]}],
                    "marshall islands": [{"languages": ["english"]}, {"capitals": ["majuro"]}],
                    "mauritania": [{"languages": ["arabic"]}, {"capitals": ["nouakchott"]}],
                    "mauritius": [{"languages": ["english"]}, {"capitals": ["port louis"]}],
                    "mexico": [{"languages": ["spanish"]}, {"capitals": ["mexico city"]}],
                    "micronesia": [{"languages": ["woleaian"]}, {"capitals": ["palikir"]}],
                    "moldova": [{"languages": ["romanian"]}, {"capitals": ["chisinau"]}],
                    "monaco": [{"languages": ["french"]}, {"capitals": ["monaco"]}],
                    "mongolia": [{"languages": ["mongolian"]}, {"capitals": ["ulaanbaatar"]}],
                    "montenegro": [{"languages": ["albanian", "croatian", "serbian"]}, {"capitals": ["podgorica"]}],
                    "morocco": [{"languages": ["arabic", "berber"]}, {"capitals": ["rabat"]}],
                    "mozambique": [{"languages": ["portuguese"]}, {"capitals": ["maputo"]}],
                    "myanmar": [{"languages": ["burmese"]}, {"capitals": ["naypyidaw"]}],
                    "namibia": [{"languages": ["english"]}, {"capitals": ["windhoek"]}],
                    "nauru": [{"languages": ["english", "nauruan"]}, {"capitals": ["yaren"]}],
                    "nepal": [{"languages": ["nepali"]}, {"capitals": ["Kathmandu"]}],
                    "netherlands": [{"languages": ["dutch"]}, {"capitals": ["amsterdam"]}],
                    "new zealand": [{"languages": ["english", "maori", "new zealand sign languages"]}, {"capitals": ["wellington"]}],
                    "nicaragua": [{"languages": ["spanish"]}, {"capitals": ["managua"]}],
                    "niger": [{"languages": ["french"]}, {"capitals": ["niamey"]}],
                    "nigeria": [{"languages": ["english"]}, {"capitals": ["abuja"]}],
                    "niue": [{"languages": ["english", "niuean"]}, {"capitals": ["alofi"]}],
                    "north Korea": [{"languages": ["Korean"]}, {"capitals": ["p'yongyang"]}],
                    "north macedonia": [{"languages": ["macedonian", "albanian"]}, {"capitals": ["skopje"]}],
                    "northern cyprus": [{"languages": ["turkish"]}, {"capitals": ["north nicosia"]}],
                    "norway": [{"languages": ["norwegian"]}, {"capitals": ["oslo"]}],
                    "oman": [{"languages": ["arabic"]}, {"capitals": ["muscat"]}],
                    "pakistan": [{"languages": ["english", "urdu"]}, {"capitals": ["islamabad"]}],
                    "palau": [{"languages": ["english", "palauan"]}, {"capitals": ["ngerulmud"]}],
                    "palestine": [{"languages": ["arabic"]}, {"capitals": ["east jerusalem", "ramallah"]}],
                    "panama": [{"languages": ["spanish"]}, {"capitals": ["panama city"]}],
                    "papua new guinea": [{"languages": ["english", "hiri motu", "png sign languages", "tok pisin"]}, {"capitals": ["port moresby"]}],
                    "paraguay": [{"languages": ["spanish", "guarani"]}, {"capitals": ["asunción"]}],
                    "peru": [{"languages": ["spanish", "aymara", "quechua"]}, {"capitals": ["lima"]}],
                    "philippines": [{"languages": ["english", "filipino", "filipino sign languages"]}, {"capitals": ["manila"]}],
                    "poland": [{"languages": ["polish"]}, {"capitals": ["warsaw"]}],
                    "portugal": [{"languages": ["portuguese"]}, {"capitals": ["lisbon"]}],
                    "qatar": [{"languages": ["arabic"]}, {"capitals": ["doha"]}],
                    "romania": [{"languages": ["romanian"]}, {"capitals": ["bucharest"]}],
                    "russia": [{"languages": ["russian"]}, {"capitals": ["moscow"]}],
                    "rwanda": [{"languages": ["english", "french", "Kinyarwanda", "swahili"]}, {"capitals": ["Kigali"]}],
                    "sahrawi arab democratic republic": [{"languages": ["tamazight", "arabic", "spanish"]}, {"capitals": ["laayoune"]}],
                    "saint Kitts and nevis": [{"languages": ["english"]}, {"capitals": ["basseterre"]}],
                    "saint lucia": [{"languages": ["english"]}, {"capitals": ["castries"]}],
                    "saint vincent and the grenadines": [{"languages": ["english"]}, {"capitals": ["Kingstown"]}],
                    "samoa": [{"languages": ["english"]}, {"capitals": ["apia"]}],
                    "san marino": [{"languages": ["italian"]}, {"capitals": ["san marino"]}],
                    "sao tome and principe": [{"languages": ["portuguese"]}, {"capitals": ["sao tome"]}],
                    "saudi arabia": [{"languages": ["arabic"]}, {"capitals": ["riyadh"]}],
                    "senegal": [{"languages": ["french"]}, {"capitals": ["dakar"]}],
                    "serbia": [{"languages": ["serbian"]}, {"capitals": ["belgrade"]}],
                    "seychelles": [{"languages": ["english", "french", "seychellois creole"]}, {"capitals": ["victoria"]}],
                    "sierra leone": [{"languages": ["english"]}, {"capitals": ["freetown"]}],
                    "singapore": [{"languages": ["english", "malay", "mandarin", "tamil"]}, {"capitals": ["singapore"]}],
                    "slovakia": [{"languages": ["slovak"]}, {"capitals": ["bratislava"]}],
                    "slovenia": [{"languages": ["slovene"]}, {"capitals": ["ljubljana"]}],
                    "solomon islands": [{"languages": ["english"]}, {"capitals": ["honiara"]}],
                    "somalia": [{"languages": ["arabic"]}, {"capitals": ["mogadishu"]}],
                    "somaliland": [{"languages": ["arabic", "english", "somali"]}, {"capitals": ["hargeisa"]}],
                    "south africa": [{"languages": ["afrikaans", "english", "southern ndebele", "sotho", "northern sotho", "swazi", "tsonga", "tswana", "venda", "xhosa", "zulu"]}, {"capitals": ["pretoria", "cape town", "bloemfontein"]}],
                    "south Korea": [{"languages": ["Korean", "Korean sign languages"]}, {"capitals": ["seoul"]}],
                    "south ossetia": [{"languages": ["ossetian", "russian"]}, {"capitals": ["tskhinvali"]}],
                    "south sudan": [{"languages": ["english"]}, {"capitals": ["juba"]}],
                    "spain": [{"languages": ["spanish"]}, {"capitals": ["madrid"]}],
                    "sri lanka": [{"languages": ["sinhala", "tamil"]}, {"capitals": ["sri jayawardenapura Kotte"]}],
                    "sudan": [{"languages": ["arabic", "english"]}, {"capitals": ["Khartoum"]}],
                    "suriname": [{"languages": ["dutch"]}, {"capitals": ["paramaribo"]}],
                    "sweden": [{"languages": ["swedish"]}, {"capitals": ["stockholm"]}],
                    "switzerland": [{"languages": ["french", "german", "italian", "romansh"]}, {"capitals": ["bern"]}],
                    "syria": [{"languages": ["arabic"]}, {"capitals": ["damascus"]}],
                    "taiwan": [{"languages": ["mandarin"]}, {"capitals": ["taipei"]}],
                    "tajikistan": [{"languages": ["tajik"]}, {"capitals": ["dushanbe"]}],
                    "tanzania": [{"languages": ["english"]}, {"capitals": ["dodoma"]}],
                    "thailand": [{"languages": ["thai"]}, {"capitals": ["bangkok"]}],
                    "togo": [{"languages": ["french"]}, {"capitals": ["lome"]}],
                    "tonga": [{"languages": ["english"]}, {"capitals": ["nukuʻalofa"]}],
                    "transnistria": [{"languages": ["moldovan", "russian", "ukrainian"]}, {"capitals": ["tiraspol"]}],
                    "trinidad and tobago": [{"languages": ["english"]}, {"capitals": ["port of spain"]}],
                    "tunisia": [{"languages": ["arabic"]}, {"capitals": ["tunis"]}],
                    "turkey": [{"languages": ["turkish"]}, {"capitals": ["ankara"]}],
                    "turkmenistan": [{"languages": ["turkmen"]}, {"capitals": ["ashgabat"]}],
                    "tuvalu": [{"languages": ["english"]}, {"capitals": ["fongafale"]}],
                    "uganda": [{"languages": ["english", "swahili"]}, {"capitals": ["Kampala"]}],
                    "ukraine": [{"languages": ["ukrainian"]}, {"capitals": ["Kiev"]}],
                    "united arab emirates": [{"languages": ["arabic"]}, {"capitals": ["abu dhabi"]}],
                    "united Kingdom": [{"languages": ["english"]}, {"capitals": ["london"]}],
                    "unites states of america": [{"languages": ["none"]}, {"capitals": ["washington, d.c."]}],
                    "uruguay": [{"languages": ["spanish"]}, {"capitals": ["montevideo"]}],
                    "uzbekistan": [{"languages": ["uzbek"]}, {"capitals": ["tashkent"]}],
                    "vanuatu": [{"languages": ["english", "french"]}, {"capitals": ["port vila"]}],
                    "vatican city": [{"languages": ["italian"]}, {"capitals": ["vatican city"]}],
                    "venezuela": [{"languages": ["spanish", "venezuelan sign languages"]}, {"capitals": ["caracas"]}],
                    "vietnam": [{"languages": ["none"]}, {"capitals": ["hanoi"]}],
                    "yemen": [{"languages": ["arabic"]}, {"capitals": ["sana'a"]}],
                    "zambia": [{"languages": ["english"]}, {"capitals": ["lusaka"]}],
                    "zimbabwe": [{"languages": ["chewa", "chibarwe", "english", "Kalanga", "Khoisan", "nambya", "ndau", "ndebele", "shangani", "shona", "sign languages", "sotho", "tonga", "tswana", "venda", "xhosa"]}, {"capitals": ["harare"]}],
                    }

def main():
    """ Main function done by both Mike and Marissa"""
    play_again = "y"

    while play_again == "y" or play_again == "Y":

        # Initialize variables at the start of each game.
        user_difficulty = ""
        user_score = 0
        visited_countries_indices = []
        country_visited = False
        first_time = True
        user_wants_key = ""
        main_loop_index = 0
        tie_is_broken = True
        tie_question = ""
        tie_questions_counter = 0
        second_player_question = ""
        player2_score = 0
        list_of_answers_player_1 = []
        list_of_answers_player_2 = []
        
        # Pick the game mode. Either one player or two players mode.
        while second_player_question != "1" and second_player_question != "2":
            try:
                second_player_question = str(int(input("Type '1' for single player or '2' two player mode: ")))
            except ValueError:
                print("Oops.. you didn't type a number.")

        # If one player mode is selected, the player is asked to define the computer's level of difficulty
        if second_player_question == "1":
            while user_difficulty != "h" and user_difficulty != "H" and user_difficulty != "e" and user_difficulty != "E":
                user_difficulty = str(input("Select a level of difficulty. Type 'e' for easy or 'h' for hard: "))

        # This is the main loop. It will keep iterating as long a the number of questions to be asked
        # is not reached or if the user chose to break the tie.
        while main_loop_index < NUMBER_OF_QUESTIONS or tie_is_broken == False:

            # Generating a random answer that will be used to be compared to the user's answer.
            random_country_index = generate_random_country_index(visited_countries_indices)

            # The following code will only be executed if a random country number, that doesn't
            # belong to a visited country, has been generated

            # Since the randomly picked country hasn't been visited its index is added to the list
            # of visited countries indices
            visited_countries_indices.append(random_country_index)

            # This answer contains what the question is about plus a country and its data.
            answer = get_answer(random_country_index)

            # the answer is added to the user's list of answers.
            list_of_answers_player_1.append(answer)

            # This function asks the appropriate question depending on the answer
            ask_question(answer)

            # After a random question is asked, it is time for the players to answer it.
            # The first player starts, if they got the right answer then their score increase by 1
            # otherwise their score stays the same.
            user_score = user_turn(answer, user_score, 1)

            # Repeating the same steps for player 2
            random_country_index = generate_random_country_index(visited_countries_indices)
            visited_countries_indices.append(random_country_index)
            answer = get_answer(random_country_index)
            list_of_answers_player_2.append(answer)            
            ask_question(answer)         

            if second_player_question == "1":
                # The second player starts, this time it is the computer. Their performance is generated
                # randomly and depending on the difficulty. The easy mode gives more chances to the computer
                # to make mistakes while the hard mode gives less chances to make mistakes.
                player2_score = computer_turn(user_difficulty, player2_score)            
            else:
                # The second player starts playing
                player2_score = user_turn(answer, player2_score, 2)

            # If it is the last question or the user decided to break a tie
            if main_loop_index == NUMBER_OF_QUESTIONS - 1 or tie_is_broken == False:
                
                # Display information about the players performance
                print("")                
                print("Player 1 answered " + str((user_score)) + "/" + str((NUMBER_OF_QUESTIONS+tie_questions_counter)) + " (" + str(round(user_score/(NUMBER_OF_QUESTIONS+tie_questions_counter)*100, 2)) + "%) questions correctly.")

                if second_player_question == "1":
                    print("The computer", end = " ")
                else:
                    print("Player 2", end = " ")
                    
                print("answered " + str((player2_score)) + "/" + str((NUMBER_OF_QUESTIONS+tie_questions_counter)) + " (" + str(round(player2_score/(NUMBER_OF_QUESTIONS+tie_questions_counter)*100, 2)) + "%) questions correctly.")

                # Show who won
                print("")
                if user_score > player2_score:
                    if second_player_question == "1":
                        print("You won!")
                    else:
                        print("Player 1 won!")
                    tie_is_broken = True
                elif user_score < player2_score:
                    if second_player_question == "1":
                        print("Sorry. The computer won.")
                    else:
                        print("Player 2 won!")                    
                    tie_is_broken = True
                else:
                    # If it's a tie ask the user if they want to break it. If they decide to do so
                    # another question will be asked for reach player
                    while tie_question != "y" and tie_question != "Y" and tie_question != "n" and tie_question != "N":
                        tie_question = str(input("It's a tie! Would you like to answer one more question to break the tie? Type 'y' for yes or 'n' for no: "))

                    if tie_question == "y" or tie_question == "Y":
                        tie_is_broken = False
                        tie_questions_counter += 1

                    tie_question = ""

            main_loop_index += 1

        # After all the answers have been answered and a possible tie broken
        # ask the user if they want to have a key to display all quiz answers
        print("")
        while user_wants_key != "y" and user_wants_key != "Y" and user_wants_key != "n" and user_wants_key != "N":
            user_wants_key = str(input("Would you like to have a key to display all quiz answers? Type 'y' for yes or 'n' for no: "))
        
        if user_wants_key == "y" or user_wants_key == "Y":
            # Key to display all quiz for player 1
            print("")
            print("Player 1. Here are the answers to all the questions: ")
            print("")
            i = 0
            for answer_in_list in list_of_answers_player_1:
                print("Question " + str(i + 1) + ":", end = "")            
                ask_question(answer_in_list)
                print("Answer " + str(i + 1) + ":")    
                the_answer_is(answer_in_list)
                i += 1

            # Key to display all quiz for player 2
            if second_player_question != "1":
                print("")
                print("Player 2. Here are the answers to all the questions: ")
                print("")
                i = 0
                for answer_in_list in list_of_answers_player_2:
                    print("Question " + str(i + 1) + ":", end = "")            
                    ask_question(answer_in_list)
                    print("Answer " + str(i + 1) + ":")    
                    the_answer_is(answer_in_list)
                    i += 1                

        # Finally, when a game is over, ask the user if they want to play again.
        print("")
        play_again = ""
        while play_again != "y" and play_again != "Y" and play_again != "n" and play_again != "N":
            play_again = str(input("Would you like to play the game again? Type 'y' for yes or 'n' for no: "))
        print("")


def generate_random_country_index(visited_countries_indices):
    """ This function keeps generating a random number until it 
    finds one that doesn't exist in the list of visited countries indices. Created My Marissa, edited by Mike."""

    country_visited = True

    # Loop that checks whether a country has already been visited.
    while country_visited == True:

        # Resetting the flag variables to the initial value
        country_visited = False

        # Generate a random number between 0 and 204 to be used to access a country randomly
        random_country_index = random.randint(1, len(SOVEREIGN_STATES))

        # Check if the randomly generated index exists in the list of visited countries indices
        for country_index in visited_countries_indices:
            if country_index == random_country_index:
                country_visited = True    
    
    return random_country_index


def user_turn(answer, user_score, player_number):
    """ Function that increases the user_score if they got the right answer. Created by Mike. Edited by Marissa. """

    # This variable is initialized to 0 to allow entering the loop that asks for the user answer.
    user_answer = "0"
    user_answered_correctly = False

    # Show the answer if this is one
    if(SECRET_DEVELOPER_OPTION_SHOW_ANSWERS):
        the_answer_is(answer)

    print("Player " + str(player_number) + "'s turn:")

    if answer[0] == "LANGUAGES":

        while answer_contains_expected_chars(user_answer, "language") == False:
            user_answer = input("Type an answer: ")

        for language in answer[1][1][0]["languages"]:
            # Compare everything in lowercase to make the comparison case insensitive.
            if user_answer.lower() == language.lower():
                user_answered_correctly = True
                user_score += 1
    else:

        while answer_contains_expected_chars(user_answer, "capital") == False:
            user_answer = input("Type an answer: ")

        for capital in answer[1][1][1]["capitals"]:
            # Compare everything in lowercase to make the comparison case insensitive.
            if user_answer.lower() == capital.lower():
                user_answered_correctly = True
                user_score += 1
            
    print("")
    if user_answered_correctly == False:
        print("Oops.. that's wrong. Here is the correct answer:")
    else:
        print("Correct answer!")

    the_answer_is(answer)

    print("")

    return user_score


def computer_turn(user_difficulty, player2_score):
    """ Function that increases the computer_turn randomly and depending on the user difficulty. Created by Marissa and Mike. """
    print("The computer's turn...")

    answer = ("","")

    if user_difficulty == "e":
        random_question = random.randint(2,10)
    else:
        random_question = random.randint(1,6)

    if random_question <= 5:
        player2_score += 1

    print("The computer's is done.")

    print("")

    return player2_score


def get_answer(random_country_index):
    """ Function that randomly decides the type of the answer (either LANGUAGES or CAPITALS). 
    It also accesses the dictionary using the randomly generated index and it fetches the 
    corresponding item from it. Created by Marissa."""

    random_question = random.randint(1,10)
    answer = ("","")

    try:
        if random_question <= 5:
            answer = ("LANGUAGES", list(SOVEREIGN_STATES.items())[random_country_index])
        else:
            answer = ("CAPITALS", list(SOVEREIGN_STATES.items())[random_country_index])

    except IndexError:
        print("There is no country with the index " + random_country_index)

    return answer


def answer_contains_expected_chars(user_answer, user_answer_type):
    """ Function that checks if the user answer doesn't contain unexpected characters. Created by Marissa and Mike. """

    for character in user_answer:
        if character.isdigit():
            # If this is not the first time
            if user_answer != "0":
                print("Incorrect " + user_answer_type +  " name, your answer containes a number. Try again.")
            return False

    return True


def the_answer_is(answer):
    """ Function that displays the answer, whatever its type is, appropriately. Created by Mike, altered by Marissa """

    print(capitalize_first_letter(answer[1][0]) + " has the following", end = " ")

    if(answer[0] == "LANGUAGES"):
        singular_noun = "language"
        spot = 0
    else:
        singular_noun = "capital"
        spot = 1

    if len(answer[1][1][spot][singular_noun + "s"]) == 1:
        print(singular_noun + ":", end = " ")
    else:
        print(singular_noun + "s:", end = " ")

    i = 0
    for item in answer[1][1][spot][singular_noun + "s"]:
        if i != len(answer[1][1][spot][singular_noun + "s"]) - 1 and i != len(answer[1][1][0][singular_noun + "s"]) - 2:
            print(capitalize_first_letter(item) + ", ", end = "")
        elif i == len(answer[1][1][spot][singular_noun + "s"]) - 2:
            print(capitalize_first_letter(item) + " and ", end = "")
        else:
            print(capitalize_first_letter(item) + ".")
        i += 1

    print("")


def capitalize_first_letter(word):
    """ Function that capitalizes the first letters of words in the input. Created by Marissa and Mike. """
    
    j = 0
    capitalized_word = ""

    list_of_words_in_name = word.split()

    for word_in_name in list_of_words_in_name:       
        i = 0 
        for char in word_in_name:
            if i == 0:
                capitalized_word += char.upper()
            else: 
                capitalized_word += char
            i += 1    

        if j != len (list_of_words_in_name) - 1:
            capitalized_word += " "

        j += 1

    return capitalized_word


def ask_question(answer):
    """Function that asks a question depending on the answer given. Created by Marissa. """
    print("")
    print("What", end = " ")
    # If the randomly generated answer is about languages, a question about
    # the country's language is asked.
    if answer[0] == "LANGUAGES":
        if len (answer[1][1][0]["languages"]) == 1:
            print("is the official language of " + capitalize_first_letter(answer[1][0]) + "?")
        else:
            print("is one of the official languages of " + capitalize_first_letter(answer[1][0]) + "?")

    # Else if the randomly generated answer is about capitals, a question about
    # the country's capital is asked.
    else:
        if len (answer[1][1][1]["capitals"]) == 1:
            print("is the capital of " + capitalize_first_letter(answer[1][0]) + "?")
        else:
            print("is one of the capitals of " + capitalize_first_letter(answer[1][0]) + "?")
    print("")

# Invoke the main function
main()