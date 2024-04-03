# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromadb/proto/chroma.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x63hromadb/proto/chroma.proto\x12\x06\x63hroma\"&\n\x06Status\x12\x0e\n\x06reason\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x05\"U\n\x06Vector\x12\x11\n\tdimension\x18\x01 \x01(\x05\x12\x0e\n\x06vector\x18\x02 \x01(\x0c\x12(\n\x08\x65ncoding\x18\x03 \x01(\x0e\x32\x16.chroma.ScalarEncoding\"\x1a\n\tFilePaths\x12\r\n\x05paths\x18\x01 \x03(\t\"\xa5\x02\n\x07Segment\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12#\n\x05scope\x18\x03 \x01(\x0e\x32\x14.chroma.SegmentScope\x12\x17\n\ncollection\x18\x05 \x01(\tH\x00\x88\x01\x01\x12-\n\x08metadata\x18\x06 \x01(\x0b\x32\x16.chroma.UpdateMetadataH\x01\x88\x01\x01\x12\x32\n\nfile_paths\x18\x07 \x03(\x0b\x32\x1e.chroma.Segment.FilePathsEntry\x1a\x43\n\x0e\x46ilePathsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12 \n\x05value\x18\x02 \x01(\x0b\x32\x11.chroma.FilePaths:\x02\x38\x01\x42\r\n\x0b_collectionB\x0b\n\t_metadata\"\xd1\x01\n\nCollection\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12-\n\x08metadata\x18\x04 \x01(\x0b\x32\x16.chroma.UpdateMetadataH\x00\x88\x01\x01\x12\x16\n\tdimension\x18\x05 \x01(\x05H\x01\x88\x01\x01\x12\x0e\n\x06tenant\x18\x06 \x01(\t\x12\x10\n\x08\x64\x61tabase\x18\x07 \x01(\t\x12\x14\n\x0clog_position\x18\x08 \x01(\x03\x12\x0f\n\x07version\x18\t \x01(\x05\x42\x0b\n\t_metadataB\x0c\n\n_dimension\"4\n\x08\x44\x61tabase\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06tenant\x18\x03 \x01(\t\"\x16\n\x06Tenant\x12\x0c\n\x04name\x18\x01 \x01(\t\"b\n\x13UpdateMetadataValue\x12\x16\n\x0cstring_value\x18\x01 \x01(\tH\x00\x12\x13\n\tint_value\x18\x02 \x01(\x03H\x00\x12\x15\n\x0b\x66loat_value\x18\x03 \x01(\x01H\x00\x42\x07\n\x05value\"\x96\x01\n\x0eUpdateMetadata\x12\x36\n\x08metadata\x18\x01 \x03(\x0b\x32$.chroma.UpdateMetadata.MetadataEntry\x1aL\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12*\n\x05value\x18\x02 \x01(\x0b\x32\x1b.chroma.UpdateMetadataValue:\x02\x38\x01\"\xaf\x01\n\x0fOperationRecord\x12\n\n\x02id\x18\x01 \x01(\t\x12#\n\x06vector\x18\x02 \x01(\x0b\x32\x0e.chroma.VectorH\x00\x88\x01\x01\x12-\n\x08metadata\x18\x03 \x01(\x0b\x32\x16.chroma.UpdateMetadataH\x01\x88\x01\x01\x12$\n\toperation\x18\x04 \x01(\x0e\x32\x11.chroma.OperationB\t\n\x07_vectorB\x0b\n\t_metadata\"C\n\x15VectorEmbeddingRecord\x12\n\n\x02id\x18\x01 \x01(\t\x12\x1e\n\x06vector\x18\x03 \x01(\x0b\x32\x0e.chroma.Vector\"a\n\x11VectorQueryResult\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08\x64istance\x18\x03 \x01(\x02\x12#\n\x06vector\x18\x04 \x01(\x0b\x32\x0e.chroma.VectorH\x00\x88\x01\x01\x42\t\n\x07_vector\"@\n\x12VectorQueryResults\x12*\n\x07results\x18\x01 \x03(\x0b\x32\x19.chroma.VectorQueryResult\"4\n\x11GetVectorsRequest\x12\x0b\n\x03ids\x18\x01 \x03(\t\x12\x12\n\nsegment_id\x18\x02 \x01(\t\"D\n\x12GetVectorsResponse\x12.\n\x07records\x18\x01 \x03(\x0b\x32\x1d.chroma.VectorEmbeddingRecord\"\x86\x01\n\x13QueryVectorsRequest\x12\x1f\n\x07vectors\x18\x01 \x03(\x0b\x32\x0e.chroma.Vector\x12\t\n\x01k\x18\x02 \x01(\x05\x12\x13\n\x0b\x61llowed_ids\x18\x03 \x03(\t\x12\x1a\n\x12include_embeddings\x18\x04 \x01(\x08\x12\x12\n\nsegment_id\x18\x05 \x01(\t\"C\n\x14QueryVectorsResponse\x12+\n\x07results\x18\x01 \x03(\x0b\x32\x1a.chroma.VectorQueryResults*8\n\tOperation\x12\x07\n\x03\x41\x44\x44\x10\x00\x12\n\n\x06UPDATE\x10\x01\x12\n\n\x06UPSERT\x10\x02\x12\n\n\x06\x44\x45LETE\x10\x03*(\n\x0eScalarEncoding\x12\x0b\n\x07\x46LOAT32\x10\x00\x12\t\n\x05INT32\x10\x01*(\n\x0cSegmentScope\x12\n\n\x06VECTOR\x10\x00\x12\x0c\n\x08METADATA\x10\x01\x32\xa2\x01\n\x0cVectorReader\x12\x45\n\nGetVectors\x12\x19.chroma.GetVectorsRequest\x1a\x1a.chroma.GetVectorsResponse\"\x00\x12K\n\x0cQueryVectors\x12\x1b.chroma.QueryVectorsRequest\x1a\x1c.chroma.QueryVectorsResponse\"\x00\x42:Z8github.com/chroma-core/chroma/go/pkg/proto/coordinatorpbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chromadb.proto.chroma_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z8github.com/chroma-core/chroma/go/pkg/proto/coordinatorpb'
  _SEGMENT_FILEPATHSENTRY._options = None
  _SEGMENT_FILEPATHSENTRY._serialized_options = b'8\001'
  _UPDATEMETADATA_METADATAENTRY._options = None
  _UPDATEMETADATA_METADATAENTRY._serialized_options = b'8\001'
  _globals['_OPERATION']._serialized_start=1775
  _globals['_OPERATION']._serialized_end=1831
  _globals['_SCALARENCODING']._serialized_start=1833
  _globals['_SCALARENCODING']._serialized_end=1873
  _globals['_SEGMENTSCOPE']._serialized_start=1875
  _globals['_SEGMENTSCOPE']._serialized_end=1915
  _globals['_STATUS']._serialized_start=39
  _globals['_STATUS']._serialized_end=77
  _globals['_VECTOR']._serialized_start=79
  _globals['_VECTOR']._serialized_end=164
  _globals['_FILEPATHS']._serialized_start=166
  _globals['_FILEPATHS']._serialized_end=192
  _globals['_SEGMENT']._serialized_start=195
  _globals['_SEGMENT']._serialized_end=488
  _globals['_SEGMENT_FILEPATHSENTRY']._serialized_start=393
  _globals['_SEGMENT_FILEPATHSENTRY']._serialized_end=460
  _globals['_COLLECTION']._serialized_start=491
  _globals['_COLLECTION']._serialized_end=700
  _globals['_DATABASE']._serialized_start=702
  _globals['_DATABASE']._serialized_end=754
  _globals['_TENANT']._serialized_start=756
  _globals['_TENANT']._serialized_end=778
  _globals['_UPDATEMETADATAVALUE']._serialized_start=780
  _globals['_UPDATEMETADATAVALUE']._serialized_end=878
  _globals['_UPDATEMETADATA']._serialized_start=881
  _globals['_UPDATEMETADATA']._serialized_end=1031
  _globals['_UPDATEMETADATA_METADATAENTRY']._serialized_start=955
  _globals['_UPDATEMETADATA_METADATAENTRY']._serialized_end=1031
  _globals['_OPERATIONRECORD']._serialized_start=1034
  _globals['_OPERATIONRECORD']._serialized_end=1209
  _globals['_VECTOREMBEDDINGRECORD']._serialized_start=1211
  _globals['_VECTOREMBEDDINGRECORD']._serialized_end=1278
  _globals['_VECTORQUERYRESULT']._serialized_start=1280
  _globals['_VECTORQUERYRESULT']._serialized_end=1377
  _globals['_VECTORQUERYRESULTS']._serialized_start=1379
  _globals['_VECTORQUERYRESULTS']._serialized_end=1443
  _globals['_GETVECTORSREQUEST']._serialized_start=1445
  _globals['_GETVECTORSREQUEST']._serialized_end=1497
  _globals['_GETVECTORSRESPONSE']._serialized_start=1499
  _globals['_GETVECTORSRESPONSE']._serialized_end=1567
  _globals['_QUERYVECTORSREQUEST']._serialized_start=1570
  _globals['_QUERYVECTORSREQUEST']._serialized_end=1704
  _globals['_QUERYVECTORSRESPONSE']._serialized_start=1706
  _globals['_QUERYVECTORSRESPONSE']._serialized_end=1773
  _globals['_VECTORREADER']._serialized_start=1918
  _globals['_VECTORREADER']._serialized_end=2080
# @@protoc_insertion_point(module_scope)
