while true; do
	echo "Starting MS API"
	python camera_image.py
	python ms_visionapi.py
	python aws_dynamodb.py
	python audio.py
	sleep 0.25 
done 
