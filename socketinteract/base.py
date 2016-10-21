import pymysql.cursors
import settings

class base():
    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='',
                                     db='pygame',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

    def fail(self, error):
        return { 'fail':error }


    def request(self, function, params = 0):
        #Called by incoming data
        toReturn = self.fail('1034: Function Not Found')

        if(function =='auth'):
            #Do Auth
            toReturn = self.fail('1034: Auth Not Found')

        elif(function=='score'):
            #do Score
            toReturn = self.fail('1034: Score Not Found')


        '''
        try:
            with self.onnection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `test` (`name`) VALUES (%s)"
                cursor.execute(sql, ('webmaster@python.org'))

            self.connection.commit()

            with self.connection.cursor() as cursor:

                # Read a single record
                sql = "SELECT `name` FROM `test` WHERE `id`=%s"
                cursor.execute(sql, (1))
                result = cursor.fetchone()
                print(result)

        finally:
            self.connection.close()

        '''
        return toReturn