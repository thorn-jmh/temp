#!/usr/bin/python
# -*- coding: UTF-8 -*-

import getopt
import os
import re
import sys

address = '/home/thorn/WTF/cs/thorn-jmh/notify-scrapy-master/notify_scrapy'

# sys.path.append('address')
# This is only used for test, normally this code is not necessary, if you find something wrong like
# ModuleNotFind Error,you can use this code by changing the sys.path.append(where_is_your_notify-scrapy)

from pages_converters import get_pages_converter

VERSION = '3.3'
CLASS_TEMPLATE = address+ '/spider_generator/template/class.py'
SUBCLASS_TEMPLATE = address + '/spider_generator/template/subclass.py'
WRAPPER_TEMPLATE = address + '/spider_generator/template/wrapper.py'

# This file is edited by Br at 2021/5/18 , and now it doesn't need more instructions to be used together
# with 'generator.py -o <output file> <config file>', you can just use
# 'py generator.py' to use this script. But remember, you need to put all of your configs in the folder
# named 'configs' lied in the same directory of generator.py . The output .py files will be put in the
# folder 'output_py' in the same directory of generator.py


# def print_help():
#     print('Usage: generator.py -o <output file> <config file>')


def main(argv):
    # try:
    #     opts, args = getopt.getopt(argv, "hc:o:", ["help", "config=", "output="])
    # except getopt.GetoptError as err:
    #     print(err)
    #     print_help()
    #     sys.exit(2)
    #
    # if len(args) < 1:
    #     print('Config file is required.')
    #     print_help()
    #     sys.exit(2)
    now_folder = os.path.dirname(os.path.realpath(__file__))
    config_folder = now_folder + '/configs'
    for config_file in os.listdir(config_folder):
        output = now_folder + '/output_py/' + os.path.splitext(config_file)[0] + '.py'

        # for opt, arg in opts:
        #     if opt in ('-h', '--help'):
        #         print_help()
        #         sys.exit()
        #     elif opt in ('-o', '--output'):
        #         output = arg

        with open(now_folder+'/configs/'+config_file, 'r', encoding='utf-8') as fp:
            if config_file.endswith('.yaml') or config_file.endswith('.yml'):
                import yaml
                config = yaml.safe_load(fp)
            elif config_file.endswith('.json'):
                import json
                config = json.load(fp)
            else:
                print('Unknown config file type. Only .json and .yaml/.yml are supported.')
                exit(-1)

        version = config.get('version')
        if not version:
            print('Invalid config file: the version must be provided.')
            exit(-1)
        version = str(version)
        if version.split('.')[0] != VERSION.split('.')[0]:
            print('Invalid config file: the config file is of version %s, but the generator only supports version %s.x.' % (
                version, VERSION.split('.')[0]))
            exit(-1)

        pages_converter = config.get('pages_converter')
        if pages_converter:
            converter = get_pages_converter(pages_converter)
            if converter:
                config['pages'] = converter(config['pages'])

        with open(output, 'w', encoding='utf-8') as fp:
            fp.write(generate_spider(config))

    print("Success! Spider has been saved in %s." % output)
    print('Be sure to test the spider before deploying it.')


def generate_spider(config: dict):
    name = re.split(r'[\s,_\-]', config['name'])
    with open(CLASS_TEMPLATE, 'r') as fp:
        class_template = fp.read()
    init_page = config['pages'][0]
    init_page_name = name + re.split(r'[\s,_\-]', init_page['name'])
    super_class_name = get_camel_case(init_page_name + ['spider'])
    class_res = class_template.format(
        version=VERSION,
        class_name=super_class_name,
        spider_name=get_snake_case(init_page_name),
        publisher=init_page.get('publisher', config['publisher']),
        source=init_page.get('source', config['source']),
        column=init_page.get('column', config.get('column', [])),
        initial_url=init_page['initial_url'],
        page_url=init_page['page_url'],
        initial_page=config['initial_page'],
        list_xpath=config['list_xpath'],
        title_xpath=config['title_xpath'],
        url_xpath=config['url_xpath'],
        publish_time_xpath=config['publish_time_xpath'],
        publish_time_format=config['publish_time_format'],
        publisher_group=config.get('publisher_group', '')
    )

    with open(SUBCLASS_TEMPLATE, 'r') as fp:
        subclass_template = fp.read()
    subclasses = []
    for page in config['pages'][1:]:
        page_name = name + re.split(r'[\s,_\-]', page['name'])
        class_name = get_camel_case(page_name + ['spider'])
        subclass_res = subclass_template.format(
            subclass_name=class_name,
            super_class=super_class_name,
            spider_name=get_snake_case(page_name),
            publisher=page.get('publisher', config['publisher']),
            source=page.get('source', config['source']),
            column=page.get('column', config.get('column', [])),
            initial_url=page['initial_url'],
            page_url=page['page_url'],
        )
        subclasses.append(subclass_res)

    with open(WRAPPER_TEMPLATE, 'r') as fp:
        wrapper_template = fp.read()
    return wrapper_template.format(
        version=VERSION,
        spider_class=class_res,
        subclasses='\n\n\n'.join(subclasses)
    )


def get_camel_case(words):
    return ''.join([word.lower().capitalize() for word in words])


def get_snake_case(words):
    return '_'.join([word.lower() for word in words])


if __name__ == "__main__":
    main(sys.argv[1:])
