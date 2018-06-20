import asyncio
import json
import requests

class AServer(object):
    """
        Initalizes a new asynchronous server object.
        This server invokes methods with request_type decorators,
        when data is read. See requests.py
    """

    def __init__(self, port):

        self.port = port

        # constants
        self.BUFFER_SIZE = 512

        # privates
        self.__writer = None
        self.__alive = False
        self.__loop = None


    def start(self):
        """
            Starts the asynchronous server on the given port.
        """
        self.__loop = asyncio.get_event_loop()
        self.__alive = True
        coro = asyncio.start_server(self.handle_connection, 'localhost', self.port)
        self.__loop.run_until_complete(coro)
        try:
            self.__loop.run_forever()
        finally:
            self.__loop.close()


    def stop(self):
        """
            Stops the asynchronous server.
        """
        self.__loop.stop()
        self.__alive = False


    async def handle_connection(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        """
            Handles a new client connection using NIO.
            When reading, it invokes the suitable request callback depending
            on the JSON request.

            :param: reader, the stream reader to read data from (in bytes)
            :param: writer, the stream writer to write data to (in bytes)
        """
        print("Incoming client connection")

        try:
            self.__writer = writer

            while self.__alive:
                data = await reader.readline()
                data = data.decode('ascii')

                try:
                    # try parse the JSON, then get the type of request
                    data = json.loads(data)

                    # if it's a /terminate/ type, terminate the server
                    if(data['type'] == 'terminate'):
                        self.stop()

                    # invoke a callback belonging to a requset type if it is available
                    funcs = requests.get_types()
                    if(funcs.get(data['type'])):    
                        await funcs[data['type']](self, data)

                except:
                    pass

        except ConnectionError:
            self._writer = None



    async def write(self, message: str):
        """
            Writes data to the stream writer and then
            closes the server (for now)
        """
        if self.__writer == None:
            return

        self.__writer.write(message.encode())
        await self.__writer.drain()
        self.stop()


# testing
if __name__ == "__main__":
    server = AServer(6000)
    server.start()
