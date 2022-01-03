const kafka = require('kafka-node');
const express = require('express');
const port = 3000;
const app = express();

//Consumer topic & partitions
var topics = [
  { topic: 'live_detection_topic', partition: 0 },
  { topic: 'live_detection_topic', partition: 1 },
  { topic: 'live_detection_topic', partition: 2 },
  { topic: 'live_detection_topic', partition: 3 },
  { topic: 'live_detection_topic', partition: 4 },
  { topic: 'live_detection_topic', partition: 5 },
  { topic: 'live_detection_topic', partition: 6 },
  { topic: 'live_detection_topic', partition: 7 },
  { topic: 'live_detection_topic', partition: 8 },
  { topic: 'live_detection_topic', partition: 9 },
];

var options = {
  autoCommit: false,
};


const Consumer = kafka.Consumer,
client = new kafka.KafkaClient('localhost:9092'),
consumer = new Consumer(client, 
                        topics,
                        { groupId: 'consumer' },
                        options);


const server = app.listen(port, () => {
  console.log(`Listening on port ${server.address().port}`);
});
const io = require('socket.io')(server, {
  cors: {
    origin: '*',
  }
});

io.on(
  'connection', client => {
  console.log('Connected', client);

  consumer.on('message', function (message) {
      console.log(message)
      client.emit('livemap', message);
  });

  consumer.on('error', function(err) {
    console.log('error', err);
  });

  client.on('disconnect', () => {
      console.log('Client disconnected');
  });
});