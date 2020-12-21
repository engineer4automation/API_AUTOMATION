import configparser
import os
import random
import datetime


def get_url():
    config_parser = configparser.RawConfigParser()
    config_file_path = os.getcwd() + '/config.ini'
    config_parser.read(config_file_path)
    return config_parser.get('URL', 'url')


def get_email() -> object:
    config_parser = configparser.RawConfigParser()
    config_file_path = os.getcwd() + '/config.ini'
    config_parser.read(config_file_path)
    today = datetime.datetime.now()
    date_time = today.strftime("%m%d%Y.%H%M%S")
    base = config_parser.get('EMAIL', 'base')
    domain = config_parser.get('EMAIL', 'domain')
    email = base + date_time + domain
    return email


def get_config(argument):
    config_parser = configparser.RawConfigParser()
    config_file_path = os.getcwd() + '/config.ini'
    config_parser.read(config_file_path)
    lowerCaseArgument = argument.lower()
    return config_parser.get(argument, lowerCaseArgument)
