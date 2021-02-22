import sys
import datetime
import calendar

inputfile = '_scripts/sessions.txt'

try:
    with open(inputfile, encoding='utf8') as f:
        content = f.readlines()
except Exception as e:
    print('File could not be opened.', e)
    sys.exit(3)

TRAINING_SPEAKER_LIST = open("_scripts/training_speaker_list.txt", "w", encoding='utf8')
TRAINING_WORKSHOP_LIST = open("_scripts/training_workshops_affiliates_list.txt", "w", encoding='utf8')
TRAINING_MEETINGS_LIST = open("_scripts/training_meetings_list.txt", "w", encoding='utf8')

current_session_id = 'XXXX'
current_session_title = 'YYYY'
first_submission = True

for line in content:
    entry = line.strip().split("\t")
    if entry[1].startswith('cer') or entry[1].startswith('ci') or entry[1].startswith('ert') or entry[1].startswith('toce') or entry[1].startswith('engage') or entry[1].startswith('nifty') or entry[1].startswith('pss'):
        print("paper - ", entry[1], len(entry))
        if len(entry) == 12:
            try:
                name_list = entry[10].strip().split(';')
                email_list = entry[11].strip().split(',')
                for i in range(len(name_list)):
                    if (name_list[i] != '' and name_list[i] != '#N-A'):
                        TRAINING_SPEAKER_LIST.write(name_list[i].strip() + "," + email_list[i].strip() + "\n")
            except:
                print("FAILURE - ", entry[1])
    elif entry[1].startswith('w'):
        print("w - ", entry[1], len(entry))
        if len(entry) == 12:
            try:
                name_list = entry[10].strip().split(';')
                email_list = entry[11].strip().split(',')
                for i in range(len(name_list)):
                    if (name_list[i] != '' and name_list[i] != '#N-A'):
                        TRAINING_WORKSHOP_LIST.write(name_list[i].strip() + "," + email_list[i].strip() + "\n")
            except:
                print("FAILURE - ", entry[1])
    elif entry[1].startswith('b') or entry[1].startswith('src') or entry[1].startswith('d') or entry[1].startswith('p'):
        print("w - ", entry[1], len(entry))
        if len(entry) == 12:
            try:
                name_list = entry[10].strip().split(';')
                email_list = entry[11].strip().split(',')
                for i in range(len(name_list)):
                    if (name_list[i] != '' and name_list[i] != '#N-A'):
                        TRAINING_MEETINGS_LIST.write(name_list[i].strip() + "," + email_list[i].strip() + "\n")
            except:
                print("FAILURE - ", entry[1])


    # if entry[3] == '':
    #     first_submission = True
    #     current_session_id = entry[1]
    #     if len(entry) > 9:
    #         if entry[9] == '' or entry[9] == '#N-A':
    #             current_session_title = entry[2]
    #         else:
    #             current_session_title = entry[9]
    #     else:
    #         current_session_title = entry[2]
        # f.write('- session_id: "' + current_session_id + '"\n')
        # f.write('  session_title: "' + current_session_title + '"\n')
        # if entry[4] != '':
        #     start_time = datetime.datetime.strptime(entry[4], "%m-%d-%Y %H:%M")
        #     end_time = datetime.datetime.strptime(entry[5], "%m-%d-%Y %H:%M")
        #     f.write('  day: "' + start_time.strftime("%A, %B %d") + '"\n')
        #     f.write('  start_time: "' + start_time.strftime("%I:%M %p") + ' (ET)"\n')
        #     f.write('  end_time: "' + end_time.strftime("%I:%M %p") + ' (ET)"\n')
        
        # elif entry[1].startswith('pss') or entry[1].startswith('nifty'):
        #     #f.write('  session_type: "Panel / Special Session"\n')
        # elif entry[2].startswith('Demo'):
        #     #f.write('  session_type: "Demonstration"\n')
        # elif entry[2].startswith('ACM S'):
        #    # f.write('  session_type: "ACM SRC"\n')
        # elif entry[6].startswith('Special Ev'):
        #    # f.write('  session_type: "Special Event"\n')
        # elif entry[6].startswith('Key'):
        #    # f.write('  session_type: "Keynote"\n')
        # elif entry[6].startswith('Poster'):
        #    # f.write('  session_type: "Poster"\n')
        # elif entry[6].startswith('Lightning'):
        #    # f.write('  session_type: "Lightning Talk"\n')
        # elif entry[1].startswith('bof'):
        #   #  f.write('  session_type: "Birds of a Feather"\n')
    # else:
    #     if first_submission:
    #         first_submission = False
    #         f.write('  submissions:\n')
    #     f.write('    - id: "' + entry[1] + '"\n')
    #     f.write('      title: "' + entry[2] + '"\n')
