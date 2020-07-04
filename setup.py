from distutils.core import setup

setup(
    name='dectext',
    packages = ['dectext'],
    version="0.01",
    license='MIT', 
    description = 'It print a decorated text on console.',
    author = 'Saurabh Gujjar',
    author_email = 'saurabhpanwar127@gmail.com',
    url = 'https://github.com/SaurabhGujjar/dectext.git', 
    download_url = 'https://github.com/SaurabhGujjar/dectext/archive/v_0.01.tar.gz',
    keywords = ['TEXT', 'DECORATION', 'CONSOLE'],

    py_modules=['dectext'],
    install_requires=['Click', 'pyfiglet', 'random2', ],
    entry_points=''' 
    [console_scripts]
    dectext = dec:main
    ''',

    classifiers=[
    'Development Status :: 3 - Alpha',    
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3',  
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ]

)