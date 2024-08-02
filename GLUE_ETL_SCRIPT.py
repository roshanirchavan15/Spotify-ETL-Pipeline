import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node Artist
Artist_node1719427579886 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://myspotifyproj/Staging/Artist.csv"], "recurse": True}, transformation_ctx="Artist_node1719427579886")

# Script generated for node Albums
Albums_node1719427580502 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://myspotifyproj/Staging/Albums.csv"], "recurse": True}, transformation_ctx="Albums_node1719427580502")

# Script generated for node Tracks
Tracks_node1719427581172 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://myspotifyproj/Staging/Tracks.csv"], "recurse": True}, transformation_ctx="Tracks_node1719427581172")

# Script generated for node Join Album and Artist
JoinAlbumandArtist_node1719427691369 = Join.apply(frame1=Albums_node1719427580502, frame2=Artist_node1719427579886, keys1=["artist_id"], keys2=["id"], transformation_ctx="JoinAlbumandArtist_node1719427691369")

# Script generated for node Join with Tracks
JoinwithTracks_node1719428006030 = Join.apply(frame1=JoinAlbumandArtist_node1719427691369, frame2=Tracks_node1719427581172, keys1=["track_id"], keys2=["track_id"], transformation_ctx="JoinwithTracks_node1719428006030")

# Script generated for node Drop Fields
DropFields_node1719428075733 = DropFields.apply(frame=JoinwithTracks_node1719428006030, paths=["`.track_id`", "id"], transformation_ctx="DropFields_node1719428075733")

# Script generated for node Destination
Destination_node1719428130646 = glueContext.write_dynamic_frame.from_options(frame=DropFields_node1719428075733, connection_type="s3", format="glueparquet", connection_options={"path": "s3://myspotifyproj/Datawarehouse/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="Destination_node1719428130646")

job.commit()