#!/usr/bin/env python

import re
import sys

green_color = "\033[1;32m"
red_color = "\033[1;31m"
default_color = "\033[0m"

PATH_TO_REPOSITORY = "./"

# Регулярное выражение для проверки формата сообщения коммита
conventional_commit_message_regex = r'^((?:build|chore|ci|docs|feat|fix|perf|refactor|revert|style|test)(?:\([\w\-\.]+\))?)!??: (.+)$'

#
#
#
#

def validate_commit_message():
    if len(sys.argv) != 2:
        print(f"prepare-commit-conventional-hook: {red_color}Error! Incorrect count argvs!{default_color}")
        return False
    
    commit_msg_file = sys.argv[1]
    
    try:
        with open(commit_msg_file, 'r') as f:
            commit_message = f.read().strip()
        
        match = re.match(conventional_commit_message_regex, commit_message)
        if match:
            return True
        else:
            return False
    except FileNotFoundError:
        print(f"prepare-commit-conventional-hook: {red_color}Error! File '{commit_msg_file}' not found.{default_color}")
        return False

#
#
#
#

if __name__ == "__main__":
    if validate_commit_message():
        print(f"prepare-commit-conventional-hook: {green_color}Commit message is valid.{default_color}")
    else:
        print(f"prepare-commit-conventional-hook: {red_color}Failed! The commit message does not comply with Conventional Commits standards!{default_color}")
        print(f"pattern: {conventional_commit_message_regex}")
        sys.exit(1)

