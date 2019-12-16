# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    List as typing___List,
    Optional as typing___Optional,
    Text as typing___Text,
    Tuple as typing___Tuple,
    cast as typing___cast,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class CheckSDCardRequest(google___protobuf___message___Message):

    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> CheckSDCardRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class CheckSDCardResponse(google___protobuf___message___Message):
    inserted = ... # type: bool

    def __init__(self,
        *,
        inserted : typing___Optional[bool] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> CheckSDCardResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"inserted"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"inserted",b"inserted"]) -> None: ...

class DeviceInfoRequest(google___protobuf___message___Message):

    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> DeviceInfoRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class DeviceInfoResponse(google___protobuf___message___Message):
    name = ... # type: typing___Text
    initialized = ... # type: bool
    version = ... # type: typing___Text
    mnemonic_passphrase_enabled = ... # type: bool
    monotonic_increments_remaining = ... # type: int

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        initialized : typing___Optional[bool] = None,
        version : typing___Optional[typing___Text] = None,
        mnemonic_passphrase_enabled : typing___Optional[bool] = None,
        monotonic_increments_remaining : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> DeviceInfoResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"initialized",u"mnemonic_passphrase_enabled",u"monotonic_increments_remaining",u"name",u"version"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"initialized",b"initialized",u"mnemonic_passphrase_enabled",b"mnemonic_passphrase_enabled",u"monotonic_increments_remaining",b"monotonic_increments_remaining",u"name",b"name",u"version",b"version"]) -> None: ...

class InsertRemoveSDCardRequest(google___protobuf___message___Message):
    class SDCardAction(int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> InsertRemoveSDCardRequest.SDCardAction: ...
        @classmethod
        def keys(cls) -> typing___List[str]: ...
        @classmethod
        def values(cls) -> typing___List[InsertRemoveSDCardRequest.SDCardAction]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[str, InsertRemoveSDCardRequest.SDCardAction]]: ...
        REMOVE_CARD = typing___cast(InsertRemoveSDCardRequest.SDCardAction, 0)
        INSERT_CARD = typing___cast(InsertRemoveSDCardRequest.SDCardAction, 1)
    REMOVE_CARD = typing___cast(InsertRemoveSDCardRequest.SDCardAction, 0)
    INSERT_CARD = typing___cast(InsertRemoveSDCardRequest.SDCardAction, 1)

    action = ... # type: InsertRemoveSDCardRequest.SDCardAction

    def __init__(self,
        *,
        action : typing___Optional[InsertRemoveSDCardRequest.SDCardAction] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> InsertRemoveSDCardRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"action"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"action",b"action"]) -> None: ...

class ResetRequest(google___protobuf___message___Message):

    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ResetRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class SetDeviceLanguageRequest(google___protobuf___message___Message):
    language = ... # type: typing___Text

    def __init__(self,
        *,
        language : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> SetDeviceLanguageRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"language"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"language",b"language"]) -> None: ...

class SetDeviceNameRequest(google___protobuf___message___Message):
    name = ... # type: typing___Text

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> SetDeviceNameRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"name"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"name",b"name"]) -> None: ...

class SetPasswordRequest(google___protobuf___message___Message):
    entropy = ... # type: bytes

    def __init__(self,
        *,
        entropy : typing___Optional[bytes] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> SetPasswordRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"entropy"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"entropy",b"entropy"]) -> None: ...