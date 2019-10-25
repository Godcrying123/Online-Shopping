from setuptools import setup, find_packages

setup(
    name='shopsite',
    version='${version}',
    description='My Online Shoping Site on Django',
    author='zhkai',
    author_email='jackson.zhang1@hotmail.com',
    url='https://github.com/Godcrying123/',
    license='MIT',
    packages=find_packages('shopsite'),
    package_dir={'': 'shopsite'},
    # package_data={'': [
    #     'shopsite/shopsite/*',
    # ]},
    include_package_data=True,
    install_requires=[
        # 'django==2.2.6',
        # 'Pillow==6.2.0',
        # 'WeasyPrint==0.42.3',
        # 'braintree==3.57.1',
        # 'celery==4.3.0',
        # 'coreapi==2.3.3',
        # 'django-parler==2.0',
        # 'django-rosetta==0.8.1',
        # 'djangorestframework==3.10.3',
        # 'eventlet==0.25.1',
        # 'flower==0.9.2',
        # 'Jinja2==2.10.3',
        # 'Pygments==2.4.2',
        # 'amqp==2.5.1',
        # 'django-redis==4.10.0',
        # 'redis==3.3.10',
        # 'hiredis==1.0.0',
        # # 'mysqlclient==1.4.4',
        # 'pymysql==0.9.3',
    ],
    extras_require={
      'ipython': ['ipython==7.8.0']
    },
    scripts=[
        'shopsite/manage.py',
    ],
    entry_points={
        'console_scripts': [
            'shopsite_manage = manage:main',
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.7',
    ],
)
