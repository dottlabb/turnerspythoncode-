import boto3

client = boto3.client('s3', region_name='ap-southeast-2')

client.upload_file('truck1.jpg', 'missionreadycartest', 'truck1.jpg')
