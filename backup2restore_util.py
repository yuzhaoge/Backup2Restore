#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import argparse
import datetime

def parse_args():
    """parse args for backup2restore"""
    parser = argparse.ArgumentParser(description='backup and restore with python', add_help=False)
    parser.add_argument('-h', '--host',dest='host', type=str, help='Host the MySQL database server located',default=None)
    parser.add_argument('-P', '--port', dest='port', type=int, help='MySQL port to use', default=3306)
    parser.add_argument('-u', '--user', dest='user', type=str, help='MySQL Username to log in as', default='root')
    parser.add_argument('-p', '--password', dest='password', type=str, help='MySQL Password to use', default='')
    parser.add_argument('--help', dest='help', action='store_true', help='help information', default=False)
    return parser

def command_line_args(args):
    need_print_help = False if args else True
    parser = parse_args()
    args = parser.parse_args(args)
    if args.help or need_print_help:
        parser.print_help()
        sys.exit(1)
    return args


def check_port():
    """check port if used"""
    pass

def check_basedir():
    """check basedir if used"""
    pass

def check_datadir():
    """check basedir if used"""
    pass

def generate_server_id():
    pass

def check_xtrabackup():
    pass


def is_backup_or_restore(arg):
     if not arg in ["--backup", "--restore"]:
        return False
     return True


