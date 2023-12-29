import logging

import psycopg2

from database import database_connection_pool

logger = logging.getLogger()

class Vote:
    """PostgreSQL Database class."""

    def __init__(self):
        self.__database_connection_pool = database_connection_pool


    async def get_server_vote(self, server_id):
        try:
            logger.info(f'get server {server_id} all votes')
            sql = """ SELECT id, name, description, activity_date, end_time FROM vote WHERE server_id=%s order by id"""
            conn = await self.__database_connection_pool.connect()
            
            with conn.cursor() as cur:
                cur.execute(sql, (server_id,))
                records = cur.fetchall()

        except psycopg2.DatabaseError as e:
            logger.error(e)
            raise e

        finally:
            if conn:
                self.__database_connection_pool.disConnect(conn)
            return records


    async def get_vote(self, id):
        try:
            logger.info(f'get vote {id}')
            sql = """SELECT id, name, description, activity_date, end_time FROM vote WHERE id=%s"""

            conn = await self.__database_connection_pool.connect()

            with conn.cursor() as cur:
                cur.execute(sql, (id,))
                record = cur.fetchone()

        except psycopg2.DatabaseError as e:
            logger.error(e)
            raise e

        finally:
            if conn:
                self.__database_connection_pool.disConnect(conn)
            return record


    async def get_option_voter(self, id):
        try:
            logger.info(f'get vote {id} detail')
            sql = """ 
                        SELECT o.name option, r.name voter
                        FROM vote_option o
                        LEFT JOIN vote_voter r
                        ON o.id = r.o_id
                        WHERE v_id=%s
                  """

            conn = await self.__database_connection_pool.connect()

            with conn.cursor() as cur:
                cur.execute(sql, (id,))
                records = cur.fetchall()

        except psycopg2.DatabaseError as e:
            logger.error(e)
            raise e

        finally:
            if conn:
                self.__database_connection_pool.disConnect(conn)
            return records


    async def insert_vote(self, insertTuple):
        logger.info("insert vote")
        try:
            sql = """ INSERT INTO vote 
                    (name, description, activity_date, end_time, server_id)
                    VALUES(%s, %s, %s, %s, %s)
                    RETURNING id"""
            conn = await self.__database_connection_pool.connect()

            with conn.cursor() as cur:
                cur.execute(sql, insertTuple)
                conn.commit()
                id = cur.fetchone()

            logger.info('insert successfully.')

        except psycopg2.DatabaseError as e:
            if conn:
                conn.rollback()
            logger.error(e)
            raise e

        finally:
            if conn:
                self.__database_connection_pool.disConnect(conn)
            
            return id


    async def insert_option(self, insertTuple):
        logger.info("insert option")
        try:
            sql = """ INSERT INTO vote_option
                        (name, v_id)
                        VALUES(%s, %s)"""
            conn = await self.__database_connection_pool.connect()


            with conn.cursor() as cur:
                cur.execute(sql, insertTuple)
                conn.commit()

            logger.info('insert successfully.')

        except psycopg2.DatabaseError as e:
            if conn:
                conn.rollback()
            logger.error(e)
            raise e

        finally:
            if conn:
                self.__database_connection_pool.disConnect(conn)


    async def insert_voter(self, insertTuple):
        logger.info("insert voter")
        try:
            sql = """ INSERT INTO vote_voter
                        (name, o_id)
                        VALUES(%s, %s)"""
            conn = await self.__database_connection_pool.connect()


            with conn.cursor() as cur:
                cur.execute(sql, insertTuple)
                conn.commit()

            logger.info('insert successfully.')

        except psycopg2.DatabaseError as e:
            if conn:
                conn.rollback()
            logger.error(e)
            raise e

        finally:
            if conn:
                self.__database_connection_pool.disConnect(conn)


    async def delete_vote(self, id):
        try:
            sql = """ DELETE FROM vote WHERE id=%s """

            conn = await self.__database_connection_pool.connect()
            with conn.cursor() as cur:
                cur.execute(sql, (id,))

        except psycopg2.DatabaseError as e:
            logger.error(e)
            raise e

        finally:
            if conn:
                self.__database_connection_pool.disConnect(conn) 
        

vote_db = Vote()