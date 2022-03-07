from setuptools import setup, find_packages

setup(
    name='notify_scrapy',
    version='0.3.2',
    packages=find_packages(),
    entry_points={'scrapy': ['settings = notify_scrapy.settings']},
    license='MIT',
    author='Zhou Haoyang',
    editor='Li Yuqian',
    description='The scrapy project of Notify.',
    install_requires=[
        'mysqlclient>=2.0.3',
        'Scrapy>=2.5.0',
        'pytz>=2021.1'
    ]
)
