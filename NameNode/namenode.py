"""
NameNode
"""
from concurrent import futures
import grpc
import Service_pb2
import Service_pb2_grpc
import random
from threading import Thread
import time

# Diccionario que almacena los datanodes y los archivos que contienen
datanodes = {}
active_datanodes = []
files = {}
heartbeats = {}


def distribute_file(file_name, num_partitions, size, response):
    """
    Distribuye un archivo en los datanodes
    param file_name: El nombre del archivo
    param num_partitions: La lista de partes del archivo
    return: El diccionario de datanodes
    """
    datanode_index = 0
    for i in range(num_partitions):
        if datanode_index >= len(active_datanodes):
            datanode_index = 0
        response.partitions[partition_name(
            i)] = active_datanodes[datanode_index]
        datanodes[file_name] = {partition_name(
            i): active_datanodes[datanode_index]}
        datanode_index += 1
    files[file_name] = size
    return response


def partition_name(i):
    """
    Genera el nombre de la partición
    param i: El número de la partición
    return: El nombre de la partición
    """
    length = len(str(i))
    serial = "0" * (4 - length) + str(i)
    name = f"part-{serial}"
    return name


def locate_file(file_name):
    """
    Localiza un archivo
    param file_name: El nombre del archivo
    return: La lista de ubicaciones del archivo
    """
    if file_name not in datanodes:
        return []
    return datanodes[file_name]


class NameNodeServicer(Service_pb2_grpc.NameNodeServicer):
    def Create(self, request, context):
        """
        Crea un archivo
        param request: El archivo a crear
        return: El diccionario de datanodes
        """
        file_name = request.file_name
        num_partitions = request.num_partitions
        size = request.size
        response = Service_pb2.CreateResponse()
        response = distribute_file(file_name, num_partitions, size, response)
        return response

    def ListFiles(self, request, context):
        """
        Lista los archivos
        return: None
        """
        response = Service_pb2.ListFilesResponse()
        for key, value in files.items():
            response.files[key] = value
        return response

    def ReplicationUrl(self, request, context):
        """
        Realiza una solicitud a la URL
        param request: La solicitud
        return: La URL
        """
        if not active_datanodes:
            return Service_pb2.ReplicationUrlResponse(url="")
        partitions_of_file = datanodes[request.file_name]
        if request.partition_name not in partitions_of_file.keys():
            url = random.choice(active_datanodes)
            return Service_pb2.ReplicationUrlResponse(url=url)
        else:
            active_urls = [
                x for x in active_datanodes if x not in partitions_of_file]
            if not active_urls:
                return Service_pb2.ReplicationUrlResponse(url="")
            url = random.choice(active_urls)
            return Service_pb2.ReplicationUrlResponse(url=url)

    def HeartBeat(self, request, context):
        """
        Realiza un latido
        param request: El latido
        return: None
        """
        if request.url not in active_datanodes:
            active_datanodes.append(request.url)
        heartbeats[request.url] = request.timestamp
        return Service_pb2.HeartBeatResponse(message="OK")


def file_system(option):
    """
    Muestra el sistema de archivos
    param option: La opción a mostrar
    return: None
    """
    if option == "ls":
        return files
    else:
        return "Invalid option"


def monitor_heartbeats():
    while True:
        time.sleep(15)
        current_time = int(time.time())
        for url, timestamp in list(heartbeats.items()):
            if current_time - timestamp > 15:
                print(f"DataNode {url} is inactive, removing from active list")
                active_datanodes.remove(url)
                del heartbeats[url]


if __name__ == "__main__":
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Service_pb2_grpc.add_NameNodeServicer_to_server(
        NameNodeServicer(), server)
    server.add_insecure_port('localhost:8080')
    server.start()
    print("NameNode running at port 8080.")
    monitor_heartbeats_thread = Thread(target=monitor_heartbeats)
    monitor_heartbeats_thread.daemon = True
    monitor_heartbeats_thread.start()
    server.wait_for_termination()
