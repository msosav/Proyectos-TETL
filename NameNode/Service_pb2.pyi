from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateRequest(_message.Message):
    __slots__ = ("file_name", "num_partitions", "size")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    NUM_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    num_partitions: int
    size: int
    def __init__(self, file_name: _Optional[str] = ..., num_partitions: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("partitions", "status_code")
    class PartitionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    partitions: _containers.ScalarMap[str, str]
    status_code: int
    def __init__(self, partitions: _Optional[_Mapping[str, str]] = ..., status_code: _Optional[int] = ...) -> None: ...

class SendPartitionRequest(_message.Message):
    __slots__ = ("file_name", "partition_name", "partition_data", "current_replication")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    PARTITION_NAME_FIELD_NUMBER: _ClassVar[int]
    PARTITION_DATA_FIELD_NUMBER: _ClassVar[int]
    CURRENT_REPLICATION_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    partition_name: str
    partition_data: bytes
    current_replication: int
    def __init__(self, file_name: _Optional[str] = ..., partition_name: _Optional[str] = ..., partition_data: _Optional[bytes] = ..., current_replication: _Optional[int] = ...) -> None: ...

class SendPartitionResponse(_message.Message):
    __slots__ = ("status_code",)
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    status_code: int
    def __init__(self, status_code: _Optional[int] = ...) -> None: ...

class ReplicationUrlRequest(_message.Message):
    __slots__ = ("partition_name", "file_name")
    PARTITION_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    partition_name: str
    file_name: str
    def __init__(self, partition_name: _Optional[str] = ..., file_name: _Optional[str] = ...) -> None: ...

class ReplicationUrlResponse(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class ListFilesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListFilesResponse(_message.Message):
    __slots__ = ("files",)
    class FilesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    FILES_FIELD_NUMBER: _ClassVar[int]
    files: _containers.ScalarMap[str, int]
    def __init__(self, files: _Optional[_Mapping[str, int]] = ...) -> None: ...
