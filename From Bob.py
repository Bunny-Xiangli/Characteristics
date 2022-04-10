#
# Copyright (c) 2021 Ericsson AB.
# All rights reserved.
#

import yaml
import sys
import os
import string
import getopt
import time
from xml.etree import ElementTree as ET


def now_time():
    return time.asctime(time.localtime(time.time()))


display_help = """
This script is used to generate new commands during ISSU.

To do it, run the manual_migration.py with the optional -s <file> -o <file> options.
Usage:   manual_migration.py -s <file> -r <file> -o <file>
Example: manual_migration.py -s ericsson.cfg -r rule.xml -o migration_commands.cfg
Options Description:
    -h|--help          : Display this help
    -l <file>.  Specify the log output file
    -s|--source <file> . Use a specified file as saved configuration file
    -r|--rule <file>.  Specify the rule file
    -o <file>.  Specify the output file
"""
help_argv = ["-h", "--help"]
source_argv = ["-s", "--source"]
rule_argv = ["-r", "--rule"]

source_cfg = "ericsson.cfg"
output_cfg = "migration_commands.cfg"
rule_file = "rule.xml"
log_file = "upgrade.log"
log_file_fp = 0
read_fp = 0
write_fp = 0
rule_tree = []
rule_tree_index = 0
action_list = []


#
# The string_matching function is used to detect whether a string matches a rule
# rules_str : Need to match the rules
# test_str  : Need to detect the command
# return    : Returns true if successful, false if failed
#
def string_matching(rules_str, test_str):
    if type(test_str) != str or type(rules_str) != str:
        return False
    if rules_str == test_str:
        return True
    if rules_str != '':
        rules_first_char = rules_str[0]
    else:
        rules_first_char = ''
    if test_str != '':
        test_first_char = test_str[0]
    else:
        test_first_char = ''
    if rules_first_char != '.' and rules_first_char != '*':
        if rules_first_char != test_first_char:
            return False
        else:
            rules_str = rules_str[1:]
            test_str = test_str[1:]
            return string_matching(rules_str, test_str)
    if rules_first_char == '.':
        rules_str = rules_str[1:]
        test_str = test_str[1:]
        return string_matching(rules_str, test_str)
    if rules_first_char == '*' and rules_str.strip('*') == '':
        return True
    if test_str[1:] == '':
        return False
    return string_matching(rules_str, test_str[1:]) or string_matching(rules_str[1:], test_str)


def print_log(*argv):
    if len(argv) == 1:
        Str = '[%s] %s\n' % (now_time(), argv[0])
    else:
        Str = '[%s] line:%d [%s] %s\n' % (now_time(), line_num, argv[0], argv[1])
    log_file_fp.write(Str)


def intend_level(str):
    return len(str) - len(str.lstrip(' '))


def add_to_intend_tree(read_fp, old_list, old_level):
    newline = read_fp.readline()
    if not newline:
        return old_list
    if newline == "!":
        return old_list
    current_level = intend_level(newline)
    line = newline.strip()
    if current_level == old_level:
        old_list.append(line)
        result = add_to_intend_tree(read_fp, old_list, old_level)
        return old_list
    elif current_level > old_level:
        newlist = [line]
        result = add_to_intend_tree(read_fp, newlist, current_level)
        old_list.append(result)
        return old_list
    elif current_level < old_level:
        return old_list

    return old_list


def compare_indent_tree(rule_list, command_tree, write_fp, intend_level):
    intend = " " * intend_level
    for index in range(len(command_tree)):
        if string_matching(rule_list[0], command_tree[index]):
            if len(rule_list) == 1:
                write_fp.write(intend + "no " + command_tree[index] + '\n')
                write_fp.write(intend + action_list[rule_tree_index] + '\n')
                return True
            write_fp.write(intend + command_tree[index] + '\n')
            intend_level += 1
            if compare_indent_tree(rule_list[1], command_tree[index + 1], write_fp, intend_level):
                intend = " " * (intend_level - 1)
                write_fp.write(intend + '!\n')
                return True
    return False


def traverseXml(element, old_tree):
    if len(element) > 0:
        new_tree = []
        for child in element:
            if "description" in child.keys():
                new_tree.append(child.attrib["description"])
            elif child.get("operation") == "new":
                global action_list
                action_list.append(child.get("name"))
            else:
                new_tree.append(child.get("name"))
            traverseXml(child, new_tree)
        old_tree.append(new_tree)


def cfg2cfg_init():
    global log_file_fp
    global log_file
    log_file_fp = open(log_file, 'w', encoding='utf-8')

    global rule_file
    tree = ET.parse(rule_file)
    root = tree.getroot()
    global rule_tree
    for child in root:
        new_tree = []
        new_tree.append(child.attrib["description"])
        traverseXml(child, new_tree)
        rule_tree.append(new_tree)

    print_log(rule_tree)
    print_log(action_list)


def cfg2cfg_process(source, output):
    global read_fp
    global write_fp
    print_log("source_file = \'%s\'" % source)
    print_log("output_file = \'%s\'" % output)
    try:
        read_fp = open(source, 'r', encoding='utf-8')
        write_fp = open(output, 'w', encoding='utf-8')
    except:
        print_log('File open failed!!!')
        if read_fp | write_fp:
            if read_fp:
                read_fp.close()
            if write_fp:
                write_fp.close()
            sys.exit(1)
    global rule_tree_index

    intend_tree = []
    command_tree = add_to_intend_tree(read_fp, intend_tree, 0)
    print_log(command_tree)
    print_log(len(command_tree))

    while command_tree != []:
        if compare_indent_tree(rule_tree[rule_tree_index][1], command_tree, write_fp, 0):
            write_fp.write("#" + rule_tree[rule_tree_index][0] + '\n')

        intend_tree = []
        command_tree = add_to_intend_tree(read_fp, intend_tree, 0)

    print("the commands for new PCG is stored in file: %s" % (output_cfg))
    print("the tool logs can be found in file: %s" % (log_file))
    read_fp.close()
    write_fp.close()


def cfg2cfg_finish():
    log_file_fp.close()


def main():
    # Get the file parameters
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hs:r:o:l:", ["help", "source=", "rule="])
    except:
        print("Parameter acquisition failed")
        sys.exit(1)
    # Parse the file parameters
    for opt, value in opts:
        if opt in help_argv:
            print(display_help)
            sys.exit(0)
        elif opt in source_argv:
            global source_cfg
            source_cfg = value
        elif opt in rule_argv:
            global rule_file
            rule_file = value
        elif "-o" == opt:
            global output_cfg
            output_cfg = value
        elif "-l" == opt:
            global log_file
            log_file = value

    if False == os.path.exists(source_cfg):
        print("source cfg file is not exists: %s" % (source_cfg))
        sys.exit(1)
    if False == os.path.exists(rule_file):
        print("rule file is not exists: %s" % (rule_file))
        sys.exit(1)
    # Initialize the rule tree
    cfg2cfg_init()
    # File conversion
    cfg2cfg_process(source_cfg, output_cfg)
    cfg2cfg_finish()


if __name__ == '__main__':
    main()


