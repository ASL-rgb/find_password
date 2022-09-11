import string
from pyfiglet import figlet_format
import argparse
import multiprocessing

def intro():
    print(figlet_format('Custom Password Creation', font='future'))
    parser = argparse.ArgumentParser(description='Programm is designed to create a Password based on personal information')
    parser.add_argument('--prefix', '-pf', required=False, action='store', default=2, type=int)
    parser.add_argument('--subfix', '-sf', required=False, action='store', default=2, type=int)
    parser.add_argument('--password', '-p', required=True, help='Provide Personal Information, this will create a Password from it.')
    #parser.add_argument('--safe', required=True, metavar='-s', action='store', dest='file', default='./', type=str
    #                   , help='Specify the Path in which the file will be saved')

    args = parser.parse_args()
    intro.subfix = args.subfix
    intro.prefix = args.prefix
    intro.password = args.password





def main():
    intro()
    allstrings = string.ascii_letters + string.digits + string.punctuation
    print(len(allstrings))
    allfix = intro.subfix + intro.prefix
    allCombinationLength = len(allstrings)**allfix
    floating_indicator = []
    PassList = []

    lost_list = []
    allfix_counter = 0
    prefix = []
    subfix = []
    prestring = ""
    substring = ""
    countpre = 0
    countsub = 0
    pre_count = 0
    allist = list(allstrings)

    # calculate all the indication points

    for i in range(1, intro.subfix):
        floating_indicator.append(len(allstrings)**i)
    # In the main Algorythm we miss some possible string combinations,
    # in the code below we append them in prefix list

    if intro.prefix > 0:

        for y in allstrings:
            if pre_count == intro.prefix:
                break
            lost_list.append(y)
            pre_count += 1

        pre_count = 0
        while pre_count != intro.prefix:
            diff = intro.prefix - pre_count - 1
            for x in range(0, intro.prefix):
                loststring = diff*lost_list[pre_count] + lost_list[x] + pre_count*lost_list[pre_count]
                prefix.append(loststring)
            pre_count += 1

        # Below is the Algorythm to generate all possible combinations for prefixes



        for i in range(0, intro.prefix):
            allfix_counter += 1
            for fix in allstrings:

                    if countpre % intro.prefix == 0:
                        fix = allist[i]
                        countpre = 0
                    if len(prestring) == intro.prefix:
                        prefix.append(prestring)

                        prestring = ""
                    prestring += fix
                    countpre += 1

    # In the main Algorythm we miss some possible string combinations,
    # in the code below we append them in subfix list

    if intro.subfix > 0:
        sub_count = 0
        lost_list = []

        for y in allstrings:
            if sub_count == intro.subfix:
                break
            lost_list.append(y)
            sub_count += 1


        if intro.subfix > 0:

            for y in allstrings:
                if sub_count == intro.subfix:
                    break
                lost_list.append(y)
                sub_count += 1

            sub_count = 0
            while sub_count != intro.subfix:
                diff = intro.subfix - sub_count - 1
                for x in range(0, intro.subfix):
                    loststring = diff * lost_list[sub_count] + lost_list[x] + sub_count * lost_list[sub_count]
                    subfix.append(loststring)
                sub_count += 1


        # This is Main Algorythm to generate all possible combinations for subfixes

        for i in range(0, intro.subfix):
            allfix_counter += 1
            for fix in allstrings:

                    if countsub % intro.subfix == 0:
                        if subfix == 1:
                            continue
                        else:
                            fix = allist[i]
                            countsub = 0
                    if len(substring) == intro.subfix:
                        subfix.append(substring)

                        substring = ""
                    substring += fix
                    countsub += 1
    File = open(f"{intro.password}.txt", 'w')
    if len(prefix) > 0:
        for i in prefix:
            if len(subfix) < 1:
                Password = i + intro.password
                File.write(Password + "\n")
            else:
                for z in subfix:
                    Password = i + intro.password + z
                    File.write(Password + "\n")

    elif len(subfix) > 0:
        for i in subfix:
            if len(prefix) < 1:
                Password = intro.password + i
                print(Password)
                File.write(Password + "\n")
            else:
                for x in prefix:
                    Password = x + intro.password + i
                    print(Password)
                    File.write(Password + "\n")



    File.close()


if __name__ == '__main__':
    main()
