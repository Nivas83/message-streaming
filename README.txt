Producer will stream the same sample response with 1 second interval


Step 1: Start kafka & zookeeper

Terminal 1: ./initKafka.sh



Step 2: Start Kafka Consumer & Socket server

install required node packages & start socket server & kafka consumer by running the following command 

Terminal 2:

    npm i

    node server_consumer.js



Step 3: Faust Producer

install required python packages & start producer by running the following command

Terminal 3:

    pip install -r requirements.txt

    faust -A faust_producer worker -l info



Step 4: Open Web application

install required node packages & start Angular project

Socket is listening on 'http://localhost:3000' & receive events 'livemap'

Terminal 4:

    cd frontend

    npm i

    npm start

Open console to view received events