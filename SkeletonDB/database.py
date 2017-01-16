#!/usr/bin/env python

import os
import json
import ligneous

logger = ligneous.log("database") 


def load(location="skeleton.db", fsave=True, verbose=True):
    '''Return a SkeletonDB object. location is the path to the json file.'''
    return Database(location, fsave, verbose)


class Database(object):

    def __init__(self, location="skeleton.db", fsave=True, verbose=True):
        '''Creates a database object and loads the data from the location path.
        If the file does not exist it will be created on the first update.'''
        self.verbose = verbose
        self.load(location, fsave)

    def load(self, location, fsave):
        '''Loads, reloads or changes the path to the db file.'''
        location = os.path.expanduser(location)
        self.location = location
        self.fsave = fsave
        if os.path.exists(location):
            self._loaddb()
        else:
            self.db = {}

    def dump(self):
        '''Force dump memory db to file.'''
        self._dumpdb(True)

    def set(self, key, value):
        '''Set the (string,int,whatever) value of a key'''
        self.db[key] = value
        if self.verbose: 
            logger.info("insert")
        self._dumpdb(self.fsave)
        return True

    def get(self, key):
        '''Get the value of a key'''
        try:
            return self.db[key]
        except KeyError:
            return None

    def keys(self,key=None):
        '''Returns list containing keys of database or dict entry'''
        if key:
            return list(self.db[key].keys())
        return list(self.db.keys())

    def reload(self):
        '''Reloads database'''
        self._loaddb(self.fsave)

    def exists(self,key):
        '''Checks if key exists in database'''
        if key not in self.db:
            return False
        else:
            return True

    def remove(self, key):
        '''Delete a key'''
        if key in self.db:
            del self.db[key]
            self._dumpdb(self.fsave)
        return True

    def _deldb(self):
        '''Delete everything from the database'''
        self.db= {}
        self._dumpdb(self.fsave)
        return True

    def _loaddb(self):
        '''Load or reload the json info from the file'''
        if self.verbose: 
            logger.info("load from database")
        self.db = json.load(open(self.location))

    def _dumpdb(self, forced):
        '''Write/save the json dump into the file'''
        if forced:
            if self.verbose: 
                logger.info("commit")
            json.dump(self.db, open(self.location, 'w'))


