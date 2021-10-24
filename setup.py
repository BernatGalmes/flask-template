from distutils.core import setup

setup(
    name='flask-template',
    version='v0.0.1',
    packages=['api'],
    url='',
    license='',
    author='Bernat Galmés Rubert',
    author_email='rubit.consultor@gmail.com',
    description='Template for any flask project',
    install_requires=[
        'click==7.1.2',
        'Flask==2.0.2',
        'flask-marshmallow==0.14.0',
        'Flask-RESTful==0.3.9',
        'Flask-SQLAlchemy==2.5.1',
        'marshmallow==3.14.0',
        'marshmallow-sqlalchemy==0.26.1',
        'python-dotenv==0.19.1',
        'requests==2.26.0',
        'SQLAlchemy==1.4.26',
    ]
)
