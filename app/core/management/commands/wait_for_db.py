
# django command to wait_for_db to be available
import time
from django import db
from psycopg2 import OperationalError as Psycopg2OpError
from django.db.utils import OperationalError 
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    # django command to wait_for_db

    def handle(self,*args,**options):
        self.stdout.write('waiting for db')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except(Psycopg2OpError,OperationalError):
                self.stdout.write('DB unavilable, wait for 1 sec')
                time.sleep(1)
        
        self.stdout.write(self.style.SUCCESS('Db available'))